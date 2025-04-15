import requests
import time
import hmac
import hashlib

# Nom du bot : BotAutoTP-Bitget
API_KEY = "bg_2f8ab665057c20f46e514e4e6415e105"
API_SECRET = "66518bd5ac20fcc95e58ea2f4d2daefef0f57a5bc7eae26d9258330780b5a179"
PASS_PHRASE = "grouchym"  # Passphrase si nécessaire
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

# Fonction pour récupérer les ordres ouverts
def get_open_orders():
    endpoint = "/api/v1/order/open"  # Pour voir les ordres ouverts
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
result = get_open_orders()
print("📊 Résultat brut :", result)
