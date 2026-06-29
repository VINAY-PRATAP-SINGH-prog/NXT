import monitor
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from events import events

app = Flask(__name__,static_folder="../frontend")
CORS(app)



@app.route("/")
def index():
    return send_from_directory(app.static_folder,"index.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route("/events")
def get_events():
    return jsonify(events)
if __name__ == "__main__":
    monitor.start_monitor()
    app.run(host="0.0.0.0", port=5000, debug=False)