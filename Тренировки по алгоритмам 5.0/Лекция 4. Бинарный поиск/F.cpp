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
	int x{};
	int y{};
	bool operator==(const Point&) const = default;
	auto operator<=>(const Point&) const = default;
};

struct MinMax {
	int min{};
	int max{};
};

struct PointYCmp {
	bool operator()(const Point& lhs, const Point& rhs) const {
		return std::tie(lhs.y, lhs.x) < std::tie(rhs.y, rhs.x);
	}
};

struct Check2 {
	bool operator()(int w, vector<Point>& points, vector<MinMax>& prefixes, vector<MinMax>& suffixes) const {
		int j = 0;
		for (int i : ranges::iota_view{ 0, ssize(points) }) {
			while (j < points.size() && (points[j].x - points[i].x + 1 <= w)) {
				j++;
			}
			int y_min, y_max;
			if (i == 0) {
				y_min = suffixes[j].min;
				y_max = suffixes[j].max;
			} else if (j >= points.size()) {
				y_min = prefixes[i - 1].min;
				y_max = prefixes[i - 1].max;
			} else {
				y_min = std::min(prefixes[i - 1].min, suffixes[j].min);
				y_max = std::max(prefixes[i - 1].max, suffixes[j].max);
			}
			if (y_max - y_min + 1 <= w) {
				return true;
			}
		}
		return false;
	}
};


int main() {
	int w, h, n;
	cin >> w >> h >> n;
	vector<Point> points(n);
	int min_x = w, max_x = 0;
	for (int i : ranges::iota_view{ 0, n }) {
		cin >> points[i].x >> points[i].y;
	}
	std::sort(points.begin(), points.end());
	vector<MinMax> prefixes(n);
	vector<MinMax> suffixes(n);
	prefixes.front().min = prefixes.front().max = points.front().y;
	suffixes.back().min = suffixes.back().max = points.back().y;
	for (int i : ranges::iota_view{ 1, n }) {
		prefixes[i].min = std::min(prefixes[i - 1].min, points[i].y);
		prefixes[i].max = std::max(prefixes[i - 1].max, points[i].y);
	}
	for (int i = n - 2; i >= 0; --i) {
		suffixes[i].min = std::min(suffixes[i + 1].min, points[i].y);
		suffixes[i].max = std::max(suffixes[i + 1].max, points[i].y);
	}
	int ans = UpperBound(1, std::min(w, h), Check2{}, points, prefixes, suffixes);
	cout << ans << endl;
}