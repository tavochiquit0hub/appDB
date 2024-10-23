import requests

class GetRecord:
    __url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    # Función para obtener el último registro desde la API
    def get_last_record(self):
        try:
            response = requests.get(self.__url)
            response.raise_for_status()  # Verifica si hubo un error en la solicitud
            data = response.json()

            # Obtiene el último registro
            if data:
                return data[-1]  # Devuelve el último registro
            else:
                return None  # Si no hay registros
        except Exception as e:
            print(f"Error: {e}")  # Manejo de errores
            return None  # Devuelve None en caso de error
