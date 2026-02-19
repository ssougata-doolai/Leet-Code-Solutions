class Solution {
public:
    bool isValid(string s) {
        int counter1 = 0, counter2 = 0, counter3 = 0;
        stack<char> st;

        for(char c : s) {
            if(c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else {
                if(st.empty()) return false;
                
                char top = st.top();
                st.pop();
                if((c == ')' && top != '(') ||
                   (c == '}' && top != '{') ||
                   (c == ']' && top != '[')
                ) return false;
            }
        }

        return st.empty();
    }
};