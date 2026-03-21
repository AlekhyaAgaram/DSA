class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        string res = strs[0];

        for(int i = 1; i < n; i++) {
            //if longest prefix not in other strings
            while(strs[i].find(res) != 0) {
                //remove last char of longest string
                res.pop_back();
                //if longest prefix empty
                if(res.empty()){
                    return "";
                }
            }
        }
        return res;
    }
};