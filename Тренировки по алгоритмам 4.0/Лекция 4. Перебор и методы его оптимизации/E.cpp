#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <stack>


bool IsCorrectSequence(std::vector<char>& sequence, int begin, int end) {
	static const std::unordered_map<char, char> brace_map = { {')', '('}, {']', '['} };
	std::stack<char> stack;
	for (int i = begin; i < end; ++i) {
		char brace = sequence[i];
		if (brace == '(' || brace == '[') {
			stack.push(brace);
			continue;
		}
		if (stack.empty()) {
			return false;
		}
		if (stack.top() != brace_map.at(brace)) {
			return false;
		}
		stack.pop();
	}
	if (!stack.empty()) {
		return false;
	}
	return true;
}

void Print(std::vector<char>& sequence) {
	for (auto c : sequence)
		std::cout << c;
	std::cout << '\n';
}

void Generate(std::vector<char>& sequence, int n, int t, int op1, int cl1, int op2, int cl2) {
	if ((op1 + op2) > n / 2)
		return;
	if (cl1 > op1 || cl2 > op2)
		return;
	if (cl1 == op1 and cl2 == op2)
		if (!IsCorrectSequence(sequence, 0, t))
			return;
	if (t == n) {
		if (IsCorrectSequence(sequence, 0, t)) {
			Print(sequence);
		}
		return;
	}
	sequence[t] = '(';
	Generate(sequence, n, t + 1, op1 + 1, cl1, op2, cl2);
	sequence[t] = '[';
	Generate(sequence, n, t + 1, op1, cl1, op2 + 1, cl2);
	sequence[t] = ')';
	Generate(sequence, n, t + 1, op1, cl1 + 1, op2, cl2);
	sequence[t] = ']';
	Generate(sequence, n, t + 1, op1, cl1, op2, cl2 + 1);
}

int main() {
	using namespace std;
	int n;
	cin >> n;
	if (n % 2) {
		return 0;
	}
	std::vector<char> sequence;
	sequence.resize(n);
	Generate(sequence, n, 0, 0, 0, 0, 0);

}

