from flask import Flask, render_template, request
from leds import *

app = Flask(__name__)



@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Encrypt') == 'Encrypt':
            print("on")
            on(0)
        elif  request.form.get('Decrypt') == 'Decrypt':
            off(0)
        else:
            #? other
            return render_template("main.html")
    elif request.method == 'GET':
        print("No Post Back Call")

    return render_template("main.html")

if __name__ == '__main__':
    setup()
    try:
        app.run(host="0.0.0.0", port=80, debug=True)
    except KeyboardInterrupt:
        #? on end
        destroy()