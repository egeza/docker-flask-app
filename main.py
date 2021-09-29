from flask import Flask #importing Flask package

app = Flask(__name__)

@app.route('/') #to convert simple python fxn to the flask
def  hell_world():
    return 'KEEP LEARNING, KEEP MOVING AHEAD'

if __name__=="__main__":
    app.run(port=5001, debug=True)