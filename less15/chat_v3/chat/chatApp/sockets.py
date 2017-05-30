import sockjs.tornado


class SocketHandler(sockjs.tornado.SockJSConnection):
    def on_open(self):
        pass

    def on_message(self):
        pass

    def on_close(self):
        pass
