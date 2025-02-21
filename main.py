import re
from flask import Flask, jsonify
from datetime import datetime
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/")
def home():
    email = "oyerindegideon01@gmail.com"
    current_datetime = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    return jsonify({
        
  "email": "oyerindegideon01@gmail.com",
  "current_datetime": current_datetime,
  "github_url": "https://github.com/Gidbug/HNG-stage-0-backend-project"
    })

if __name__ == "__main__":
    app.run(debug=True)
