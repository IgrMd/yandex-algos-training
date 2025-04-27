#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstddef>
#include <cstdint>
#include <fstream>
#include <iosfwd>
#include <iostream>
#include <limits>
#include <optional>
#include <queue>
#include <random>
#include <ranges>
#include <sstream>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>
#include <map>

using namespace std::string_literals;

class Arhiver {
protected:
	std::vector<unsigned char> packed;
	class BitStreamIn {
		Arhiver& owner;
		int block_index = 0;
		int bit_index = 0;
	public:

		explicit BitStreamIn(Arhiver& owner) : owner{ owner } {}
		BitStreamIn& operator >> (bool& out);
		operator bool () const;
	};

	class BitStreamOut {
		Arhiver& owner;
		unsigned char* block = nullptr;
		int bit_index = 0;
	public:

		explicit BitStreamOut(Arhiver& owner) : owner{ owner }, block{ owner.NextBlock() } {}
		BitStreamOut& operator << (bool out);
	};

	BitStreamIn InStream() { return BitStreamIn{ *this }; }
	BitStreamOut OutStream() { return BitStreamOut{ *this }; }
	unsigned char* NextBlock() { return &packed.emplace_back(); }
};

Arhiver::BitStreamOut& Arhiver::BitStreamOut::operator<<(bool out) {
	if (out) {
		*block |= 1 << bit_index;
	} else {
		*block &= ~(1 << bit_index);
	}
	if (++bit_index == 8) {
		block = owner.NextBlock();
		bit_index = 0;
	}
	return *this;
}

Arhiver::BitStreamIn& Arhiver::BitStreamIn::operator>>(bool& out) {
	if (block_index >= owner.packed.size()) {
		out = false;
	} else {
		out = owner.packed[block_index] & 1 << (bit_index++);
	}
	if (bit_index == 8) {
		++block_index;
		bit_index = 0;
	}
	return *this;
}

Arhiver::BitStreamIn::operator bool() const {
	return block_index < owner.packed.size();
}

class LWZArhiver : public Arhiver {
	static const char TERM = 'z' + 1;
	static const char EXTEND = 'z' + 2;
	static const char POS_WIDTH = 5;
	static const char DISPL = 'a';
	static const int CHAR_WIDTH = 5;
	struct WordInfo {
		int id = 0;
		char added{};
		int prev = 0;
	};

	std::vector<std::string> words;
	std::unordered_map<std::string, WordInfo> word_map;
	void Clear();

public:
	LWZArhiver() { Clear(); }
	auto Pack(const std::string& data) -> std::vector<unsigned char>;
	auto Unpack(std::vector<unsigned char> data) -> std::string;
};

void LWZArhiver::Clear() {
	words = { ""s };
	word_map = { {""s, { 0, 0, -1 }} };
	for (char c = 'a'; c <= 'z'; ++c) {
		words.push_back(""s + c);
		word_map[words.back()] = { int(words.size() - 1), c, 0 };
	}
}

auto LWZArhiver::Pack(const std::string& data) -> std::vector<unsigned char> {
	int pos_width = POS_WIDTH;
	int max_pos = 0;
	for (int i = 0; i < pos_width; ++i) {
		max_pos <<= 1;
		max_pos |= 1;
	}
	auto os = OutStream();
	std::string w, wc;
	const auto Write = [&os](int bit_cnt, int val) {
		while (bit_cnt--) {
			os << (val & 1);
			val >>= 1;
		}
	};
	for (char c : data) {
		wc = w + c;
		if (word_map.count(wc)) {
			w = wc;
			continue;
		}
		auto prev = word_map.find(w);
		WordInfo wi;
		wi.added = c;
		wi.id = words.size();
		wi.prev = prev->second.id;
		words.push_back(wc);
		word_map[wc] = wi;
		Write(pos_width, wi.prev);
		Write(CHAR_WIDTH, c - DISPL);
		if (wi.id == max_pos) {
			Write(pos_width, 0);
			Write(CHAR_WIDTH, EXTEND - DISPL);
			++pos_width;
			max_pos <<= 1;
			max_pos |= 1;
		}
		w.clear();
		wc.clear();
	}
	if (!wc.empty()) {
		Write(pos_width, word_map.at(wc).id);
	} else {
		Write(pos_width, 0);
	}
	Write(CHAR_WIDTH, TERM - DISPL);
	return move(packed);
}

auto LWZArhiver::Unpack(std::vector<unsigned char> data) -> std::string {
	packed = std::move(data);
	int pos_width = POS_WIDTH;
	int max_pos = 0;
	for (int i = 0; i < pos_width; ++i) {
		max_pos <<= 1;
		max_pos |= 1;
	}
	auto is = InStream();
	bool read_pos = true;
	std::ostringstream res;
	std::string buf;
	const auto Read = [&is](int bit_cnt) -> int {
		int res = 0;
		for (int i = 0; i < bit_cnt; ++i) {
			bool bit;
			is >> bit;
			res |= (bit << i);
		}
		return res;
	};
	while (is) {
		int id = Read(pos_width);
		char c = Read(CHAR_WIDTH) + DISPL;
		if (c == EXTEND) {
			++pos_width;
			max_pos <<= 1;
			max_pos |= 1;
			continue;
		}
		buf = words.at(id);
		if (c == TERM) {
			res << buf;
			break;
		}
		buf += c;
		res << buf;
		words.push_back(buf);
		buf.clear();
	}
	return res.str();
}

std::string generateRandomString(size_t length) {
	static const std::string chars = "abcdefghijklmnopqrstuvwxyz";
	static std::random_device rd;
	static std::mt19937 gen(rd());
	static std::uniform_int_distribution<> distrib(0, chars.size() - 1);

	std::string result;
	result.reserve(length);
	for (size_t i = 0; i < length; ++i) {
		result += chars[distrib(gen)];
	}
	return result;
}

void test() {
	while (true) {
		std::string s = generateRandomString(50000);
		//string s = "mobqgiqret";
		//ifstream file("input.txt");
		//file >> s;
		LWZArhiver a1;
		auto packed = a1.Pack(s);
		auto size = packed.size();
		std::cout << s.size() * 1. / packed.size() << std::endl;
		LWZArhiver a2;
		auto res = a2.Unpack(packed);
		if (res != s) {
			std::cout << s << std::endl;
			assert(res == s);
		}
	}
}

void LWZ() {
	LWZArhiver a;
	std::string cmd;
	std::cin >> cmd;
	if (cmd == "pack"s) {
		std::string data;
		std::cin >> data;
		auto packed = a.Pack(data);
		std::cout << packed.size() << std::endl;
		bool first = true;
		for (int c : packed) {
			if (first) {
				std::cout << c;
				first = false;
			} else {
				std::cout << ' ' << c;
			}
		}
		std::cout << std::endl;
	}
	if (cmd == "unpack"s) {
		int byte_count = 0;
		std::cin >> byte_count;
		std::vector<unsigned char> packed(byte_count);
		for (int i = 0; i < byte_count; ++i) {
			int byte = 0;
			std::cin >> byte;
			packed.at(i) = byte;
		}
		auto unpacked = a.Unpack(std::move(packed));
		std::cout << unpacked << std::endl;
	}
}

int main() {
	LWZ();
	return 0;
}
