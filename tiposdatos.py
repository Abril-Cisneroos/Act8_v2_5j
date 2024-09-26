print("Clase v2  Frida Abril Cisneros")
# zona de clase
class Datos:
    # el constructor
    def __init__(self,estatura,peso):
        self.estatura=estatura
        self.peso=peso
    def mostrar_datos(self):
        print(f"Estatura: {self.estatura} mts,  Peso: {self.peso} Kg")
        
    def mi_lista_1162(self):
        flores=["Flor de loto","Flor nube","Freesia"]
        print(flores)
        for fl in flores:
            print(fl)
            
    def mi_tupla_1162(self):
        peliculas=("Love Roise", "he's just not that into you","Me before you")
        print(peliculas)
        for p in peliculas:
            print(p)
            
    def mi_diccionario_1162(self):
        pais = {
            "Nombre": "Mexico",
            "Idioma": "Español",
            "Continente": "America"
        }
        print(pais)
        for m, x in pais.items():
            print(m,x)
            
    def mi_set_1162(self):
        colores={"Rojo","Azul","Amarillo"}
        print(colores)
        for c in colores:
            print(c)
            
# creacion de objetos
informacion=Datos(1.65,55.5)

#utilizando el obj --> info
informacion.mostrar_datos()
print("Lista de flores")
informacion.mi_lista_1162()
print("Tupla de peliculas")
informacion.mi_tupla_1162()
print("conjunto de colores")
informacion.mi_set_1162()
print("Diccionario de pais")
informacion.mi_diccionario_1162()

