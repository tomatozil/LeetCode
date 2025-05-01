class Solution {
public:
    bool isValid(string s) {
        map<char, char> brackets{{'(', ')'}, {'{', '}'}, {'[', ']'}};
        stack<char> stack;

        for (char c: s) {
            if (!brackets.contains(c)) {
                if (stack.empty() || c != brackets[stack.top()]) {
                    return false;
                } else {
                    stack.pop();
                }
            } else {
                stack.push(c);
            }
        }

        return stack.empty();
    }
};