from flask import Flask, json, request

api= Flask(__name__)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    
    if (content_type == 'application/json'):
        jsonReq = request.json
        scodicefiscale = jsonReq["codf"]
        anagrafe = JsonDerialize(sAnagrafe)
        if scodicefiscale not in anagrafe:
            dNuovoCittadino = ComponiDatoCittadino(jsonReq)
            anagrafe[scodicefiscale] = dNuovoCittadino
            jsonSerialize(anagrafe, sAnagrafe)
            jsonResp = {"Esito":"200", "Msg":"ok"}
            return json.dumps(jsonResp), 200
        else:
            jsonResp = {"Esito": "001", "Msg": "Cittadino gia preso"}
            return json.dumps(jsonResp), 200
    else:
        return 'Content-Type not supported!', 401


api.run(host="127.0.0.1", port=8080)