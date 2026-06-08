class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = {}
        for i in range(len(speed)):
            time[position[i]] = (target - position[i])/ speed[i]
        
        position.sort(reverse = True)

        stack = []
        for i in range(len(speed)):
            if not stack:
                stack.append(time[position[i]])
            elif stack and time[position[i]] > stack[-1]:
                stack.append(time[position[i]])
        return len(stack)



        

        





