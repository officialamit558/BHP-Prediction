from flask import Flask, request ,jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hii'




if __name__ == "__main__":
    print("Starting Python Flask server for home price prediction")
    app.run()