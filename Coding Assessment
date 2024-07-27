from collections import defaultdict, deque

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration
        self.dependencies = []
        self.earliest_start_time = 0
        self.earliest_finish_time = 0
        self.latest_start_time = float('inf')
        self.latest_finish_time = float('inf')

def add_dependency(tasks, task_name, dependency_name):
    tasks[task_name].dependencies.append(dependency_name)

def calculate_earliest_finish_time(tasks, start_task):
    queue = deque([start_task])
    while queue:
        current_task = queue.popleft()
        current_duration = tasks[current_task].duration
        for dependent in tasks:
            if current_task in tasks[dependent].dependencies:
                tasks[dependent].earliest_start_time = max(tasks[dependent].earliest_start_time, tasks[current_task].earliest_finish_time)
                tasks[dependent].earliest_finish_time = tasks[dependent].earliest_start_time + tasks[dependent].duration
                queue.append(dependent)

def calculate_latest_finish_time(tasks, end_task):
    tasks[end_task].latest_finish_time = tasks[end_task].earliest_finish_time
    tasks[end_task].latest_start_time = tasks[end_task].latest_finish_time - tasks[end_task].duration
    queue = deque([end_task])
    while queue:
        current_task = queue.popleft()
        for task in tasks:
            if current_task in tasks[task].dependencies:
                tasks[task].latest_finish_time = min(tasks[task].latest_finish_time, tasks[current_task].latest_start_time)
                tasks[task].latest_start_time = tasks[task].latest_finish_time - tasks[task].duration
                queue.append(task)

def main():
    tasks = {
        'A': Task('A', 3),
        'B': Task('B', 2),
        'C': Task('C', 4),
        'D': Task('D', 1),
        'E': Task('E', 2)
    }

    add_dependency(tasks, 'A', 'B')
    add_dependency(tasks, 'A', 'C')
    add_dependency(tasks, 'B', 'D')
    add_dependency(tasks, 'C', 'D')
    add_dependency(tasks, 'D', 'E')

    calculate_earliest_finish_time(tasks, 'A')
    calculate_latest_finish_time(tasks, 'E')

    earliest_completion_time = max(task.earliest_finish_time for task in tasks.values())
    latest_completion_time = min(task.latest_finish_time for task in tasks.values() if task.latest_finish_time != float('inf'))

    print(f"Earliest completion time: {earliest_completion_time}")
    print(f"Latest completion time: {latest_completion_time}")

if __name__ == "__main__":
    main()
