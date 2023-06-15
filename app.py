from flask import Flask, request, render_template,jsonify
app = Flask(__name__,static_url_path='/static')

from proyecto_lab_copy import Classifier

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])

def procesar():
    data = request.get_json()
    clasificador=Classifier(int(data['frio']),int(data['calor']))
    read, prob_frio = clasificador.resp()
    h,t = read
    if prob_frio<=0.4: mensaje = 'Si eres team verano, hoy es tu día de suerte :)'
    elif prob_frio<=0.6: mensaje = 'Tal vez lleva un chaleco en la mochila...'
    else: mensaje = 'Te recomendamos usar chaleco!!'
    
    resultados = {
        'temperatura': t,
        'humedad': h,
        'probabilidad': round(prob_frio*100,2),
        'mensaje': mensaje
    }
    
    # Devolver los resultados como JSON
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(debug=False)