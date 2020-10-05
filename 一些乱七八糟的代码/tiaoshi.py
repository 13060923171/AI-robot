from flask import Flask,request
app = Flask(__name__)

@app.route("/v1/motions")
def v1():
    information = request.args.get("name","")
    return information

if __name__ == '__main__':
    app.run(debug=True)