# from flask import Flask
#
# app= Flask(__name__)
#
# @app.route('/')
# def hello() -> str:
#
#     return 'Hello world!'
# app.run()



from flask import Flask
from vsearch import search4letters
app= Flask(__name__)

@app.route('/')
def hello() -> str:

    return 'Hello world!'

@app.route('/sear4')
def do_search():
    return str(search4letters('life, the universe, and everythin!')) ## this function was export to system
app.run()


