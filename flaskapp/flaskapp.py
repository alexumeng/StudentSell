from flask import Flask, render_template

app = Flask(__name__) #name of module

posts = [
    {
        'user': 'Alex Meng',
        'title': 'Keyboards',
        'content': 'Im selling a cool gamer keyboard.',
        'price': '$420.00'
    },
    {
        'user': 'Kristine Nguyen',
        'title': 'Illustrations',
        'content': 'Commission me for some cool art. Furries free.',
        'price': '$9999.00'
    },
    {
        'user': 'Emily Ngai',
        'title': 'Socks',
        'content': 'I knitted socks! Order some here :). DNI if u sleep with socks on or if ur a man.',
        'price': '$69.00'
    },
    {
        'user': 'Lexi Rodriguez',
        'title': 'Dry Lip Deputy',
        'content': 'Ending dry lips on campus 1 custom chapstick at a time.',
        'price': '$10.00'
    },
    {
        'user': 'Emily Jackson',
        'title': 'Take my Stats Midterm for Me',
        'content': 'Please PLease PLEASE PLESE.',
        'price': 'free'
    },
    {
        'user': 'Carlos Gutierrez',
        'title': 'Mario Cart Trainer',
        'content': '1 coaching session with the #1 mario cart-er in the world.',
        'price': '$1000.00'
    }
]

#what we type into our browser to go to different pages
@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('home.html')

@app.route("/feed")
def feed():
    return render_template('userfeed.html', posts=posts)

@app.route("/styles/style.css")
def style():
    return render_template('layout.html')

if __name__ == '__main__':
    app.run(debug=True)