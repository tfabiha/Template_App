from flask import Flask
app = Flask(__name__) # create instance of class Flask

@app.route("/") #assign fxn to route
def hello_world():
    return "No hablo queso!"

if __name__ == "__main__":
    app.debug = True
    app.run()
