from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    list1=["abc","xyz"]
    return render_template('passlist.html',name=list1)

if __name__=="__main__":
      app.run(debug=True)
