from flask import Flask, redirect, request
import requests

app = Flask(__name__)

GOOGLE_AUTH_BASE = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_BASE = "https://oauth2.googleapis.com/token"

# 授权跳转
@app.route("/oauth/authorize")
def proxy_authorize():
    return redirect(f"{GOOGLE_AUTH_BASE}?{request.query_string.decode()}")

# 授权回调，提供给 OpenAI 插件识别
@app.route("/oauth/callback")
def oauth_callback():
    code = request.args.get("code", "")
    return f"OAuth callback received. Code: {code}", 200

# 获取 token
@app.route("/oauth/token", methods=["POST"])
def proxy_token():
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(GOOGLE_TOKEN_BASE, data=request.form, headers=headers)
    return response.content, response.status_code, response.headers.items()

if __name__ == "__main__":
    app.run()
