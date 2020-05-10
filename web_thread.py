from core.db_image import Image
from PyQt5.QtCore import QThread, pyqtSignal
from gevent.pywsgi import WSGIServer
from core.webapp import app

class WebThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, dst):
        super(WebThread, self).__init__()
        self.dst = dst

    def run(self):
        http_server = WSGIServer(('', 5000), app)
        http_server.serve_forever()
        self.signal.emit("WebThread start")
