// #include <map>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        map<string, vector<string>> m;
        for (auto origin: strs) {
            string sorts = origin;
            sort(sorts.begin(), sorts.end());
            if (m.contains(sorts)) {
                m[sorts].push_back(origin);
            } else {
                m[sorts] = {origin};
            }
        }
        for (const auto& pair: m) {
            result.push_back(pair.second);
        }
        return result;
    }
};