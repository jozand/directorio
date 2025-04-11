from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ubicacion(db.Model):
    __tablename__ = 'ubicacion'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion_id_padre = db.Column(db.Integer, db.ForeignKey('ubicacion.id'), nullable=True)

    sububicaciones = db.relationship('Ubicacion')

class Puesto(db.Model):
    __tablename__ = 'puesto'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

class Empleado(db.Model):
    __tablename__ = 'empleado'
    id = db.Column(db.Integer, primary_key=True)
    codigo_empleado = db.Column(db.String(50), unique=True, nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    extension = db.Column(db.String(10), nullable=True)
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicacion.id'), nullable=False)
    puesto_id = db.Column(db.Integer, db.ForeignKey('puesto.id'), nullable=False)

    ubicacion = db.relationship('Ubicacion')
    puesto = db.relationship('Puesto')
