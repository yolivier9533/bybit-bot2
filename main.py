import time
import hmac
import hashlib
import base64
import requests
import json

# Paramètres API
API_KEY = 'bg_efce6c9c994335ade6edcb632cdc43d3'  # Remplace avec ta clé API
SECRET_KEY = '513c544ad212d7a002549769f42cee2bda5baa11fb41dc520cdf22e8989cdad6'  # Remplace avec ton Secret Key
PASSPHRASE = 'grouchym'  # Remplace avec ta passphrase

# URL de l'API
API_URL = "https://api.bitget.com"

# Fonction pour générer la signature
def generate_signature(timestamp, method, request_path, body=""):
    signature_content = f"{timestamp}{method}{request_path}{body}"
    signature = hmac.new(SECRET_KEY.encode(), signature_content.encode(), hashlib.sha256).digest()
    return base64.b64encode(signature).decode()

# Fonction pour vérifier s'il y a un trade en cours
def check_open_position():
    # Récupérer le timestamp actuel
    timestamp = str(int(time.time() * 1000))

    # Chemin de l'API pour vérifier les positions en cours
    request_path = "/api/v2/mix/position"
    method = "GET"
    
    # Générer la signature
    signature = generate_signature(timestamp, method, request_path)

    # En-têtes HTTP nécessaires
    headers = {
        'ACCESS-KEY': API_KEY,
        'ACCESS-SIGN': signature,
        'ACCESS-TIMESTAMP': timestamp,
        'ACCESS-PASSPHRASE': PASSPHRASE,
        'Content-Type': 'application/json'
    }

    # Faire la requête
    response = requests.get(f"{API_URL}{request_path}", headers=headers)
    
    # Vérification du code de réponse
    if response.status_code == 200:
        print("Trade en cours :", response.json())
    else:
        print("Erreur :", response.status_code, response.text)

# Appeler la fonction pour vérifier les positions
check_open_position()
