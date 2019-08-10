from flask import Flask, render_template #render_template es para que se abran archivos html
#objeto llamado app
app = Flask(__name__)
#aqui se hace la ruta principal por defecto
@app.route("/")
def home():
    return render_template("home.html")


#Se crea lo que dira en la pagina /about
@app.route("/about")
def about():
    return render_template("about.html")

#Validacion para comprobar si estamos ejecutando este archivo como archivo de ejecucion y no modulo
if __name__ == '__main__':
    #Nos permite ejecutar la aplicacion
    app.run(debug=True)