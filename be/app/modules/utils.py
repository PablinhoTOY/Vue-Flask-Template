

def processCorreo(correo):
    char_remove_correo = ['"',"\n"]
    for x in char_remove_correo:
        correo = correo.replace(x,'')
    return correo