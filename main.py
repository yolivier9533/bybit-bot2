import requests
import time
import hmac
import hashlib

API_KEY = "TA_NOUVELLE_CLE"
API_SECRET = "TON_NOUVEAU_SECRET"
BASE_URL = "https://api.bybit.com"

def generate_signature(params, secret):
    sorted_params = sorted(params.items())
    query_string = "&".join([f"{k}={v}" for k, v in sorted_params])
    return hmac.new(
        bytes(secret, "utf-8"),
        bytes(query_string, "utf-8"),
        hashlib.sha256
    ).hexdigest(), query_string

def get_wallet_balance():
    endpoint = "/v5/account/wallet-balance"
    url = BASE_URL + endpoint

    timestamp = str(int(time.time() * 1000))
    params = {
        "apiKey": API_KEY,
        "timestamp": timestamp,
        "accountType": "UNIFIED"
    }

    signature, query_string = generate_signature(params, API_SECRET)

    headers = {
        "X-BYBIT-API-KEY": API_KEY,
        "X-BYBIT-API-SIGN": signature,
        "X-BYBIT-API-TIMESTAMP": timestamp,
        "Content-Type": "application/json"
    }

    final_url = f"{url}?{query_string}&sign={signature}"

    print("🔍 URL signée :", final_url)
    print("🔍 Headers :", headers)

    response = requests.get(url, params=params, headers=headers)

    print("🔥 Code HTTP :", response.status_code)
    print("🔥 Contenu brut :", response.text)

    return response.text

print("🔄 Connexion à Bybit...")
result = get_wallet_balance()
print("📊 Résultat brut :", result)
