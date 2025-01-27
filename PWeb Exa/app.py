from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/pagina1', methods=['GET', 'POST'])
def pagina1():
    if request.method == 'POST':
        if 'nombre' in request.form and 'edad' in request.form and 'tarros' in request.form:
            nombre = request.form['nombre']
            edad = int(request.form['edad'])
            cantidad_tarros = int(request.form['tarros'])

            precio_tarro = 9000
            total_sin_descuento = cantidad_tarros * precio_tarro

            if 18 <= edad <= 30:
                descuento = total_sin_descuento * 0.15
            elif edad > 30:
                descuento = total_sin_descuento * 0.25
            else:
                descuento = 0

            total_con_descuento = total_sin_descuento - descuento

            return render_template('ejercicio01.html', nombre=nombre,
                                   total_sin_descuento=total_sin_descuento, descuento=descuento,
                                   total_con_descuento=total_con_descuento)

    return render_template('ejercicio01.html')

@app.route('/pagina2', methods=['GET', 'POST'])
def pagina2():
    mensaje = ""
    if request.method == 'POST':
        nombre = request.form['nombre']
        contrasena = request.form['contraseña']

        if nombre == "juan" and contrasena == "admin":
            mensaje = "Bienvenido administrador juan"
        elif nombre == "pepe" and contrasena == "user":
            mensaje = "Bienvenido usuario pepe"
        else:
            mensaje = "Nombre de usuario o contraseña incorrectos"

    return render_template('ejercicio02.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
