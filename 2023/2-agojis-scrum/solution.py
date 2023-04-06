import heapq

def main():
    q = int(input())
    operations = [input().split() for i in range(q)]
    backlog = []
    added_task = set()
    total_value = 0
    for op in operations:
        if op[0] == '+':
            task_id, value = op[1:]
            heapq.heappush(backlog, (-int(value), task_id))
            added_task.add(task_id)
        elif op[0] == '-':
            task_id = op[1]
            if task_id in added_task:
                added_task.remove(op[1])
        else:
            n = int(op[1])
            while n > 0 and backlog:
                value, task_id = heapq.heappop(backlog)
                if task_id in added_task:
                    n -= 1
                    total_value -= value
                    added_task.remove(task_id)
    return total_value

if __name__ == '__main__':
    print(main())
