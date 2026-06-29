import monitor
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from events import events

app = Flask(__name__)
CORS(app)



@app.route("/")

def home():
    return "NXT Backend Running"

@app.route("/events")
def get_events():
    return jsonify(events)
if __name__ == "__main__":
    monitor.start_monitor()
    app.run(debug=True, use_reloader=False)