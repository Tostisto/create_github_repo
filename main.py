import requests
import argparse
import os
from setup import GITHUB_USER, GITHUB_TOKEN

GITHUB_URL = "https://api.github.com"

parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()
repo_name = args.name
is_private = args.is_private

if is_private:
    payload = '{"name": "' + repo_name + '", "private": true }'
else:
    payload = '{"name": "' + repo_name + '", "private": false }'

header = {
    "Authorization": "token " + GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}

repo = requests.post(GITHUB_URL + "/user/repos", data=payload, headers=header)

os.system("git clone https://github.com/" + GITHUB_USER + "/" + repo_name)