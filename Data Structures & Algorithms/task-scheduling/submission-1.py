class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task = Counter(tasks)

        current_max = max(task.values())

        max_count = 0
        for i in task.values():
            if i == current_max:
                max_count += 1
            
        ans = (n+1) * (current_max-1) + max_count

        return max(len(tasks), ans)
