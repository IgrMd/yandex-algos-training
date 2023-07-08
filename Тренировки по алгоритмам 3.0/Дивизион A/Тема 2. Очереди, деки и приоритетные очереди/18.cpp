#include <algorithm>
#include <iostream>
#include <ranges>
#include <deque>
#include <queue>
#include <numeric>

using namespace std;
namespace rng = std::ranges;
namespace view = rng::views;

struct Train {
	int arrive;
	int depart;
	int platform;
};

struct Comparator {
	bool operator() (Train t1, Train t2) {
		return t1.depart > t2.depart;
	}
};

int main() {
	int K, N;
	cin >> K >> N;
	vector<int> vtrains_platforms(K);
	iota(vtrains_platforms.begin(), vtrains_platforms.end(), 1);
	priority_queue<int, vector<int>, greater<int>> platforms_queue(
		vtrains_platforms.begin(), vtrains_platforms.end()
	);
	priority_queue<Train, vector<Train>, Comparator> trains_queue;
	vtrains_platforms.resize(N);
	bool fail = false;
	int train_fail_number = 0;
	for (auto i : view::iota(0, N)) {
		int arrive, depart;
		cin >> arrive >> depart;
		if (trains_queue.empty()) {
			trains_queue.emplace(arrive, depart, platforms_queue.top());
			vtrains_platforms[i] = platforms_queue.top();
			platforms_queue.pop();
			continue;
		}
		while (trains_queue.size() && trains_queue.top().depart < arrive) {
			platforms_queue.push(trains_queue.top().platform);
			trains_queue.pop();
		}
		if (trains_queue.size() < K) {
			trains_queue.emplace(arrive, depart, platforms_queue.top());
			vtrains_platforms[i] = platforms_queue.top();
			platforms_queue.pop();
			continue;
		} else {
			fail = true;
			train_fail_number = i + 1;
			break;
		}
	}
	if (fail) {
		cout << 0 << ' ' << train_fail_number;
	} else {
		for (int i : vtrains_platforms) {
			cout << i << '\n';
		}
	}
}

