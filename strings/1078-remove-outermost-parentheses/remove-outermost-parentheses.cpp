class Solution {
public:
    string removeOuterParentheses(string s) {
        int depth = 0;
        string result = "";
        for(char c : s) {
            if(c == '(') {
                if(depth > 0){
                    result += '(';
                }
                depth++;
            }
            else if(c == ')'){
                depth--;
                if(depth > 0){
                    result += ')';
                }
            }
        }
        return result;
    }
};