from flask import Flask, render_template

app = Flask(__name__)

# post list
posts = [
    {'title': 'image01', 'content': 'hello', 'image': 'https://cdn.pixabay.com/photo/2021/10/15/11/06/lemon-background-6712130_640.png'},
    {'title': 'image02', 'content': 'hello', 'image': 'https://cdn.pixabay.com/photo/2023/08/07/08/35/broccoli-8174625_640.jpg'}
]

# main page
@app.route('/')
def home():
    return render_template('index.html', posts=posts)

# post page
@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts[post_id - 1]
    return render_template('post.html', post=post)

# about page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

