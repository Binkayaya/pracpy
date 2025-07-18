from flask import Flask, redirect, request, session, url_for
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")


# Replace with your GitHub OAuth credentials
CLIENT_ID = os.environ.get("YOUR_CLIENT_ID")
CLIENT_SECRET = os.environ.get("YOUR_CLIENT_SECRET")

GITHUB_AUTH_URL = "https://github.com/login/oauth/authorize"
GITHUB_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_API_URL = "https://api.github.com/user"

@app.route('/')
def home():
    return '<a href="/login">Login with GitHub</a>'

@app.route('/login')
def login():
    return redirect(f"{GITHUB_AUTH_URL}?client_id={CLIENT_ID}&scope=read:user")

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_res = requests.post(GITHUB_TOKEN_URL, headers={'Accept': 'application/json'}, data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
    })
    token_json = token_res.json()
    access_token = token_json.get('access_token')

    if not access_token:
        return f"Error: {token_json}"

    # Save token in session (in-memory for now)
    session['token'] = access_token

    user_res = requests.get(GITHUB_API_URL, headers={
        'Authorization': f'token {access_token}'
    })
    user_data = user_res.json()
    return f"<h1>Welcome {user_data['login']}</h1><p>{user_data}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=8000)


