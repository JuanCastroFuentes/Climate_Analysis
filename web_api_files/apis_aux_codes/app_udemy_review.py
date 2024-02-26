from libs.openexchange import OpenExchangeClient
import requests

APP_ID = "a6f3de885eb847b795bd980d06e2873f"

client = OpenExchangeClient(APP_ID)

#ENDPOINT = "http://openexchangerates.org/api/latest.json"

#response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
#exchange_rates=response.json()["rates"]

usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD","GBP")

print(f"USD {usd_amount} is GBP {gbp_amount}")

