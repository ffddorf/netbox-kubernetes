from http.server import HTTPServer, BaseHTTPRequestHandler
from rq import Worker
import threading
import socket

class HealthcheckedRQWorker(Worker):
    def _start_health(self):
        class HealthcheckHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'OK\n')

        class ModernServer(HTTPServer):
            address_family = socket.AF_INET6

        httpd = ModernServer(('::', 8000), HealthcheckHandler)
        httpd.serve_forever()

    def work(self, *args, **kwargs):
        http = threading.Thread(target=self._start_health)
        http.start()

        super().work(*args, **kwargs)
