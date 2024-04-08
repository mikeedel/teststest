from Pruebas_practica import validar
import pytest

def test_nombre_alfabetico():
    resultado, _ = validar("Cafe,1,3,5")  #prueba que sea alfabetico
    assert resultado == True

def test_nombre_demasiado_corto():    #prueba que el tamaño
    resultado, _ = validar("C,1")
    assert resultado == False

def test_nombre_longitud_valida():          #prueba tamaño
    resultado, _ = validar("Espresso,1,2")
    assert resultado == True

def test_tam_fuera_de_rango():
    resultado, _ = validar("Latte,0,49")   #prueba el rango de los tamaños

def test_tam_no_entero():
    resultado, _ = validar("Mocha,2.5,3")
    assert resultado == False  # Esta prueba espera que la validación falle porque 2.5 no es un entero

def test_tam_orden_ascendente():
    resultado, _ = validar("Americano,1,2,3,4,5")   #prueba con los tamaños en orden ascendente
    assert resultado == True

def test_tam_desordenados():
    resultado, _ = validar("Frappe,5,4,3,2,1")      #los tamaños en diferente orden
    assert resultado == False

def test_sin_espacios():
    resultado, _ = validar(" Capuccino , 2 , 4 , 6 ")    #con espacios
    assert resultado == True

def test_maximo_cinco_tam():
    resultado, _ = validar("Latte,1,2,3,4,5")     #maximo 5 tamaños
    assert resultado == True

def test_mas_de_cinco_tam():
    resultado, _ = validar("Latte,1,2,3,4,5,6")  #se pasa de la cantidad de 5 tamaños
    assert resultado == False

def test_nombre_alfabetico_falso():
    resultado, _ = validar("123,1,3,5")
    assert resultado == False  # Ahora el nombre contiene dígitos y debería fallar.

def test_nombre_demasiado_corto_verdadero():
    resultado, _ = validar("Ca,1")
    assert resultado == True  #Ca tiene 2 caracteres, que es la longitud mínima válida

def test_nombre_longitud_valida_falso():
    resultado, _ = validar("NombreMuyLargoParaCafe,1,2")
    assert resultado == False  #El nombre excede los 15 caracteres

def test_tam_fuera_de_rango_verdadero():
    resultado, _ = validar("Latte,1,24")
    assert resultado == True  #Ambos tamaños están dentro del rango permitido (1-48)

def test_tam_no_entero_verdadero():
    resultado, _ = validar("Mocha,2,3")
    assert resultado == True  #Los tamaños son enteros y válidos

def test_tam_orden_ascendente_falso():
    resultado, _ = validar("Americano,5,4,3,2,1")
    assert resultado == False  #Los tamaños no están en orden ascendente

def test_tam_desordenados_verdadero():
    resultado, _ = validar("Frappe,1,2,3,4,5")
    assert resultado == True  # Los tamaños están en orden ascendente

def test_sin_espacios_falso():
    resultado, _ = validar("Capuccino, 60")
    assert resultado == False  #60 está fuera del rango permitido para el tamaño

def test_maximo_cinco_tam_falso():
    resultado, _ = validar("Latte")  #sin tamaños
    assert resultado == False

def test_mas_de_cinco_tam_verdadero():
    resultado, _ = validar("Latte,1,2,3")
    assert resultado == True  # Menos de cinco tamaños es válido 
