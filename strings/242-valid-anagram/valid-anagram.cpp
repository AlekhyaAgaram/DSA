class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if(s.length()!=t.length()){
            return false;
        }

        vector <int> s1(256);
        vector <int> t1(256);
        
        for(char c:s){
            s1[c]++;
        }
        for(char c:t){
            t1[c]++;
        }
        
        if(s1 == t1){
            return true;
        }
        else{
            return false;
        }
    }
};