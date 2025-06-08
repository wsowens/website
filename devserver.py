# THIS IS FOR LOCAL TESTING ONLY
# DO NOT USE THIS IN PRODUCTION
#
# YOU'VE BEEN WARNED!

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import argparse

class HTMLHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # If path doesn't end in .html and doesn't contain a dot
        if not self.path.endswith('.html') and '.' not in self.path:
            # if path ends in a '/', try to serve index.html
            if self.path == "":
                self.path = "index.html"
            elif self.path.endswith('/'):
                html_path = os.path.join(self.path, "index.html")
                if os.path.exists(os.path.join(os.getcwd(), html_path)):
                    self.path = html_path
            else:
                # Try to serve path.html
                html_path = f"{path}.html"
                if os.path.exists(os.path.join(os.getcwd(), html_path.lstrip('/'))):
                    self.path = html_path
                else:
                    self.path = '/404.html'
                    if not os.path.exists(os.path.join(os.getcwd(), '404.html')):
                        self.send_error(404, "File not found and no 404.html available")
                        return
        return SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a development server with .html extension handling')
    parser.add_argument('--port', type=int, default=8000, help='Port to run the server on (default: 8080)')
    args = parser.parse_args()
    
    server_address = ('', args.port)
    httpd = HTTPServer(server_address, HTMLHandler)
    print(f"Serving at http://localhost:{args.port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server")
        httpd.server_close()