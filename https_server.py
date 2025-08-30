import http.server
import ssl
import sys
import os

PORT = 4443
CERT_FILE = 'cert.pem'
KEY_FILE = 'key.pem'

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Silence logging for cleaner output

if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
    print('Certificate or key not found. Please generate cert.pem and key.pem.')
    sys.exit(1)

httpd = http.server.HTTPServer(('0.0.0.0', PORT), Handler)
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
print(f'Serving HTTPS on port {PORT}...')
httpd.serve_forever()
