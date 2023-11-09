#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

static constexpr uint64_t X = 257;
static constexpr uint64_t P = 1'000'000'007;

bool IsEqual(int slen, int from1, int from2,
	const std::vector<uint64_t>& h, const std::vector<uint64_t>& x) {
	if (slen == 0) {
		return true;
	}
	return
		(h[from1 + slen - 1] + h[from2 - 1] * x[slen]) % P ==
		(h[from2 + slen - 1] + h[from1 - 1] * x[slen]) % P;
}

template<typename It>
void Print(It it, It end) {
	for (;it != end; ++it) {
		std::cout << *it << ' ';
	}
	std::cout << std::endl;
}

template<typename Check, typename...Args>
int UpperBound(int left, int right, const Check& check, const Args&...args) {
	while (left < right) {
		int mid = (left + right + 1) / 2;
		if (check(mid, args...)) {
			left = mid;
		} else {
			right = mid - 1;
		}
	}
	return left;
}

int main() {
	using namespace std::literals;
	std::string s;
	std::cin >> s;
	int n = s.size();
	s = " "s.append(std::move(s));
	std::vector<uint64_t> h(n + 1, 0);
	std::vector<uint64_t> x(n + 1, 1);
	for (int i = 1; i < n + 1; ++i) {
		h[i] = (h[i - 1] * X + s[i]) % P;
		x[i] = (x[i - 1] * X) % P;
	}
	std::vector<int> z(n + 1, 0);
	std::function<bool(int, int, int, const std::vector<uint64_t>&, const std::vector<uint64_t>&)> check(IsEqual);
	for (int i = 2; i < n + 1; ++i) {
		if (s[i] == s[1]) {
			z[i] = UpperBound(1, n - i + 1, check, 1, i, h, x);
		}
	}
	Print(std::next(z.begin()), z.end());
}
