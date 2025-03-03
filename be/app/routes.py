
from app import app, IST

from flask import request

from app.Controllers import (
    UsersController as users,
)

@app.route("/", methods=["GET"])
def Kiosko():
    result = users.PruebaKiosko()
    return result.jsonify()
