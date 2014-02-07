#!/usr/bin/python

import tornado.web
import tornado.websocket
import tornado.ioloop


class Sumatoria(tornado.websocket.WebSocketHandler):

    def open(self):
        print "sumatoria connected"
        self.write_message("sumatoria conected")

    def on_message(self, message):
        sumatoria = int(message) + int(message)
        self.write_message(sumatoria)

    def on_close(self):
        print "Client disconnected sumatoria"


class WebSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print "New client connected"
        self.write_message("You are connected")

    def on_message(self, message):
        message = 'el cuadrado de lo que hiciiste es: %s' % str(
            int(message) * int(message))
        self.write_message(message)

    def on_close(self):
        print "Client disconnected"


application = tornado.web.Application([
    (r"/", WebSocketHandler),
    (r"/sumatoria", Sumatoria),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
