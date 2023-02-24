from flask import *
import random
import re
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)
@app.route("/")
def home():
    url = 'https://floridanewsheadlines.com/articles/florida-man/'
    r = requests.get(url)
    html_page = r.text
    links = []
    soup = BeautifulSoup(html_page, "html.parser")
    for link in soup.findAll('a'):
        pattern = 'articles\/\d+$'
        prog = re.compile(pattern)
        result = prog.search(link.get('href'))
        if result:
            #print(link.get('href'))
            #print(link.get('title'))
            links.append(link.get('title'))
    randomLine = random.choice(links)
    return render_template("home.html", fact=randomLine, secret_env_test="")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
