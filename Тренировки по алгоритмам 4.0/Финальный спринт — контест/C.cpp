#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <set>
#include <queue>
#include <climits>

int MAX_TIME = 24 * 60;
int TRUCK_WEIGHT = 3 * (1'000'000);

struct Road{
	int i, t, w;
	Road(int i, int t, int w)
	: i(i), t(t), w(w){}
};


int main() {
	using namespace std;
	int n, m;
	cin >> n >> m;
	std::vector<vector<Road>> graph;
	graph.resize(n + 1);
	std::set<int> weights;
	for (int _ = 0; _ < m; ++_) {
		int a, b, t, w;
		cin >> a >> b >> t >> w;
		graph[a].emplace_back(b, t, w);
		graph[b].emplace_back(a, t, w);
		weights.insert(w);
	}

	if (n == 1) {
		cout << 10'000'000 << '\n';
		return 0;
	}
	int answer = TRUCK_WEIGHT;
	for (int max_road_weight : weights) {
		vector<bool> visited(n + 1, false);
		vector<int> time(n + 1, INT_MAX);
		time[1] = 0;
		using elem = pair<int, int>;
		priority_queue<elem, deque<elem>, greater<elem>> heap;
		heap.push({0, 1});
		while (!heap.empty()) {
			auto [now_time, now] = heap.top();
			heap.pop();
			if (visited[now])
				continue;
			visited[now] = true;
			for (auto road : graph[now]) {
				if (road.w < max_road_weight)
					continue;
				if (now_time + road.t < time[road.i]) {
					time[road.i] = now_time + road.t;
					heap.push({ time[road.i], road.i });
				}
			}
			if (time[n] <= MAX_TIME) {
				answer = std::max(max_road_weight, answer);
				break;
			}
		}
	}
	cout << (answer - TRUCK_WEIGHT) / 100 << '\n';

	return 0;
}

