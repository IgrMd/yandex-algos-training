#include <algorithm>
#include <cassert>
#include <iostream>
#include <ranges>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;
namespace rng = std::ranges;
namespace view = rng::views;
using namespace std;

void Dfs(vector<vector<int>>& graph, vector<int>& visited, int now, int comp_num) {
	if (visited[now]) {
		return;
	}
	visited[now] = comp_num;
	for (int v : graph[now]) {
		if (!visited[v]) {
			Dfs(graph, visited, v, comp_num);
		}
	}
}

unordered_map<int, vector<int>> Components(int N, vector<vector<int>>& graph) {
	vector<int> visited(N + 1);
	int comp_num = 0;
	for (int v : view::iota(1, N + 1)) {
		Dfs(graph, visited, v, ++comp_num);
	}
	unordered_map<int, vector<int>> answer;
	for (int i : view::iota(1, N + 1)) {
		answer[visited[i]].push_back(i);
	}
	return answer;
}

int main() {
	int N, M;
	cin >> N >> M;
	vector<vector<int>> graph(N + 1);
	for (auto i : view::iota(0, M)) {
		int v1, v2;
		cin >> v1 >> v2;
		graph[v1].push_back(v2);
		graph[v2].push_back(v1);
	}
	auto answer = Components(N, graph);
	cout << answer.size() << '\n';
	for (const auto& [i, component] : answer) {
		cout << component.size() << '\n';
		for (int v : component) {
			cout << v << ' ';
		}
		cout << '\n';
	}
}
