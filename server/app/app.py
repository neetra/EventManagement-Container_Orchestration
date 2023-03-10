from flask import Flask


app = Flask(__name__)

@app.route("/", methods = ["GET"])
def ping()              :
    try:        
       return {"message" : "ping event management"}, 200       
    except :
      
        return {"message" : "error"}, 409   

if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    app.run()