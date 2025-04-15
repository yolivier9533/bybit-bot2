import requests
import time
import hmac
import hashlib

# Bitget API keys
API_KEY = "bg_2f8ab665057c20f46e514e4e6415e105"
API_SECRET = "66518bd5ac20fcc95e58ea2f4d2daefef0f57a5bc7eae26d9258330780b5a179"
PASS_PHRASE = "grouchym"
BASE_URL = "https://api.bitget.com"

# Fonction pour générer la signature
def generate_signature(params, secret):
    sorted_params = sorted(params.items())
    query_string = "&".join([f"{k}={v}" for k, v in sorted_params])
    return hmac.new(
        bytes(secret, "utf-8"),
        bytes(query_string, "utf-8"),
        hashlib.sha256
    ).hexdigest()

# Fonction pour récupérer le solde (ou d'autres infos)
def get_wallet_info():
    endpoint = "/api/v1/account/asset"  # Endpoint pour les infos sur les actifs
    url = BASE_URL + endpoint

    timestamp = str(int(time.time() * 1000))
    params = {
        "apiKey": API_KEY,
        "timestamp": timestamp,
    }

    signature = generate_signature(params, API_SECRET)

    headers = {
        "X-BYBIT-API-KEY": API_KEY,
        "X-BYBIT-API-SIGN": signature,
        "X-BYBIT-API-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }

    response = requests.get(url, params=params, headers=headers)

    print("🔥 Code HTTP :", response.status_code)
    print("🔥 Contenu brut :", response.text)

    return response.text

print("🔄 Connexion à Bitget...")
result = get_wallet_info()
print("📊 Résultat brut :", result)
