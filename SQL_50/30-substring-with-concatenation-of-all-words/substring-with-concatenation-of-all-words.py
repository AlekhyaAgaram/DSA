class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        mp = {}
        seen = {}
        res = []
        n = len(words[0])
        for i in words:
            mp[i] = mp.get(i,0)+1
        
        r = 0

        while r < n:
            seen = {}
            l = r
            count = 0
            for i in range(r,len(s)-n+1,n):                
                temp = s[i:i+n]
                
                if temp in mp: 
                    seen[temp] = seen.get(temp, 0) + 1
                    count += 1   
                    while seen[temp] > mp[temp]:
                        left_word = s[l:l+n]
                        seen[left_word] = seen.get(left_word, 0) - 1
                        l = l+n
                        count -= 1
                else:
                    seen = {}
                    l = i+n
                    count = 0

                if(count == len(words)):
                    res.append(l)
            r += 1
        return res
            

       

            
