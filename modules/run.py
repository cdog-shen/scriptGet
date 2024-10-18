from http.server import SimpleHTTPRequestHandler, HTTPServer
from functools import partial
from public_import import *


def file_tree(startpath) -> bytes:
    tree_str = "Running tree in script dir:\n"
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * level
        tree_str += f"{indent}{os.path.basename(root)}/\n"
        subindent = " " * 4 * (level + 1)
        for file in files:
            tree_str += f"{subindent}{file}\n"
    return tree_str.encode()


class SGHandler(SimpleHTTPRequestHandler):

    def do_GET(self) -> None:
        """
        route hint:
            /       ->      home info page
            /ls     ->      script file tree
            /<file> ->      get script
        """
        if self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(
                rb"welcome to scriptGet, request to '/ls' to check script file tree :)"
            )
        elif self.path == "/ls":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(file_tree("script"))
        else:
            super().do_GET()  # 其他请求就用默认的处理方式


def gen_serviceHandler(httpHandler=SGHandler, dir="docs"):
    return partial(httpHandler, directory=dir)


if __name__ == "__main__":
    print("run module test...")
    try:
        import threading

        serviceHandler = partial(SGHandler, directory="docs")
        server = HTTPServer(("0.0.0.0", 60000), serviceHandler)
        testThread = threading.Thread(target=server.serve_forever)
        testThread.start()
    except Exception as E:
        print(f"Error: {str(E)}")

    import os, time

    time.sleep(3)
    if os.system(f"curl localhost:60000") == 0:
        print("test Success !")
        exit()
    else:
        print("Error !")
        exit()
