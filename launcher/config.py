# coding:utf-8
import os, sys

launcher_path = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.join(launcher_path, os.pardir))
data_path = os.path.join(root_path, 'data')
tasks_path = os.path.join(root_path, 'tasks')
no_console = False

if len(sys.argv) >= 2:
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '--noconsole':
            no_console = True
