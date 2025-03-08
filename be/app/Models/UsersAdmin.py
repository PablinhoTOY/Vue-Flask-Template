from app import db, IST
from datetime import datetime
from flask_security import UserMixin, RoleMixin

class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    profile_image = db.Column(
        db.String(255), nullable=False, default="default_portrait.png"
    )
    secret = db.Column(db.TEXT, unique=True, nullable=False)
    fecha_creacion = db.Column(db.DateTime(timezone=True), default=datetime.now(IST))
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(IST), onupdate=datetime.now(IST)
    )
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.Text, unique=True, nullable=True)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Roles', secondary = 'roles_users', backref="user", lazy="select")
    
    def __repr__(self):
        return '<User %r>' % self.id

    def toDict(self):
        
        return {
            "id": self.id,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "active": self.active,
            "roles": [r.name for r in self.roles],
            "fecha_creacion": self.fecha_creacion,
            "last_login": self.last_login_at,
        }

roles_users = db.Table(
    "roles_users",
    db.Column('id', db.Integer, primary_key=True),
    db.Column("usuario_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("role.id")),
)


class Roles(db.Model, RoleMixin):
    __tablename__ = "role"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    created_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(IST)
    )
    updated_at = db.Column(
        db.DateTime(), nullable=False, default=datetime.now(IST), onupdate=datetime.now(IST)
    )

    def as_dict(self):
        return {"id": self.id, "name": self.name,"permisos": [r.as_dict() for r in self.permisos]}

    def __repr__(self):
        return '<Role %r>' % self.id