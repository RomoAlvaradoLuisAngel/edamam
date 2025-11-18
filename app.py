from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = 'nbkdslvnbsdbngbsnlNLNjbbNJEFSKNBGBDBNFNDBJDNBbdlnkdbdbeNEBDBFDJBJBFBSBSBÑDBDBDBBD'
API = "https://api.edamam.com/api/food-database/v2/parser"
API_KEY = "937ef3deb00ae9d109f4bd50ec9fc6fe"
API_ID = "8497257e"

@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('base.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    if request.method == 'POST':
        busqueda = request.form.get('busqueda', '').strip()
        if not busqueda:
            flash('Por favor, ingrese un término de búsqueda válido.', 'warning')
            return redirect(url_for('inicio'))
        
        params = {
            'app_id': API_ID,
            'app_key': API_KEY,
            'ingr': busqueda
        }
        try:
            response = requests.get(API, params=params)
            if response.status_code != 200:
                flash (f"Error en la solicitud a la API: {response.status_code}", 'error')
                return redirect(url_for('inicio'))
            
            data = response.json()
            alimentos_encontrados = data.get('hints', [])
            if not alimentos_encontrados:
                flash(f"No se encontraron alimentos para la búsqueda proporcionada.", 'warning')
                return redirect(url_for('inicio'))
    
            return render_template('resultado.html', alimentos=alimentos_encontrados, busqueda=busqueda)
        
        except requests.exceptions.RequestException as e:
            flash(f"Error en la solicitud a la API: {e}", 'error')
            return redirect(url_for('inicio'))
        

if __name__ == '__main__':
    app.run(debug=True)