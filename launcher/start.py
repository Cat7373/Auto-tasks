# coding:utf-8
import os, sys
import time
import threading
import config
import xlog

def init():
    if config.no_console and os.name == 'nt':
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        del ctypes

    data_path = config.data_path
    if not os.path.isdir(data_path):
        os.mkdir(data_path)

def load_tasks():
    tasks = []
    intervals = []

    import imp
    tasks_path = config.tasks_path
    for fileName in os.listdir(tasks_path):
        if fileName.lower().endswith('.py'):
            xlog.info('start load %s' % fileName)
            try:
                with open(os.path.join(tasks_path, fileName), 'rb') as fpy:
                    task = imp.load_source('Auto-tasks_%d_%s' % (len(tasks), fileName), tasks_path, fpy)

                    name = task.name
                    interval = task.run_interval

                    task.init()

                    tasks.append(task)
                    intervals.append(interval)

                    xlog.info('load task %s success.' % name)
            except:
                xlog.warn('load %s fail.' % fileName)
    del imp

    return (tasks, intervals)

def run_tasks(tasks, intervals):
    countdown = []
    for interval in intervals:
        countdown.append(0)

    while True:
        for i in range(len(tasks)):
            if countdown[i] is 0:
                countdown[i] = intervals[i]

                task = tasks[i]
                try:
                    xlog.info('run task %s.' % task.name)
                    process = threading.Thread(target=task.run)
                    process.setDaemon(True)
                    process.start()
                except:
                    xlog.warn('run task %s fail.' % task.name)
            else:
                countdown[i] = countdown[i] - 1

        time.sleep(60)

def main():
    xlog.info('=====start=====')
    init()
    (tasks, intervals) = load_tasks()
    run_tasks(tasks, intervals)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt: # Ctrl + C on console
        sys.exit(0)
