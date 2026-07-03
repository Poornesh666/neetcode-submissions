class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-c for c in count.values()]
        heapq.heapify(heap) #heap stores frequency
        q = deque() #q stores (rem. freq, ready_time)

        time = 0

        while q or heap:
            time += 1

            if heap:
                freq = heapq.heappop(heap) + 1
                if freq:
                    ready_time = time + n 
                    q.append((freq, ready_time))
            
            if q and q[0][1] == time:
                freq, ready = q.popleft()
                heapq.heappush(heap, freq)

        return time
