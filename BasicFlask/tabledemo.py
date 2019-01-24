from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def index():
    
    #list1=["abc","xyz"]
    mydict = {
	'maths':80,'c':70,'java':60
	}
    return render_template('tabledemo.html',name=mydict)

@app.route("/home")
def home():
    return render_template('home.html')

if __name__=="__main__":
      app.run(debug=True)
