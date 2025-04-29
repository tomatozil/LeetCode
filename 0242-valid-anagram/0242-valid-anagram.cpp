class Solution {
public:
    bool isAnagram(string s, string t) {
        string s_copy = s;
        string t_copy = t;
        sort(s_copy.begin(), s_copy.end());
        sort(t_copy.begin(), t_copy.end());

        if (s_copy == t_copy)
            return true;
        return false;
    }
};