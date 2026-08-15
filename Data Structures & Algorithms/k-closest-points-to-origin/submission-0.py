class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for point in points:
            x = point[0]
            y = point[1]

            distance = x * x + y * y

            dist.append((distance, point))

        dist.sort()

        return [point for distance, point in dist[:k]]