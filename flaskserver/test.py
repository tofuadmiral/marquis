from flask import Flask
app = Flask(__name__)

@app.route('/chatbot')
def hello_world():
    # this is the endpoint for the chatbot
    return "welcome to the chatbot"

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
