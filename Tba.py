import requests

# URL login TibiaME (Harus dicek dengan sniffer apakah ada endpoint tertentu)
LOGIN_URL = "https://static.tibiame.com/login"

def login_tibiame(username, password, world):
    data = {
        "username": username,
        "password": password,
        "world": world
    }

    session = requests.Session()
    response = session.post(LOGIN_URL, data=data)

    if "success" in response.text.lower():
        print("Login berhasil!")
        return session  # Simpan sesi jika ingin lanjut ke fitur lain
    else:
        print("Login gagal!")
        return None

# Input manual
user = input("Username: ")
passwd = input("Password: ")
world = input("World: ")

session = login_tibiame(user, passwd, world)
