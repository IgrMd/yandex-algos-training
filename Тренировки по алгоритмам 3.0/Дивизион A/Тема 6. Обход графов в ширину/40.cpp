#include <algorithm>
#include <iostream>
#include <ranges>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <deque>

using namespace std;
namespace rng = std::ranges;
namespace view = rng::views;

using Graph = vector<vector<int>>;
using Visited = vector<int>;


int INF = 1'000'000'000;


void dfs(const Graph& graph, Visited& visited, int now, int component) {
	if (visited[now])
		return;
	visited[now] = component;
	for (int v : graph[now]) {
		if (!visited[v])
			dfs(graph, visited, v, component);
	}
}

void AssignComponents(Graph& graph, const Graph& sub_graph, int n) {
	Visited visited(n + 1);
	int component = graph.size();
	for (int v : view::iota(1, n + 1)) {
		if (!visited[v]) {
			dfs(sub_graph, visited, v, component);
			++component;
		}
	}
	for (int v : view::iota(1, n + 1)) {
		int component = visited[v];
		if (component >= graph.size())
			graph.push_back({});
		graph[component].push_back(v);
		graph[v].push_back(component);
	}
}

int main() {
	int N, K;
	cin >> N >> K;
	Graph graph(N + 1);
	for (auto card : view::iota(0, K)) {
		int r;
		cin >> r;
		Graph sub_graph(N + 1);
		for (auto _ : view::iota(0, r)) {
			int v1, v2;
			cin >> v1 >> v2;
			sub_graph[v1].push_back(v2);
			sub_graph[v2].push_back(v1);
		}
		AssignComponents(graph, sub_graph, N);
	}
	
	Visited visited(graph.size(), INF);
	int distance = 0;
	visited[1] = distance;
	deque<int> queue;
	queue.push_back(1);
	while (!queue.empty()) {
		int now = queue.front();
		queue.pop_front();
		for (int v : graph[now]) {
			int cur_dst = visited[now] + (now > v ? 1 : 0);
			if (cur_dst < visited[v]) {
				visited[v] = cur_dst;
				queue.push_back(v);
			}
		}
		++distance;
	}
	int path = visited[N];
	cout << ((path != INF) ? path : -1);
}
