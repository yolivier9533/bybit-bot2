import time
import hmac
import hashlib
import base64
import requests

# API Key, Secret Key et Passphrase
API_KEY = 'bg_efce6c9c994335ade6edcb632cdc43d3'
SECRET_KEY = '513c544ad212d7a002549769f42cee2bda5baa11fb41dc520cdf22e8989cdad6'
PASSPHRASE = 'grouchym'

# Fonction pour obtenir le timestamp en millisecondes
def get_timestamp():
    return str(int(time.time() * 1000))

# Fonction pour générer la signature
def generate_signature(timestamp, method, request_path, body=''):
    payload = f"{timestamp}{method.upper()}{request_path}{body}"
    return hmac.new(SECRET_KEY.encode(), payload.encode(), hashlib.sha256).hexdigest()

# Fonction pour vérifier si une position est ouverte
def check_open_position():
    url = "https://api.bitget.com"  # Base URL
    request_path = "/api/v2/mix/position"  # Endpoint V2 pour vérifier les positions ouvertes

    timestamp = get_timestamp()
    method = "GET"  # Méthode GET
    signature = generate_signature(timestamp, method, request_path)

    headers = {
        'ACCESS-KEY': API_KEY,
        'ACCESS-SIGN': signature,
        'ACCESS-TIMESTAMP': timestamp,
        'ACCESS-PASSPHRASE': PASSPHRASE,
        'Content-Type': 'application/json'
    }

    # Effectuer la requête
    response = requests.get(f"{url}{request_path}", headers=headers)

    # Afficher la réponse
    print("HTTP Status Code:", response.status_code)
    print("Response Text:", response.text)

# Test de la fonction
check_open_position()


