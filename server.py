"""Python Flask WebApp Auth0 integration example
"""

import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
import streamlit as st
import jwt

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

from flask import Flask, render_template, session
import json

app = Flask(__name__)



ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")


CSU = "Initial server.py check"
sesh = session

global_token = None
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)


# Controllers API
@app.route("/")
def home():
    pretty_data = json.dumps(session.get("user"), indent=4)
    with open('output.txt', 'w') as file:
        file.write(pretty_data)
    # return render_template(
    return redirect(    
        "http://localhost:8501/Page_1"
        # session=session.get("user"),
        # # pretty=json.dumps(session.get("user"), indent=4),
        # pretty=pretty_data,
    )
# if __name__ == '__main__':
#     app.run(debug=True)

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    # decoded_token = jwt.decode(token['id_token'], options={"verify_signature": False})
    # global_token = token
    # print("Hi")
    # return redirect("FrontEnd/pages/Page_1.py")
    # global CSU
    # CSU = "Callback check"
    # email = decoded_token.get('email')
    # user_id = decoded_token.get('sub')
    # return redirect("http://localhost:8501/Page_1")
    return redirect("/")

# @app.route("/intermediate")
# def intermediate():
#     return redirect("http://localhost:8501/Page_1")

# REMOVING WROKING
# @app.route("/login")
# def login():
#     return oauth.auth0.authorize_redirect(
#         redirect_uri=url_for("callback", _external=True)
#     )
@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )
    


# @app.route("/logout")
#Added->
# @app.route("/logout")
# def logout():
#     session.clear()
#     return redirect("http://localhost:8501/")

# def logout():
#     session.clear()
#     return redirect(
#         "https://"
#         + env.get("AUTH0_DOMAIN")
#         + "/v2/logout?"
#         + urlencode(
#             {
#                 "returnTo": url_for("home", _external=True),
#                 "client_id": env.get("AUTH0_CLIENT_ID"),
#             },
#             quote_via=quote_plus,
#         )
#     )
@app.route("/logout")
def logout():
    # Redirect to Auth0 logout, which will then redirect back to /final-logout in your app.
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("final_logout", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route("/final-logout")
def final_logout():
    session.clear()
    return render_template("logout.html")
    # return redirect("http://localhost:8501/")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))
