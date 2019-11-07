from abc import ABC

import tornado.web


class IndexHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("hello")
