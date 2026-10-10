"""Serve no site/admin source here; use the authenticated canonical origin."""
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlsplit
import os


class Redirect(BaseHTTPRequestHandler):
    def do_GET(self):
        # Fixed destination; never redirect to a hostname supplied by a client.
        path = urlsplit(self.path).path
        if path.startswith('/admin'):
            path = '/admin.html'
        self.send_response(307)
        self.send_header('Location', 'https://ovitar-api.onrender.com/' + path.lstrip('/'))
        self.send_header('Cache-Control', 'no-store')
        self.send_header('Content-Length', '0')
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()

    do_HEAD = do_GET

    def log_message(self, *_):
        pass


if __name__ == '__main__':
    ThreadingHTTPServer(('0.0.0.0',int(os.getenv('PORT','10000'))), Redirect).serve_forever()
