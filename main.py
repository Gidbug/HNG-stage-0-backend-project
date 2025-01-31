from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def get_info():
    response = {
        "slack_name": "YourSlackName",  # Replace with your actual Slack name
        "email": "oyerindegideon01@gmail.com",  # Replace with your HNG registered email
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),  # Dynamic UTC time
        "github_url": "https://github.com/Gidbug/HNG-stage-0-backend-project"  # GitHub repo URL
    }
    return jsonify(response), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Allows external access when deployed

