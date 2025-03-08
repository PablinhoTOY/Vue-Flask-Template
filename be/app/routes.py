
from app import app, IST

from flask import request

from app.Controllers import (
    UsersController as users,
)

@app.route("/", methods=["GET"])
def Prueba():
    result = users.Prueba()
    return result.jsonify()
