from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# code business logic

@app.route('/')  ## decorator -@ , when route(/) is found whatever's written underneath gets processed
def base ():
    return render_template("home.html")

@app.route('/contact')  ## decorator -@ , when route(/) is found whatever's written underneath gets processed
def contact ():
    return "Contact page"

@app.route('/galary')  ## decorator -@ , when route(/) is found whatever's written underneath gets processed
def galary ():
    return render_template("gallary.html")

@app.route('/cart')  ## decorator -@ , when route(/) is found whatever's written underneath gets processed
def cart ():
    return "Cart"

@app.route('/predict', methods=['post'])
def predict():

    model = pickle.load(open('diabetic.pkl', 'rb'))
    preg = request.form.get('preg') ## function to get the exp after submit button is clicked on webpage
    plas = request.form.get('plas')
    pres = request.form. get('pres')
    skin = request.form.get('skin') ## function to get the exp after submit button is clicked on webpage
    test = request.form.get('test')
    mass = request.form. get('mass')
    pedi = request.form.get('pedi') ## function to get the exp after submit button is clicked on webpage
    age = request.form.get('age')
    

    print(preg, plas, pres, skin, test, mass, pedi, age)
    output = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if output[0] == 0:
        data = "person is diabetic"
    else : 
        data = "not diabetic"

    

    return render_template("predict.html", data = data) ## ginger format inhtml


if __name__ == "__main__":
    app.run(debug = True)

## create env and pip install flask frist

