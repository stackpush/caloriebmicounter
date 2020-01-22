
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    cal=''
    calloss=''
    store=''
    bmi = ''


    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bfast= float (request.form.get('bfast'))
        lunch = float (request.form.get('lunch'))
        dinner = float (request.form.get('dinner'))
        bmi = calc_bmi(weight, height)

        total= bfast+lunch+dinner

        temp=2000-total
        if temp>0:
            calloss=temp
        else :
            calloss='now in negative ! you have consumed more than your daily calorie requirement for today ! Stop eating !   '



    return render_template("calorieindex.html",bmi=bmi,cal=cal,calloss=calloss,store=store)


def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)), 2)

if __name__ == '__main__':
    app.run()