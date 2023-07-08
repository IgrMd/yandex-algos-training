#include <algorithm>
#include <iostream>
#include <ranges>
#include <vector>
#include <set>

using namespace std;
namespace rng = std::ranges;
namespace view = rng::views;
int main()
{
    int n, k;
    cin >> n >> k;
    vector<int> numbers;
    numbers.resize(n);
	for (auto i : view::iota(0, n)) {
		cin >> numbers[i];
	}
    multiset<int> window(numbers.begin(), numbers.begin() + k);
    for (int i = 0, j = i + k; j < n; ++i, ++j) {
        cout << *window.begin() << '\n';
        window.erase(window.find(numbers[i]));
        window.insert(numbers[j]);
    }
	cout << *window.begin();
}

