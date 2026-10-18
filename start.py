"""Start the local Rime website. Run with Python 3, then keep this window open."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import webbrowser

class RimeHandler(SimpleHTTPRequestHandler):
    extensions_map = {**SimpleHTTPRequestHandler.extensions_map,
                      '.html': 'text/html; charset=utf-8'}

if __name__ == '__main__':
    handler = partial(RimeHandler, directory=str(Path(__file__).resolve().parent))
    with ThreadingHTTPServer(('127.0.0.1', 0), handler) as server:
        address = f'http://127.0.0.1:{server.server_port}/'
        print(f'Rime: {address}\nKeep this window open. Stop with Ctrl+C.')
        webbrowser.open(address)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
