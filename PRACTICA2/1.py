"""Reglas:
- Crear una clase llamada Persona donde sus atributos deben ser nombre,
edad y de nacionalidad peruana (use el manejo de errores para el tipo de
dato) y un método para solicitar su nombre y edad.
- Tendrá un método cumpleaños donde cada vez que invoque aumentará en
un año la edad de la persona.
- Crear la instancia de la clase Persona y usar su método cumpleaños para
incrementar su edad (mínimo 2 vez, mostrar por pantalla dicha edad
actualizada).
- Crear una función que retorne solamente la fecha, hora y minuto que se ha
registrado esta persona (Mostrar por pantalla este valor)
2. Usando el concepto de herencia y encapsulación (para saldo) para crear el
siguiente programa (3 ptos): """

from datetime import datetime

class Persona:
    def _init_(self):
        self.nombre = ""
        self.edad = ""
        self.nacionalidad = "peruana"

    def solicitar_datos(self):
        self.nombre = input("Ingrese su nombre: ")
        while True:
            try:
                self.edad = int(input("Ingrese su edad: "))
                break
            except ValueError:
                print("Error: La edad debe ser un número entero. Intente nuevamente.")

    def cumpleanios(self):
        self.edad += 1

    def obtener_fecha_hora_registro(self):
        fecha_hora_registro = datetime.now()
        return fecha_hora_registro.strftime("%Y-%m-%d %H:%M")

# Crear instancia de la clase Persona
persona = Persona()

# Solicitar datos de la persona
persona.solicitar_datos()

# Mostrar edad inicial
print("Edad inicial:", persona.edad)

# Incrementar edad
persona.cumpleanios()
persona.cumpleanios()

#  edad actualizada
print("Edad actualizada:", persona.edad)

# Obtener y mostrar la fecha
fecha_hora_registro = persona.obtener_fecha_hora_registro()
print("Fecha y hora de registro:", fecha_hora_registro)
