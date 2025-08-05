import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

def add_device(device_data):
    response = requests.post(BASE_URL, json=device_data)
    return response

def list_devices():
    response = requests.get(BASE_URL)
    return response

def update_device(device_id, updated_data):
    # Usamos httpbin para PUT para evitar 503
    url = "https://httpbin.org/put"
    response = requests.put(url, json=updated_data)
    return response

def delete_device(device_id):
    # Usamos httpbin para DELETE para evitar 503
    url = "https://httpbin.org/delete"
    response = requests.delete(url)
    return response

if __name__ == "__main__":
    new_device = {"title": "Switch-01", "body": "Network Switch", "userId": 1}
    update_data = {"title": "Switch-01-Upgraded", "body": "Core Switch", "userId": 1}

    print("Agregar dispositivo:", add_device(new_device).json())
    print("Listar dispositivos:", list_devices().json()[:3])
    print("Actualizar dispositivo (PUT):", update_device(1, update_data).json())
    print("Eliminar dispositivo (DELETE):", delete_device(1).status_code)
