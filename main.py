import time
import hashlib
import hmac
import requests
import base64

# Ton API Key, Secret Key, et Passphrase
api_key = 'bg_efce6c9c994335ade6edcb632cdc43d3'
api_secret = '513c544ad212d7a002549769f42cee2bda5baa11fb41dc520cdf22e8989cdad6'
passphrase = 'grouchym'

# Fonction pour obtenir le timestamp en millisecondes
def get_timestamp():
    return str(int(time.time() * 1000))

# Fonction pour générer la signature
def generate_signature(timestamp, method, request_path, body=''):
    query_string = ''
    if body:
        body = str(body)
    payload = f"{timestamp}{method.upper()}{request_path}{query_string}{body}"
    signature = hmac.new(api_secret.encode(), payload.encode(), hashlib.sha256).hexdigest()
    return signature

# Fonction pour vérifier la position ouverte
def check_open_position():
    url = "https://api.bitget.com/api/v2/mix/position"  # Utilisation de l'endpoint V2

    timestamp = get_timestamp()
    method = "GET"
    request_path = "/api/v2/mix/position"

    # Générer la signature
    signature = generate_signature(timestamp, method, request_path)

    headers = {
        'ACCESS-KEY': api_key,
        'ACCESS-SIGN': signature,
        'ACCESS-TIMESTAMP': timestamp,
        'ACCESS-PASSPHRASE': passphrase,
        'Content-Type': 'application/json'
    }

    # Effectuer la requête GET
    response = requests.get(url + request_path, headers=headers)

    if response.status_code == 200:
        print("Position ouverte trouvée ! Voici les détails : ", response.json())
    else:
        print("Erreur : ", response.status_code)
        print("Message d'erreur : ", response.text)

# Tester la fonction
check_open_position()
