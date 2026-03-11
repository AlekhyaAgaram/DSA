class Solution {
public:
    string largestOddNumber(string num) {
        int n = num.length();

        for(int i = n - 1; i >= 0; i--){
            // check if digit is odd
            if((num[i] - '0') % 2 == 1){
                // return substring from start to i
                return num.substr(0, i + 1);
            }
            else{
                continue;
            }
        }

        return "";        
    }
};