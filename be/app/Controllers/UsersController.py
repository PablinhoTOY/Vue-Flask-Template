
from . import ControllerObject
import logging
from app.Models.UsersAdmin import Users, Roles

def PruebaKiosko():
    ret = ControllerObject()
    logger = logging.getLogger("modulos")
    logger.info(f"Entro correctamente al endpoint")
    ret.mensaje = "Se realizó la consulta exitosamente"
    ret.status = 200
    return ret