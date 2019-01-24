from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def index():
    abc ="Omkar"
    #return abc
    return render_template('demo.html') + abc

if __name__=="__main__":
      app.run(debug=True)
