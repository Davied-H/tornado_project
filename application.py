from urls.url import url  # 引用url.py
import tornado.web
import os
import configparser

cf = configparser.ConfigParser()
cf.read("conf/base.conf")

# 定义项目路径和静态资源路径
setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
)

application = tornado.web.Application(
    handlers=url,
    cookie_secret='7xz4uEubRgm5t7+L6t2gm4juHgYUE0RAmNmeY7d4QKA=',
    login_url='/login',
    debug=True,  # debug模式，修改自动重启
    **setting
)
