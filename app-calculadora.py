from flask import Flask ## Flask es un microfamework para el uso de python en la web
from flask_cors import CORS ## Necesario para configurar acceso de progamas de terceros 
import math as mt ## Libreria que implementa funciones matematicas
from flask import jsonify ## Para retornar las respuestas en formato json
app=Flask(__name__)
CORS(app)

## Suma
@app.route("/")
@app.route("/<float:numero1>/<float:numero2>")
@app.route("/<int:numero1>/<int:numero2>")
@app.route("/<int:numero1>/<float:numero2>")
@app.route("/<float:numero1>/<int:numero2>")
def suma(numero1=0,numero2=0):
    resultado=numero1+numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <h1>
    data={
        "Resultado":resultado,
        "Operacion":"suma",
    }
    return jsonify(data)
## Resta
@app.route("/resta/<float:numero1>/<float:numero2>")
@app.route("/resta/<int:numero1>/<int:numero2>")
@app.route("/resta/<int:numero1>/<float:numero2>")
@app.route("/resta/<float:numero1>/<int:numero2>")
def resta(numero1=0,numero2=0):
    resultado=numero1-numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"resta",
    }
    return jsonify(data)

## multiplicacion
@app.route("/multiplicacion/<float:numero1>/<float:numero2>")
@app.route("/multiplicacion/<int:numero1>/<int:numero2>")
@app.route("/multiplicacion/<float:numero1>/<int:numero2>")
@app.route("/multiplicacion/<int:numero1>/<float:numero2>")
def multiplicaion(numero1=0,numero2=0):
    resultado=numero1*numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"multiplicaion",
    }
    return jsonify(data)

## Division
@app.route("/Division/<float:numero1>/<fploat:numero2>")
@app.route("/Division/<int:numero1>/<int:numero2>")
@app.route("/Division/<float:numero1>/<int:numero2>")
@app.route("/Division/<int:numero1>/<float:numero2>")
def Division(numero1=0,numero2=0):
    resultado=numero1/numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"Division",
    }
    return jsonify(data)

## potenciacion
@app.route("/potenciacion/<float:numero1>/<float:numero2>")
@app.route("/potenciacion/<int:numero1>/<int:numero2>")
@app.route("/potenciacion/<int:numero1>/<float:numero2>")
@app.route("/potenciacion/<float:numero1>/<int:numero2>")
def potenciacion(numero1=0,numero2=0):
    resultado=numero1**numero2
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"potenciacion",
    }
    return jsonify(data)

## seno
@app.route("/seno/<float:numero1>")
@app.route("/seno/<int:numero1>")
def seno(numero1=0):
    resultado=mt.sin(numero1)
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"seno",
    }
    return jsonify(data)

## seno
@app.route("/coseno/<float:numero1>")
@app.route("/coseno/<int:numero1>")
def coseno(numero1=0):
    resultado=mt.cos(numero1)
    ##return f"<h1>El resultado es: {resultado}</h1> <hr>"
    data={
        "Resultado":resultado,
        "Operacion":"coseno",
    }
    return jsonify(data)

if __name__=='__main__':
    ## El valor True indica que la app se deja en modo debug
    app.run(debug=True)