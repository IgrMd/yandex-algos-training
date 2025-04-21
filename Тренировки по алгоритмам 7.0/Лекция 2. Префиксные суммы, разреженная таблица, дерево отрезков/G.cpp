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
#include <mutex>
#include <format>
#include <utility>

using namespace std;
namespace rng = ranges;

struct Segment {
	int l{}, r{};
	int len() const {
		return r - l + 1;
	}
};

struct Item {
	Segment seg{};
	int val{};
	int prf{};
	int suf{};
};

class SegmentTree {
public:
	SegmentTree(const vector<int>& arr) {
		int k = 0;
		int pow_of_2 = 1;
		while (pow_of_2 < arr.size()) {
			++k;
			pow_of_2 *= 2;
		}
		this->n = 2 * pow_of_2 - 1;
		this->displacement = pow_of_2 - 1;
		this->arr.resize(this->n);
		for (int i = n - 1; i >= 0; --i) {
			int initial_i = i - displacement;
			if (initial_i >= ssize(arr)) {
				this->arr[i].seg = { initial_i, initial_i };
			} else if (initial_i >= 0) {
				this->arr[i].seg = { initial_i, initial_i };
				if (arr[initial_i] == 0) {
					this->arr[i].val = this->arr[i].prf = this->arr[i].suf = 1;
				}
			} else {
				auto [l_i, r_i] = get_children(i);
				this->arr[i].seg = { this->arr[l_i].seg.l, this->arr[r_i].seg.r };
				update_item(i);
			}
		}
	}

	void update_item(int i, int val) {
		i += displacement;
		arr[i].val = arr[i].prf = arr[i].suf = int(val == 0);
		int parent = get_parent(i);
		while (parent >= 0) {
			update_item(parent);
			parent = get_parent(parent);
		}
	}

	int query(Segment seg) {
		return query_impl(0, seg).val;
	}

private:

	struct Ans{
		int val{};
		int prf{};
		int suf{};
	};
	Ans query_impl(int i, Segment seg){
		Ans ans;
		if (i >= n) {
			return ans;
		}
		auto& me = arr[i];
		if (seg.r < me.seg.l || seg.l > me.seg.r) {
			return ans;
		}
		if (seg.l <= me.seg.l && me.seg.r <= seg.r){
			ans.val = me.val;
			ans.prf = me.prf;
			ans.suf = me.suf;
			return ans;
		}
		auto [l_i, r_i] = get_children(i);
		auto& l_c = arr[l_i];
		auto& r_c = arr[r_i];
		auto l = query_impl(l_i, seg);
		auto r = query_impl(r_i, seg);

		ans.val = std::max(l.val, r.val);
		ans.prf = l_c.seg.len() == l.val ? l.val + r.prf : l.prf;
		ans.suf = r_c.seg.len() == r.val ? r.val + l.suf : r.suf;
		ans.val = std::max({ ans.val, ans.prf, ans.suf, l.suf + r.prf });
		return ans;
	}
	void update_item(int i) {
		auto& me = arr[i];
		auto [l_i, r_i] = get_children(i);
		auto& l_c = arr[l_i];
		auto& r_c = arr[r_i];
		me.val = std::max(l_c.val, r_c.val);
		if (l_c.seg.len() == l_c.val && r_c.seg.len() == r_c.val) {
			me.val = me.prf = me.suf = me.seg.len();
		} else if (l_c.seg.len() == l_c.val) {
			me.prf = l_c.val + r_c.prf;
			me.suf = r_c.suf;
		} else if (r_c.seg.len() == r_c.val) {
			me.suf = r_c.val + l_c.suf;
			me.prf = l_c.prf;
		} else {
			me.prf = l_c.prf;
			me.suf = r_c.suf;
		}
		me.val = std::max({ me.val, me.suf, me.prf, l_c.suf + r_c.prf });
	}
	pair<int, int> get_children(int i) {
		return { 2 * i + 1, 2 * i + 2 };
	}
	int get_parent(int i) {
		return (i != 0) ? (i - 1) / 2 : -1;
	}
	vector<Item> arr;
	int n{};
	int displacement{};
};

int main() {
	int n, m;
	cin >> n;
	vector<int> arr(n);
	for (int i = 0; i < n; ++i) {
		cin >> arr[i];
	}
	cin >> m;
	std::string cmd;
	int a, b;
	SegmentTree tree(arr);
	while (m--) {
		cin >> cmd;
		cin >> a >> b;
		if (cmd[0] == 'Q') {
			cout << tree.query({ a - 1, b - 1 }) << '\n';
		} else {
			tree.update_item(a - 1, b);
		}
	}
}