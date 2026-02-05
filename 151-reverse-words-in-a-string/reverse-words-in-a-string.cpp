class Solution {
public:
    string reverseWords(string s) {
        string new_s = "", word="";
        int i;

        reverse(s.begin(), s.end());
        
        for(i = 0; i < s.size(); i++) {
            while(i < s.size() && s[i] != ' ') {
                word += s[i];
                i++;
            }

            reverse(word.begin(), word.end());
            if(!word.empty()) {
                new_s += " ";
                new_s += word;
                word = "";
            }
        }
        return new_s.substr(1);
    }
};