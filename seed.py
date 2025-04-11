from app import create_app
from app.models import db, Puesto, Ubicacion

app = create_app()

with app.app_context():
    # Limpia tablas (opcional para desarrollo)
    db.session.query(Puesto).delete()
    db.session.query(Ubicacion).delete()

    # Crear ubicaciones con jerarquía
    unidad = Ubicacion(nombre="AUDITORÍA INTERNA")
    estado = Ubicacion(nombre="JEFATURA AUDITORÍA INTERNA ", ubicacion_id_padre=unidad.id)
    ciudad = Ubicacion(nombre="SUPERVISORES", ubicacion_id_padre=unidad.id)

    db.session.add_all([unidad, estado, ciudad])

    # Crear puestos
    puestos = [
        Puesto(nombre="Auditor Interno"),
        Puesto(nombre="Supervisor General"),
        Puesto(nombre="Supervisor"),
        Puesto(nombre="Secretaria Ejecutiva I"),
        Puesto(nombre="Auxiliar Operativo III"),
        Puesto(nombre="Secretaria V"),
        Puesto(nombre="Oficinista I"),
        Puesto(nombre="Analista III de Auditoría Interna"),
        Puesto(nombre="Asesor de Auditoría Interna"),
        Puesto(nombre="Auxiliar de Auditoría Interna"),
        Puesto(nombre="Piloto I")
    ]
    db.session.add_all(puestos)

    db.session.commit()
    print("Datos iniciales insertados.")
