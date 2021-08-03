import http.server
import ssl


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        http.server.SimpleHTTPRequestHandler.end_headers(self)


http.server.SimpleHTTPRequestHandler.extensions_map['.wasm'] = 'application/wasm'
httpd = http.server.HTTPServer(('192.168.1.147', 9999), MyHttpRequestHandler)
# httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server.pem', server_side=True)


httpd.serve_forever()

