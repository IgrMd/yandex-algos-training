#include <algorithm>
#include <iostream>
#include <ranges>
#include <string>
#include <unordered_map>
#include <vector>
#include <deque>

using namespace std;
namespace rng = std::ranges;
namespace view = rng::views;

class InfArr;
using Graph = vector<vector<int>>;
using Visited = vector<vector<InfArr>>;

int INF = 1'000'000;

struct InfArr {
	int arr[2] = { INF, INF };
	int& operator[] (int index) {
		return arr[index];
	}
	const int& operator[] (int index) const {
		return arr[index];
	}
};

void Dfs(const Graph& graph, vector<bool>& visited, int now) {
	visited[now] = true;
	for (int v : graph[now]) {
		if (!visited[v]) {
			Dfs(graph, visited, v);
		}
	}
}

bool CheckGraph(int N, const Graph& graph, vector<int>& robots) {
	vector<bool> visited(N + 1);
	Dfs(graph, visited, robots[0]);
	for (int v : robots) {
		if (!visited[v]) {
			return false;
		}
	}
	return true;
}

void Bfs(const Graph& graph, vector<InfArr>& visited,int start) {
	deque<pair<int, int>> queue;
	queue.push_back({ start, 0 });
	visited[start][0] = 0;
	while (!queue.empty()) {
		const auto [now, dst] = queue.front();
		queue.pop_front();
		const int distance = dst + 1;
		const int parity = distance % 2;
		for (int v : graph[now]) {
			if (distance < visited[v][parity]) {
				visited[v][parity] = distance;
				queue.push_back({ v, distance });
			}
		}
	}
}

int MyMaxForRoom(const Visited& visited, int room_i, int parity, int M) {
	int max = -INF;
	for (int i : view::iota(0, M)) {
		max = std::max(max, visited[i][room_i][parity]);
	}
	return max;
}

int MyMaxForEdge(const Visited& visited, int v1, int v2, int parity, int M) {
	int max = -INF;
	for (int i : view::iota(0, M)) {
		max = std::max(max, std::min(visited[i][v1][parity], visited[i][v2][parity]));
	}
	return max;
}

int main() {
	size_t N, K, M;
	cin >> N >> K;
	Graph graph(N + 1);
	vector<pair<int, int>> edges;
	for (auto i : view::iota(0, int(K))) {
		int v1, v2;
		cin >> v1 >> v2;
		graph[v1].push_back(v2);
		graph[v2].push_back(v1);
		edges.push_back({ v1, v2 });
	}
	cin >> M;
	if (M == 1) {
		cout << 0;
		return 0;
	}
	vector<int> robots(M);
	for (auto i : view::iota(0, int(M))) {
		cin >> robots[i];
	}
	if (!CheckGraph(N, graph, robots)) {
		cout << -1;
		return 0;
	}
	Visited visited(M, vector<InfArr>{N + 1});
	for (auto i : view::iota(0, int(M))) {
		Bfs(graph, visited[i], robots[i]);
	}
	double max_path = INF;
	for (int room_i : view::iota(1, int(N + 1))) {
		double max_even_path = MyMaxForRoom(visited, room_i, 0, M);
		double max_odd_path = MyMaxForRoom(visited, room_i, 1, M);
		max_path = std::min({max_path, max_even_path, max_odd_path});
	}

	for (const auto [v1, v2] : edges) {
		double max_even_edge = MyMaxForEdge(visited, v1, v2, 0, M);
		double max_odd_edge = MyMaxForEdge(visited, v1, v2, 1, M);
		max_path = std::min(max_path, std::min(max_even_edge, max_odd_edge) + 0.5);
	}
	if (max_path / 10 > .0) {
		cout << max_path;
	} else {
		cout << int(max_path);
	}
}
