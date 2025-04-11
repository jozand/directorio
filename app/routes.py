from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Empleado, Ubicacion, Puesto

main = Blueprint('main', __name__)

@main.route('/')
def index():
    empleados = Empleado.query.all()
    return render_template('index.html', empleados=empleados)

@main.route('/nuevo', methods=['GET', 'POST'])
def nuevo_empleado():
    if request.method == 'POST':
        nuevo = Empleado(
            codigo_empleado=request.form['codigo_empleado'],
            nombre=request.form['nombre'],
            extension=request.form['extension'],
            ubicacion_id=request.form['ubicacion_id'],
            puesto_id=request.form['puesto_id']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('main.index'))

    ubicaciones = Ubicacion.query.all()
    puestos = Puesto.query.all()
    return render_template('empleado_form.html', ubicaciones=ubicaciones, puestos=puestos)
