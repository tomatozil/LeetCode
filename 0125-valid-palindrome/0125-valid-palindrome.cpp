#include <cctype>

class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> sList;
        for (char c: s) {
            if (isalnum(c))
                sList.push_back(tolower(c));
        }

        int left = 0, right = sList.size()-1;
        while (left < right) {
            if (sList[left] != sList[right])
                return false;
            left++;
            right--;
        }
        return true;
    }
};