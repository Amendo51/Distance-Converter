from flask import Flask, request, render_template
import numpy as np
def left_side(x):
    yr = x * 1760
    ft = x *5280
    inc =x*63360
    return yr, ft, inc
def right_side(x):
    km=x*1.609
    m=x*1609
    cm= x*160934
    return km,m,cm

def process_input(s):
    return eval(s)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('application.html')

@app.route('/',methods =["POST"] )
def request_data():
    x = process_input(request.form['miledisplay'])

    while 'reset' not in request.form:
        if 'Convert1' in request.form:
            yr, ft, inc = left_side(x)
            return render_template('application.html',yard = yr,Feet = ft,inches= inc,Kim= request.form.get('kmdisplay'),Meters= request.form.get('mdisplay'),Center= request.form.get('cmdisplay'),mil = x)
        if 'Convert2'in request.form:
            km, m, cm = right_side(x)
            return render_template('application.html',Kim= km,Meters= m,Center= cm,yard = request.form.get('yrdisplay'),Feet = request.form.get('ftdisplay'),inches= request.form.get('indisplay'),mil=x)
        if 'eset' in request.form:
            return render_template('application.html',Kim='',Meters= '',Center= '',yard = '',Feet = '',inches= '')



if __name__ == '__main__':
        #app.confic['TEMPLACES_AUTO_RELOAD'] = True
        app.run(debug=True, use_reloader = True)