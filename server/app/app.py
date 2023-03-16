import os

from flask import Flask

import event;
    
    # create and configure the app
app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(event.bp)
#app.add_url_rule("/", endpoint="index")    

    
    # a simple page that says hello
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    # https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
    app.run()
  


   