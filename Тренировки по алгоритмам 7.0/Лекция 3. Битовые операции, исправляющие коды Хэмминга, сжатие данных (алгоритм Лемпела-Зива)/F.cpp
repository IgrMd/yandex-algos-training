#include <iostream>
#include <vector>
#include <bitset>
#include <limits>
#include <optional>
#include <cmath>
#include <cstdint>

using namespace std;

const uint64_t EMPTY = numeric_limits<uint64_t>::max();
const int POW = 64;

struct Point {
	int x, y, z;
};

pair<int, vector<Point>> read_input() {
	int n, k;
	cin >> n >> k;
	vector<Point> rooks(k);
	for (int i = 0; i < k; ++i) {
		int x, y, z;
		cin >> x >> y >> z;
		rooks[i] = { x - 1, y - 1, z - 1 };
	}
	return { n, rooks };
}

optional<tuple<int, int, int>> rooks_3d(int n, const vector<Point>& rooks) {
	int chunk_cnt = n / POW;
	uint64_t rest = 0;
	for (int i = 0; i < n % POW; ++i) {
		rest = (rest << 1) | 1;
	}

	vector<vector<bool>> xy(n, vector<bool>(n, true));
	vector<vector<uint64_t>> xz(n, vector<uint64_t>(chunk_cnt, EMPTY));
	vector<vector<uint64_t>> yz(n, vector<uint64_t>(chunk_cnt, EMPTY));

	if (n % POW != 0) {
		for (auto& row : xz) row.push_back(rest);
		for (auto& row : yz) row.push_back(rest);
	}

	for (const auto& p : rooks) {
		xy[p.x][p.y] = false;
		int chunk = p.z / POW;
		int pos = p.z % POW;
		xz[p.x][chunk] &= ~(1ULL << pos);
		yz[p.y][chunk] &= ~(1ULL << pos);
	}

	int chunk_total = chunk_cnt + (n % POW != 0 ? 1 : 0);

	for (int x = 0; x < n; ++x) {
		for (int y = 0; y < n; ++y) {
			if (xy[x][y]) {
				for (int chunk = 0; chunk < chunk_total; ++chunk) {
					if (xz[x][chunk] != 0 && yz[y][chunk] != 0) {
						for (int z = 0; z < POW; ++z) {
							if ((xz[x][chunk] & (1ULL << z)) && (yz[y][chunk] & (1ULL << z))) {
								return make_tuple(x + 1, y + 1, POW * chunk + z + 1);
							}
						}
					}
				}
			}
		}
	}

	return nullopt;
}

int main() {
	auto [n, rooks] = read_input();
	auto ans = rooks_3d(n, rooks);
	if (!ans.has_value()) {
		cout << "YES" << endl;
	} else {
		auto [x, y, z] = ans.value();
		cout << "NO" << endl;
		cout << x << " " << y << " " << z << endl;
	}
	return 0;
}
