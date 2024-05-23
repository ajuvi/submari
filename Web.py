from dades.Persistencia import Persistencia
from flask import Flask, request, jsonify, json, Response

app = Flask(__name__)

@app.route("/mesura/<nom>", methods=['GET'])
def mesura(nom):
	try:		
		return json_response(Persistencia.obtenir_ultima_mesura(nom))
	except Exception as e:
		return json_error(e)

@app.route("/mesura/all/<nom>", methods=['GET'])
def mesures(nom):
	try:
		return json_response(Persistencia.obtenir_mesures(nom))
	except Exception as e:
		return json_error(e)

def json_response(data,code=200):
    data = json.dumps(data,default=str)
    return Response(data,mimetype='application/json'),code

def json_error(e):
    data = json.dumps({'error':str(e)},default=str)
    return Response(data,mimetype='application/json'),500

app.debug = True
app.run(port=5000)
