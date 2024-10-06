# LIBRARYS
from datetime import timedelta
from flask import *
from dotenv import load_dotenv
import os

# Carga de variables de entorno del .env
load_dotenv()
secret_key = os.getenv("SECRET_KEY")

# Configuracion de la aplicacion web
app = Flask(__name__)
app.secret_key = secret_key
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = "Lax"
app.config['SESSION_COOKIE_DOMAIN'] = ".softkitacademy.com"
app.permanent_session_lifetime = timedelta(weeks=52) # Sesion con duracion de 52 semanas o 1 año
app.url_map.strict_slashes = False

@app.route("/", methods=["GET"])
def index():
    return "<h1>Service is working</h1>"

@app.route("/bucket")
def bucket():
    response = make_response("<h1>Service is working</h1>")
    response.status_code = 200
    return response

@app.route("/bucket/<path>")
def bucket_selector(path):
    if path == None:
        abort(400)
        
    
    if not os.path.exists("static/bucket/"+path):
        return abort(400)
        
    return send_from_directory("static/bucket", path)

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory("static/seo", request.path[1:])

@app.route('/favicon.ico')
def favicon():
    return send_from_directory("static/icons", "favicon.ico")

if __name__=="__main__":
    app.run(debug=True, host="127.0.0.1", port=5000, reloader_type="watchdog")