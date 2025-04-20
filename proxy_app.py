from flask import Flask, redirect, request
import requests

app = Flask(__name__)

GOOGLE_AUTH_BASE = "https://accounts.google.com/o/oauth2/v2/auth"
GOOGLE_TOKEN_BASE = "https://oauth2.googleapis.com/token"

@app.route("/oauth/authorize")
def proxy_authorize():
    # 将请求参数原样转发给 Google 授权地址
    return redirect(f"{GOOGLE_AUTH_BASE}?{request.query_string.decode()}")

@app.route("/oauth/token", methods=["POST"])
def proxy_token():
    # 将表单数据 POST 到 Google Token 接口
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(GOOGLE_TOKEN_BASE, data=request.form, headers=headers)
    return response.content, response.status_code, response.headers.items()

@app.route("/")
def health_check():
    return "Proxy service running.", 200
