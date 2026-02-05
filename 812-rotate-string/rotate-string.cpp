class Solution {
public:
    bool rotateString(string s, string goal) {
        // for(int i = 0; i < s.size(); i++) {
        //     if(s.substr(i) + s.substr(0, i) == goal) return true;
        // }
        // return false;
        if(s.size() != goal.size()) return false;
        
        string ss = s+s;
        return ss.find(goal) != string::npos;
    }
};