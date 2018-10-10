# -*- coding: utf-8 -*-
import os

from flask import Flask


app = Flask(
    __name__,
    static_folder=os.path.dirname(__file__),
    static_url_path=''
)

def open_web():
    '''调用浏览器打开页面'''
    import webbrowser
    # 标准库 webbrowser 模块的 open_new_tab() 方法可以打开一个页面
    from threading import Thread

    args = ('http://127.0.0.1:5666/main-page.html',)
    # 创建新的线程，不会阻塞主线程
    thread = Thread(target=webbrowser.open_new_tab, args=args)
    # 设置为后台模式
    thread.daemon = True
    # 启动线程
    thread.start()

if __name__ == '__main__':
    open_web() # 打开浏览器
    app.run(port=5666) # 启动完整