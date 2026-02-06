class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> v;

        generate("", 0, 0, n, v);
        return v;
    }
    void generate(string s, int open, int close, int n, vector<string> &v) {
        if(s.size() == 2*n) {
            v.push_back(s);
            return;
        }

        if(open < n) generate(s+'(', open+1, close, n, v);
        if(close < open) generate(s+')', open, close+1, n, v);
    }

};