import re
from flask import Flask, jsonify
from datetime import datetime


app = Flask(__name__)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

@app.route("/")
def home():
    email = "oyerindegideon001@gmail.com"
    
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400

    return jsonify({
        "name": "Your Name",
        "email": "oyerindegideon001@gmail.com",
        "current_datetime": datetime.utcnow().isoformat(),
        "github_url": "https://github.com/Gidbug/HNG-stage-0-backend-project"
    })

if __name__ == "__main__":
    app.run(debug=True)
