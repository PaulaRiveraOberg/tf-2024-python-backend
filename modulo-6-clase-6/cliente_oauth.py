# cliente_oauth.py
import os

from dotenv import load_dotenv
from requests_oauthlib import OAuth2Session

load_dotenv()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

authorization_base_url = "https://github.com/login/oauth/authorize"
token_url = "https://github.com/login/oauth/access_token"

client = OAuth2Session(GITHUB_CLIENT_ID)
auth_url, state = client.authorization_url(authorization_base_url)
print("Vista la siguiente url y autoriza", auth_url)

uri = input("Enter the URI: ")
client.fetch_token(
    token_url, client_secret=GITHUB_CLIENT_SECRET, authorization_response=uri
)
response = client.get("https://api.github.com/user")
print(response.json())
