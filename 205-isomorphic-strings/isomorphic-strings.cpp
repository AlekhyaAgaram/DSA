class Solution {
public:
    bool isIsomorphic(string s, string t) {
        if(s.length() != t.length()){
            return false;
        }

        int lastSeenS[256];
        int lastSeenT[256];

        for(int i=0;i<256;i++){
            lastSeenS[i] = -1;
            lastSeenT[i] = -1;
        }

        for(int i = 0; i < s.length(); i++) {
            unsigned char c1 = s[i];
            unsigned char c2 = t[i];

            if(lastSeenS[c1] != lastSeenT[c2])
                return false;

            lastSeenS[c1] = i;
            lastSeenT[c2] = i;
        }

        return true;
    }
};