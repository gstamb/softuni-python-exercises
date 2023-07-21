from datetime import datetime, timedelta
from collections import deque


def create_work_queue(work_queue):
    while True:
        instructions = input()
        if instructions == "End":
            break

        work_queue.append(instructions)


def create_robot_queue(robots, robot_queue):
    for robot in robots:
        name, time = robot.split("-")
        robot_queue.append(f"00:00:00 {name} {time}")


def check_free_robot(robots, time):
    """Finds the robot who can take the next task from the queue"""
    for robot in robots:
        end_time = robot.split()[0]
        if time >= datetime.strptime(end_time, "%H:%M:%S"):
            return robot


def main():
    robots = input().split(";")
    time_string = input()
    current_time = datetime.strptime(time_string, "%H:%M:%S")

    work_queue = deque()
    robot_queue = deque()
    create_robot_queue(robots, robot_queue)
    create_work_queue(work_queue)

    while work_queue:
        current_time += timedelta(seconds=1)
        task = work_queue.popleft()

        available_robot = check_free_robot(robot_queue, current_time)
        # rotate the queue if available robot whenever that robot is not next in line
        while available_robot != robot_queue[0] and available_robot is not None:
            robot_queue.rotate(-1)

        # use whichever robot next in line to take the task or move it back to the end of queue
        robot = robot_queue.popleft()
        end_time, name, duration = robot.split()

        if current_time >= datetime.strptime(end_time, "%H:%M:%S"):
            end_job = current_time + timedelta(seconds=int(duration))
            robot_queue.append(f"{end_job.strftime('%H:%M:%S')} {name} {duration}")
            print(f"{name} - {task} [{current_time.strftime('%H:%M:%S')}]")
        else:
            robot_queue.append(robot)
            work_queue.append(task)


if __name__ == "__main__":
    main()
