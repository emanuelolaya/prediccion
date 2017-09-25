from flask import Flask
import pickle

app = Flask(__name__)

@app.route('/<float:sl>/<float:sw>/<float:pl>/<float:pw>',methods=['GET'])

def prediccion(sl,sw,pl,pw):
    with open('modelof.mod', 'rb') as f:
        u = pickle._Unpickler(f)
        u.encoding = 'latin1'
        modelo = u.load()

    dato = [[sl, sw, pl, pw]]
    prediction1 = modelo.predict(dato)
    return prediction1

if __name__ == "__main__":
    app.run()
