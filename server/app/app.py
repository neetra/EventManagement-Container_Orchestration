from flask import Flask,jsonify
from events import event;
from flask_cors import CORS
    
    # create and configure the app
app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.register_blueprint(event.bp)
#app.add_url_rule("/", endpoint="index")    

    
    # a simple page that says hello
@app.route('/')
def hello():
    return jsonify({'message' : 'Hello, World!'}), 200

if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    app.run()
  


   