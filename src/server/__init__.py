from http.server import HTTPServer, BaseHTTPRequestHandler
from os import getenv
import time


class Handler(BaseHTTPRequestHandler):
    """
    Simple request handler to respond on GET request
    """

    def do_GET(self):  # pylint: disable=invalid-name
        """
        Respond on a GET request
        """
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.server.output["time"] = time.asctime()
        message = """
        Server to run https://twitter.com/LitMashupBot.
        A Twitter bot that mashups two French writers and creates a cover.
        For more information, please contact <guillaume.ongenae@gmail.com> or https://twitter.com/GOngenae.

        Created by Guillaume Ongenae (https://g-ongenae.github.com/)
        """
        self.server.output["body"] = message

        output = ""
        for key in self.server.output:
            output = output + key + ": " + self.server.output[key] + "\n"

        self.wfile.write(output.encode())


def run_server():
    """
    Run the server
    """
    port = int(getenv("PORT"))
    httpd = HTTPServer(("0.0.0.0", port), Handler)
    httpd.output = {}
    httpd.output["name"] = "Literature Mashup Bot — HTTP Server"
    httpd.serve_forever()
