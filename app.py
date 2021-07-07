from flask import Flask, render_template  
  
app = Flask(__name__) #creating the Flask class object   


@app.route('/home') #route for homepage  
def home():  
    return render_template("home.html") 

@app.route('/james') #route for james's page   
def JamesDetails():  
    return render_template("james.html")

if __name__ =='__main__':  
    app.run(host = '0.0.0.0', port='5000', debug=True)
