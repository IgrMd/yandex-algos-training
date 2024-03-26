#include <algorithm>
#include <climits>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <queue>
#include <ranges>
#include <set>
#include <stack>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <fstream>
#include <chrono>
#include <iostream>

using namespace std;
namespace rng = ranges;

template <typename Cmp, typename... Args>
int LowerBound(int l, int r, Cmp cmp, Args... args) {
	while (l < r) {
		int mid = (l + r + 1) / 2;
		if (cmp(mid, args...)) {
			l = mid;
		} else {
			r = mid - 1;
		}
	}
	return l;
}

struct Point {
	int x{};
	int y{};
	bool operator==(const Point&) const = default;
	auto operator<=>(const Point&) const = default;
};


struct Party {
	int v, p, i;
};

template <typename Cmp, typename... Args>
int UpperBound(uint64_t l, uint64_t r, Cmp cmp, Args... args) {
	while (l < r) {
		uint64_t mid = (l + r) / 2;
		if (cmp(mid, args...)) {
			r = mid;
		} else {
			l = mid + 1;
		}
	}
	if (!cmp(l, args...)) {
		l += 1;
	}
	return l;
}

bool CanPartyWin(uint64_t amount, int i, int n, vector<Party>& parties, vector<uint64_t>& pref_sums) {
	auto& party = parties[i];
	if (amount < party.p) {
		return false;
	}
	uint64_t can_by = amount - party.p;
	if (can_by == 0) {
		return (i == n - 1) && (parties[i - 1].v < parties[i].v);
	}
	uint64_t total_votes = party.v + can_by;
	auto it = std::lower_bound(
		parties.begin(), parties.end(), total_votes,
		[](const Party& p, uint64_t val) { return p.v < val; }
	);
	if (it == parties.end()) {
		return true;
	}
	int index_to_by = std::distance(parties.begin(), it);
	uint64_t need_to_by = pref_sums.back() - pref_sums[index_to_by - 1] - std::distance(it, parties.end()) * (total_votes - 1);
	if (need_to_by <= can_by) {
		return true;
	}
	return false;
}

struct Check {
 	bool operator()(int amount, int n, vector<Party>& parties, vector<uint64_t>& pref_sums) const {
		for (int i : rng::iota_view{ 0, n }) {
			auto& party = parties[i];
			if (party.p == -1) {
				continue;
			}
			if (CanPartyWin(amount, i, n, parties, pref_sums)) {
				return true;
			}
		}
		return false;
 	}
};

auto Read(std::istream& in) {
	int n; in >> n;
	vector<Party> parties(n);
	for (int i : rng::iota_view{ 0, n }) {
		in >> parties[i].v >> parties[i].p;
		parties[i].i = i;
	}
	return std::tuple{ n, parties };
}

void PrintAns(std::ostream& out, int min_amount, int src_i, vector<Party>& parties) {
	out << min_amount << endl;
	out << src_i + 1 << endl;
	for (auto& p : parties) {
		out << p.v << ' ';
	}
	out << endl;
}

int main() {
	auto [n, parties] = Read(std::cin);
	if (n == 1) {
		PrintAns(std::cout, parties.front().p, 0, parties);
		return 0;
	}
	std::sort(parties.begin(), parties.end(), [](const Party& lhs, const Party& rhs) {return lhs.v < rhs.v; });
	vector<uint64_t> pref_sums(n);
	uint64_t total_votes = 0;
	int max_p = 0;
	for (int i : rng::iota_view{ 0, n }) {
		pref_sums[i] = i > 0 ? pref_sums[i - 1] + parties[i].v : parties[i].v;
		total_votes += parties[i].v;
		max_p = std::max(max_p, parties[i].p);
	}
	int min_amount = UpperBound(0, total_votes + max_p, Check{}, n, parties, pref_sums);
	int mem_i = 0;
	int src_i = 0;
	int votes_to_by = 0;
	int target_votes = 0;
	for (int i : rng::iota_view{ 0, n }) {
		auto& party = parties[i];
		if (party.p == -1) {
			continue;
		}
		if (CanPartyWin(min_amount, i, n, parties, pref_sums)) {
			mem_i = i;
			src_i = party.i;
			votes_to_by = min_amount - party.p;
			target_votes = party.v + votes_to_by;
			party.v = target_votes;
			break;
		}
	}
	for (int i : rng::iota_view{ 0, n }) {
		if (i == mem_i) {
			continue;
		}
		auto& party = parties[i];
		if (party.v >= target_votes) {
			votes_to_by -= (party.v - target_votes + 1);
			party.v = target_votes - 1;
		}
	}
	for (int i : rng::iota_view{ 0, n }) {
		if (i == mem_i) {
			continue;
		}
		auto& party = parties[i];
		int delta = std::min(votes_to_by, party.v);
		votes_to_by -= delta;
		party.v -= delta;
		if (votes_to_by <= 0) {
			break;
		}
	}
	std::sort(parties.begin(), parties.end(), [](const Party& lhs, const Party& rhs) {return lhs.i < rhs.i; });
	PrintAns(std::cout, min_amount, src_i, parties);
	return 0;
}