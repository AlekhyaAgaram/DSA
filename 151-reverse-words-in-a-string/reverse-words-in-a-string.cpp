class Solution {
public:
    string reverseWords(string s) {
        string str;


        //for removing spaces from appropriate places
        for(char c : s){
            if(c!= ' '){
                str += c;
            }
            else if(c == ' ' && !str.empty() && str.back()!=' '){
                str += ' ';
            }
        }

        //remove last char if it is spaces
        if(str.back() == ' '){
            str.pop_back();
        }

        //reverse the string
        reverse(str.begin(), str.end());

        //reverse each word
        int n = str.length();
        for(int i = 0; i < n; i++) {

            if(str[i] == ' ')
                continue;
            int k = i;
            while(k < n && str[k] != ' ')
                k++;
            reverse(str.begin() + i, str.begin() + k);
            i = k;
        }
        return str;

    }
};