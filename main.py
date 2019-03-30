from flask import Flask, request
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form method={{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
      <form action="/something" method="post">

        <label for="rot">
            ENTER #
            <input type="number" name="rot" value="0"/>
        </label>
        <label for="text">
            <textarea id="text" type=text name="text">
            {0}
            </textarea>
        </label>
        <input type="submit" value="Submit">
      </form>
    </body>
</html>
"""
@app.route("/")
def index():
    result = form.format("")
    return result

@app.route("/something" , methods=['POST'])
def encrypt():
    en_num = int(request.form['rot'])
    en_mes = request.form['text']
    
    result = rotate_string(en_mes, en_num)
    message = form.format(result)

    return '<h1>' + message + '</h1>'

app.run()