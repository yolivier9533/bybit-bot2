import requests
import time
import hmac
import hashlib

# ====== CONFIGURATION ======
API_KEY = "bg_efce6c9c994335ade6edcb632cdc43d3"
API_SECRET = "513c544ad212d7a002549769f42cee2bda5baa11fb41dc520cdf22e8989cdad6"
PASS_PHRASE = "grouchym"
BASE_URL = "https://api.bitget.com"

# ===== SIGNATURE =====
def generate_signature(api_key, api_secret, params):
    sorted_params = sorted(params.items())
    query_string = "&".join([f"{k}={v}" for k, v in sorted_params])
    sign = hmac.new(
        bytes(api_secret, 'utf-8'),
        bytes(query_string, 'utf-8'),
        hashlib.sha256
    ).hexdigest()
    return sign

# ===== TEST : Vérifier les positions ouvertes =====
def check_open_position():
    endpoint = "/api/mix/v1/position"  # endpoint corrigé pour récupérer les positions futures
    url = BASE_URL + endpoint

    timestamp = str(int(time.time() * 1000))
    params = {
        "apiKey": API_KEY,
        "timestamp": timestamp,
        "passphrase": PASS_PHRASE
    }

    # Générer la signature
    sign = generate_signature(API_KEY, API_SECRET, params)
    params["sign"] = sign

    headers = {
        "X-BYBIT-API-KEY": API_KEY,
        "X-BYBIT-API-SIGN": sign,
        "X-BYBIT-API-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)
    print("HTTP Status Code:", response.status_code)
    try:
        print("Response:", response.json())
    except ValueError:
        print("Error: Unable to decode JSON response.")
        print("Response text:", response.text)

# ===== LANCEMENT =====
print("🔄 Vérification de la position sur Bitget...")
check_open_position()
