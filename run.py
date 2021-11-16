from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return {"msg":"Working demo of http bin basic"}, 200

@app.route('/status/<code>')
def status_ret(code):
    if code == 500 :
        return {"msg" : "internal server error","code" : code}, code
    elif code == 502 :
        return {"msg" : "bad gateway","code" : code}, code
    elif code == 503 :
        return {"msg" : "service unavailable","code" : code}, code
    elif code == 400 :
        return {"msg" : "bad request","code" : code}, code
    elif code == 401 :
        return {"msg" : "unauthorized","code" : code}, code
    elif code == 403 :
        return {"msg" : "forbidden","code" : code}, code
    elif code == 404 :
        return {"msg" : "not found","code" : code}, code
    else :
        return {"msg" : "returning msg","code" : code}, code
    
if __name__ == "__main__":
    app.run(debug=True)
