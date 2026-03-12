class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }
        int n = s.length();
        
        unordered_map<char,char> mp;
        unordered_map<char,int> lol;

        for(int i=0;i<n;i++){
            if(mp.find(s[i]) == mp.end() and (lol.find(t[i]) == lol.end())){                
                mp[s[i]] = t[i];
                lol[t[i]]++;
            }
            else{
                if(mp[s[i]]!=t[i]){
                    return false;
                }
            }
        }
        return true;
    }
};