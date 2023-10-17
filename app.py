from flask import Flask 

app = Flask()

@app.route("/" , methods=['POST'])
def addReview():
    # 

    pass

@app.route("/", methods=['GET'])
def getReview():
    # 
    pass