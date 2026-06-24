class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = {}
        for i in tasks:
            if i in mp:
                mp[i] += 1
            else:
                mp[i] = 1
        
        """
        max_heap = [-cnt for cnt in mp.values()]
        heapq.heapify(max_heap)

        cooldown = deque()  
        time = 0

        while max_heap or cooldown:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1  # move toward 0

                if count < 0:
                    cooldown.append((time + n , count))

            if cooldown and cooldown[0][0] == time:
                _, cnt = cooldown.popleft()
                heapq.heappush(max_heap, cnt)

        return time
        """
        #GREEDY SOLUTION
        freq=[0]*26
        for x in tasks:
            freq[ord(x)-ord('A')]+=1
        maxi=max(freq)
        c=0
        for i in freq:
            if i==maxi:
                c+=1
        return max(len(tasks),(maxi-1)*(n+1)+c)