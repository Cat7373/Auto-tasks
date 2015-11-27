# coding:utf-8
import os
import time
import shutil
import config
import xlog

name = '自动备份Chrome收藏夹'
run_interval = 60

src_file = 'C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'
dst_folder = os.path.join(config.data_path, name)

def init():
    if not os.path.isdir(dst_folder):
        os.mkdir(dst_folder)

def run():
    dst_file = '%s.save' % time.strftime('%Y-%m-%d')
    dst_file = os.path.join(dst_folder, dst_file)
    if not os.path.exists(dst_file):
        shutil.copy(src_file,  dst_file)
        xlog.info('[%s] 已经备份今天的收藏夹.' % name)

if __name__ == '__main__':
    init()
    run()
