from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/hello', methods=['GET', 'POST'])
def hello_world():
    print("What should I print?")
    return "Hello, World!!!"
    
@app.route('/hello/<name>', methods=['GET'])
def hello_person(name):
    return render_template("hello.html", html_name=name)
#    return render_template("hello.html", name=name)
    
#    return "Hello,  {}!".format(name)
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
