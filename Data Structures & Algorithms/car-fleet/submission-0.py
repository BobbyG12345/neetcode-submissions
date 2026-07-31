class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - p) / s for p, s in sorted(zip(position, speed), reverse=True)]
        
        stack = []
        for t in times:
            if not stack or t > stack[-1]:
                stack.append(t)
        return len(stack)