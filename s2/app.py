from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


class BlogPost:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class BlogManager:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)


new_blog = BlogManager()


@app.route('/')
def index():
    title = request.args.get('title')
    content = request.args.get('content')

    if title and content:
        new_post1 = BlogPost(title=title, content=content)
        new_blog.add_post(new_post1)

    posts = new_blog.posts
    return render_template('pages/index.html', data=posts)


@app.route('/page2')
def xyz():

    return 'Hello page2'


app.run(debug=True)