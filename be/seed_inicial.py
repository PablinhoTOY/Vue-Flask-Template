from app import db, app, IST

from sqlalchemy import insert

from app.Models.Deudas import TipoDeuda
from app.Models.Servicios import TipoServicio
from app.Models.UsersAdmin import Users, Roles, roles_users
from datetime import datetime
def seed_db():
    
    deudas_to_insert = [TipoDeuda(nombre='Matricula',fecha_creacion=datetime.now(IST),fecha_actualizacion=datetime.now(IST), status='active'),
                          TipoDeuda(nombre='Multa de Biblioteca',fecha_creacion=datetime.now(IST),fecha_actualizacion=datetime.now(IST), status='active')]
    
    servicios_to_insert = [TipoServicio(nombre='Boletos de Bus',fecha_creacion=datetime.now(IST),fecha_actualizacion=datetime.now(IST), status='active', url='no-existe', costo_boleto=0.25),
                          TipoServicio(nombre='Fotocopias',fecha_creacion=datetime.now(IST),fecha_actualizacion=datetime.now(IST), status='active', url='copias/asignar', costo_boleto=0.05)]
    
    
    roles_to_insert = [Roles(name="Administrador")]
    
    #Reemplazar correo por uno que tenga acceso. De lo contrario, no podrá iniciar sesión.                    
    user_to_insert = [Users(email="pablo.lizana@utp.ac.pa", nombre="Pablo", apellido="Lizana", active=1, secret="chutinga1234", fs_uniquifier="8@uQHvRniq5TDQ67ung&bXL38d3M5NerLfxoH@X!", updated_at=datetime.now(IST), fecha_creacion=datetime.now(IST), roles=[roles_to_insert[0]])]

    db.session.bulk_save_objects(deudas_to_insert)
    db.session.bulk_save_objects(servicios_to_insert)
    db.session.bulk_save_objects(roles_to_insert)
    db.session.bulk_save_objects(user_to_insert)
    
    db.session.commit()
        
    stmt = (insert(roles_users).values(usuario_id='1', role_id='1'))
    db.session.execute(stmt)

    db.session.commit()