from random import randint
from flask import Flask, render_template
from meme import Meme
import requests
app = Flask(__name__)
MEME_API = "https://meme-api.com/gimme/"



@app.route("/")
def show_example():
    num=randint(1,50)
    return render_template("index.html",rand_num=num)


@app.route("/memes/<int:num>")
def show_memes(num):
    url = f"{MEME_API}{num}"
    memes = requests.get(url=url).json().get("memes")
    meme_objects=[]
    for meme in memes:
        post_name=meme["title"]
        image=meme["url"]
        post_link=meme["postLink"]
        subreddit=meme["subreddit"]
        meme_obj=Meme(post_name,post_link,subreddit,image)
        meme_objects.append(meme_obj)
    return render_template("memes.html",memes=meme_objects)


if __name__ == "__main__":
    app.run(debug=True)
