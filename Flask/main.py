from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return'Hola, mundo.'

if __name__ == '__main__':
    app.run(port=8080)

#localhost:8080   en la pagina web para accesar