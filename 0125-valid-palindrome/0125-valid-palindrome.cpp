#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        int toLower = 32;
        string from_left;
        string from_right;

        for (auto c: s) {
            if (isalnum(c)) {
                if (c >= 'A' && c <= 'Z')
                    c += toLower;
                from_left = from_left + c;
                from_right = c + from_right;
            }
        }
        return from_left == from_right;
    }
};