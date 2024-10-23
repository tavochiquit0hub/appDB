import tkinter as tk
from classShowRecord import ShowRecord  # Importa la clase ShowRecord

# Configuración de la interfaz gráfica
ventana = tk.Tk()
app = ShowRecord(ventana)  # Crea una instancia de ShowRecord
ventana.mainloop()  # Inicia la aplicación
