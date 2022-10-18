from flask import Flask, render_template, request
from leds import *

app = Flask(__name__)

light_1 = False

@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('light-1') == 'light-1':
            print("toggle 0")
            toggle(0)
        elif  request.form.get('light-2') == 'light-2':
            toggle(1)
        else:
            #? other
            return render_template("main.html")
    elif request.method == 'GET':
        print("No Post Back Call")

    return render_template("main.html")

def check():
    if light_1:
        on(0)
    else:
        off(0)

if __name__ == '__main__':
    setup()
    try:
        app.run(host="0.0.0.0", port=80, debug=True)
    except KeyboardInterrupt:
        #? on end
        destroy()