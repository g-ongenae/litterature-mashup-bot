from multiprocessing import Process
from src import main
from src.server import run_server


def run_in_parallel(tasks):
    """
    Run tasks in Parallel
    """
    running_tasks = [Process(target=task) for task in tasks]
    for running_task in running_tasks:
        running_task.start()
    for running_task in running_tasks:
        running_task.join()


if __name__ == "__main__":
    run_in_parallel([main, run_server])
