import re

def validar(entrada):
    
        entrada_limpia = re.sub(r"\s+", "", entrada)
        
        # Nombre de la bebida seguido por tamaños/numeros separados por comas
        if not re.match(r"^[A-Za-z]+(,([1-9]|[1-3][0-9]|4[0-8])){1,5}$", entrada_limpia):  #regex que verifica el formato
            return False, "Formato de entrada inválido."
        
        # Separar nombre y tamaños
        nombre, *tam = entrada_limpia.split(',')
        tam = [int(t) for t in tam]
        
        # Nombre de bebida
        if not (2 <= len(nombre) <= 15):
            return False, "Longitud del nombre de la bebida inválida."
        
        # Rango de Tamaños
        #if not all(1 <= t <= 48 for t in tam):
            #return False, "Tamaño de bebida fuera de rango."
        
        # Orden de Tamaños
        if tam != sorted(tam):
            return False, "Los tamaños no están en orden ascendente."
        
        return True, "Entrada válida."

#n = input()
#resultado = validar(n)
#print(resultado)
