class Solution {
public:
    bool isValid(string s) {
        stack<char> paren;
        for(char c : s) {
            if(c == '(' || c == '{' || c == '[') {
                paren.push(c);
            }
            else {
                if(paren.empty()) return false;
                if(c == ')' && paren.top() == '(' || 
                    c == '}' && paren.top() == '{' ||
                    c == ']' && paren.top() == '['
                    ) {
                    paren.pop();
                }
                else {
                    return false;
                }
            }
        }
        return paren.empty();
    }
};