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

using namespace std;

template <typename Cmp, typename... Args>
int UpperBound(int l, int r, Cmp cmp, Args... args) {
	while (l < r) {
		int mid = (l + r) / 2;
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
	int i, j;
};

int SubSum(Point p1, Point p2, vector<vector<int>>& pref_sums) {
	int sum1 = pref_sums[p2.i][p2.j];
	int sum2 = p1.j > 0 ? pref_sums[p2.i][p1.j - 1] : 0;
	int sum3 = p1.i > 0 ? pref_sums[p1.i - 1][p2.j] : 0;
	int sum4 = p1.i > 0 && p1.j > 0 ? pref_sums[p1.i - 1][p1.j - 1] : 0;
	return sum1 - sum2 - sum3 + sum4;
}
struct CheckPlus {
	bool operator()(int k, int n, int m, vector<vector<int>>& pref_sums) const {
		if ((3 * k > n) || (3 * k > m)) {
			return false;
		}
		for (int i : ranges::iota_view{ 0, n - 3 * k + 1 }) {
			for (int j : ranges::iota_view{ 0, m - 3 * k + 1 }) {
				int sum1 = SubSum({ i, j + k }, { i + 3 * k - 1, j + 2 * k - 1 }, pref_sums);
				int sum2 = SubSum({ i + k, j }, { i + 2 * k - 1, j + 3 * k - 1 }, pref_sums);
				if (sum1 == sum2 && sum2 == 3 * k * k) {
					return true;
				}
			}
		}
		return false;
	}
};

int main() {
	int n, m;
	cin >> n >> m;
	vector<string> field(n);
	for (auto& row : field) {
		cin >> row;
	}
	vector<vector<int>> pref_sums(n, vector<int>(m));
	for (int i : ranges::iota_view{ 0, n }) {
		for (int j : ranges::iota_view{ 0, m }) {
			int sum1 = i > 0 ? pref_sums[i - 1][j] : 0;
			int sum2 = j > 0 ? pref_sums[i][j - 1] : 0;
			int sum3 = i > 0 && j > 0 ? pref_sums[i - 1][j - 1] : 0;
			pref_sums[i][j] = sum1 + sum2 - sum3 + (field[i][j] == '#');
		}
	}
	cout << LowerBound(1, std::min(n, m) - 1, CheckPlus{}, n, m, pref_sums) << endl;
}