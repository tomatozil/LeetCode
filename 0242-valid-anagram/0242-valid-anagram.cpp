class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> use(26, 0);
        for(auto c: s) {use[c-'a']++;}
        for(auto c: t) {use[c-'a']--;}

        for(auto i: use) {
            if (i != 0) 
                return false;
        }
        return true;
    }
};