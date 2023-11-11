# import requests

import time
from libs.openexchange import OpenExchangeClient

APP_ID = "f22570d23cf440adbcbc1eca8edcfaee"
# ENDPOINT = "https://openexchangerates.org/api/latest.json"
#
# response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")
# exchange_rates = response.json()["rates"]

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
start = time.time()

# gbp_amount = usd_amount * exchange_rates["GBP"]
gbp_amount = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)

print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")