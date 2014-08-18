from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    html_str = '<h1>%s</h1><img src="%s" />' % \
               ('Hello Kitty',
                'http://impressivemagazine.com/wp-content/uploads/2013/09/Hello-Kitty.jpg')
    return html_str

if __name__ == '__main__':
    app.run(host='0.0.0.0')
