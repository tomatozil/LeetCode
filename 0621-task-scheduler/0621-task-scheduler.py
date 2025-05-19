class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0 for _ in range(26)]
        for t in tasks:
            freq[ord(t) - ord('A')] += 1
        
        freq.sort()
        most_freq = freq[25] - 1
        idle_count = most_freq * n

        for i in range(24, -1, -1):
            idle_count -= min(most_freq, freq[i])

        if idle_count > 0:
            return len(tasks) + idle_count
        else:
            return len(tasks)