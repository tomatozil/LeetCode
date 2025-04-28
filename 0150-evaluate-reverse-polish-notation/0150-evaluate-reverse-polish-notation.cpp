#include <algorithm>

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> st;
        for (auto s: tokens) {
            if (isOperation(s)) {
                int n1 = st.top();
                st.pop();
                int n2 = st.top();
                st.pop();
                int ret = calculate(n2, n1, s[0]);
                st.push(ret);
            } else {
                st.push(stoi(s));
            }
        }

        return st.top();
    }

    bool isOperation(string s) {
        if (s.size() != 1) return false;
        array<char, 4> operations{{'+', '-', '*', '/'}};
        
        auto ptr = find(operations.begin(), operations.end(), s[0]);
        return ptr != operations.end();
    }

    int calculate(int n1, int n2, char op) {
        if (op == '+') {
            return n1+n2;
        } else if (op == '-') {
            return n1-n2;
        } else if (op == '*') {
            return n1*n2;
        } else {
            return (int)(n1/n2);
        }
    }
};