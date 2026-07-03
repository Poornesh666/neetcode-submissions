class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        x = max(count.values())

        s = sum(v == x for v in count.values())

        return max(len(tasks), (x-1)*(n+1) + s)