# import our flask library 
from flask import Flask 

# create our app instance         
app = Flask(__name__)              

# we create our app route as /, we can use something else as well probably "/hello" 
@app.route("/")                
def hello():
    return "Hello World!"  
  
# this is to automatically run the app  
if __name__ == "__main__":         
    app.run()
