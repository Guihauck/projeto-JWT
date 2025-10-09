from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify, request
import jwt

app = Flask(__name__)
@app.route("/login", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            'exp': datetime.now(timezone.utc) + timedelta(minutes=1),
            "email": "guilherme.hauck@gmail.com"
        },
        key="mykey",
        algorithm="HS256"
    )
    return jsonify({"teste":token}), 200

@app.route("/secret", methods=["POST"])
def EndpointSecret():
    raw_token = request.headers.get("Authorization")
    token = raw_token.split()[1]
    try:
        token_information = jwt.decode(token, key="mykey", algorithms="HS256")
        print(token_information)
    except Exception as exception:
        return jsonify({"error": str(exception)}), 400

    return jsonify({"key":"secret"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
