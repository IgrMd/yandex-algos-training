#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <stack>


void Print(std::vector<int>& sequence) {
	for (auto c : sequence)
		std::cout << c << ' ';
	std::cout << '\n';
}

int DIST = 0;
std::vector<int> SLICES;

void calc_splice(int n, std::vector<std::vector<int>>& graph, std::vector<int>& visited) {
	int sum_dist = 0;
	for (int i = 0; i < n; ++i) {
		if (visited[i] == 2)
			continue;
		for (int j = 0; j < n; ++j) {
			if (visited[j] == visited[i])
				continue;
			sum_dist += graph[i][j];
		}

	}
	if (sum_dist > DIST) {
		DIST = sum_dist;
		SLICES = visited;
	}
}

void calc_max_splice(int curr_v, int n, std::vector<std::vector<int>>& graph,
	std::vector<int>& visited) {

	if (curr_v == n)
		return calc_splice(n, graph, visited);
	visited[curr_v] = 2;
	calc_max_splice(curr_v + 1, n, graph, visited);
	visited[curr_v] = 1;
	calc_max_splice(curr_v + 1, n, graph, visited);
}

int main() {
	using namespace std;
	int n;
	cin >> n;
	std::vector<std::vector<int>> graph(n, std::vector<int>(n, 0));
	for (auto& row : graph) {
		for (auto& elem : row)  {
			cin >> elem;
		}
	}
	std::vector<int> visited(n, 0);
	calc_max_splice(0, n, graph, visited);
	cout << DIST << '\n';
	Print(SLICES);
	return 0;
}

