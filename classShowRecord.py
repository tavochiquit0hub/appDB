import tkinter as tk
from classGetRecord import GetRecord  # Importa la clase GetRecord

class ShowRecord:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Último Registro Estudiante")
        self.ventana.geometry("300x200")

        # Etiqueta para mostrar los resultados
        self.resultado_label = tk.Label(self.ventana, text="", justify="left")
        self.resultado_label.pack(pady=10)

        # Botón para cargar los datos
        self.boton_cargar = tk.Button(self.ventana, text="Cargar Datos", command=self.load_data)
        self.boton_cargar.pack(pady=10)

        self.get_record = GetRecord()  # Crear una instancia de GetRecord

    # Método para cargar datos
    def load_data(self):
        registro = self.get_record.get_last_record()  # Obtener el último registro
        if registro:
            self.mostrar_datos(registro)  # Mostrar los datos en la etiqueta
        else:
            self.resultado_label.config(text="No se encontraron registros o hubo un error.")

    # Método para mostrar los datos
    def mostrar_datos(self, registro):
        texto = f"ID: {registro['id']}\n" \
                f"Nombre: {registro['nombre']}\n" \
                f"Apellido: {registro['apellido']}\n" \
                f"Ciudad: {registro['ciudad']}\n" \
                f"Calle: {registro['calle']}"
        self.resultado_label.config(text=texto)  # Actualiza la etiqueta con los datos
