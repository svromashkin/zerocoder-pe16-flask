import datetime
import os
import platform
import socket

from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder="public", static_url_path="")

VERSION = "1.1"
TITLE = "QuietPod deploy demo"


@app.get("/")
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.get("/api/status")
def status():
    now = datetime.datetime.now().astimezone()
    return jsonify(
        version=VERSION,
        title=TITLE,
        host=socket.gethostname(),
        system=platform.platform(),
        python=platform.python_version(),
        server_time=now.strftime("%Y-%m-%d %H:%M:%S %z"),
        in_docker=os.path.exists("/.dockerenv"),
        wsgi=request.environ.get("SERVER_SOFTWARE", "неизвестно"),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
