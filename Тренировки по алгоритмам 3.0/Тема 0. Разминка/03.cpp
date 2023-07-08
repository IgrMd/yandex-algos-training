#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_set>
#include <utility>

using namespace std;

int stickers_count(const vector<int>& diego, int k) {
	auto it = lower_bound(diego.begin(), diego.end(), k);
	if (it == diego.end()) {
		return diego.size();
	}
	if (it == diego.begin()) {
		return *it < k ? 1 : 0;
	}
	return distance(diego.begin(), it);
}

int main()
{
	int n = 0;
	cin >> n;
	vector<int> diego_raw;
	diego_raw.resize(n);
	for (int i = 0; i < n; ++i) {
		cin >> diego_raw[i];
	}
	int k = 0;
	cin >> k;
	vector<int> collectors;
	collectors.resize(k);
	for (int i = 0; i < k; ++i) {
		cin >> collectors[i];
	}
	unordered_set<int> diego_set(diego_raw.begin(), diego_raw.end());
	vector<int> diego(diego_set.begin(), diego_set.end());
	sort(diego.begin(), diego.end());
	for (int k : collectors) {
		cout << stickers_count(diego, k) << '\n';
	}
}
