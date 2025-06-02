from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"], post["image_url"])
    post_objects.append(post_obj)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route('/about')
def get_about():
    return render_template("about.html")


@app.route('/contact')
def get_contact():
    return render_template("contact.html")


@app.route('/posts/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
