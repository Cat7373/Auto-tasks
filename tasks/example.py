# coding:utf-8
import xlog

name = 'example'
run_interval = 1 #Minute

def init():
    xlog.info('[%s] init!' % name)

def run():
    xlog.info('[%s] run!' % name)

if __name__ == '__main__':
    init()
    run()
