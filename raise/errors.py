class FloatNumberError(Exception):
    pass

def somar_inteiros(numero_um, numero_dois):
    try:
        if type(numero_um) is float or type(numero_dois) is float:
            raise FloatNumberError("Formato inválido para a soma")
        
        return numero_um + numero_dois

    except FloatNumberError as err:
        return err

    
somar_inteiros(2.3, 4.2)