from flask import Flask, render_template

app = Flask(__name__,template_folder='../vista')

@app.route('/')
def inicio():
    return render_template('registro.html')

@app.route('/modificar')
def modificarTarjeta():
    return render_template('modificar.html')

@app.route('/consultar')
def consultarTarjetas():
    return render_template('consultar.html')

@app.route('/eliminar')
def eliminarTarjeta():
    return render_template('eliminar.html')

@app.route('/guardar',methods=['post'])
def guardarInformacion():

    return '<h1>Guardando informacion</h1>' '<br>' '<a href="/">Regresar</a>'



if __name__ == '__main__':
    app.run(debug=True);