#include <algorithm>
#include <cassert>
#include <iostream>
#include <ranges>
#include <deque>
#include <queue>
#include <numeric>
#include <unordered_set>

using namespace std;
namespace rng = std::ranges;
namespace view = rng::views;


int main() {
	int N;
	cin >> N;
	vector<int> cubes;
	int i = 1;
	while (i * i * i <= N) {
		cubes.push_back(i * i * i);
		++i;
	}
	vector<int> dp(N + 1);
	dp[0] = 0;
	dp[1] = 1;
	for (int num : view::iota(2, N + 1)) {
		int min_cube_count = dp[num - 1] + 1;
		for (int cube : cubes) {
			if (num - cube < 0)
				break;
			if (dp[num - cube] + 1 < min_cube_count)
				min_cube_count = dp[num - cube] + 1;
			dp[num] = min_cube_count;
		}
	}
	cout << dp[N];
}

