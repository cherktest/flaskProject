from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def dafault_route():
    return 'Messenger Flask server is running! ' \
           '<br> <a href="/status">Check status</a>'

if __name__ == '__main__':
    app.run()