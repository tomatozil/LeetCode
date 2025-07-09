class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        map<string, vector<string>> patterns;
        for(int i = 0; i < wordList.size(); i++) {
            string word = wordList[i];
            for (int j = 0; j < word.size(); j++) {
                string pattern = makePattern(word, j);
                patterns[pattern].push_back(word);
            }
        }

        deque<pair<string, int>> q;
        q.emplace_back(beginWord, 1);
        unordered_set<string> visited;
        visited.insert(beginWord);
        
        while (!q.empty()) {
            auto [cur, dist] = q.front(); q.pop_front();
            for (int j = 0; j < cur.size(); j++) {
                string p = makePattern(cur, j);
                auto& samePatternWords = patterns[p];
                for (auto& w: samePatternWords) {
                    if (w == endWord) {
                            return dist + 1;
                    } 
                    if (!visited.count(w)) {
                        q.emplace_back(w, dist + 1);
                        visited.insert(w);
                    } 
                }
            }
        }
        return 0;
    }

private:
    string makePattern(const string& word, int idx) {
        string result = word;
        result[idx] = '*';
        return result;
    }
};