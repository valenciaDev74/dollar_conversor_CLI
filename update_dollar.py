import requests

# This line makes a GET request to the PydolarVenezuela API.
response = requests.get(
    "https://pydolarvenezuela-api.vercel.app/api/v1/dollar/dolar_promedio")


# This function gets the average price of the dollar from the JSON response.
def get_average_price(json_data):

    prices = []
    for currency in json_data:
        prices.append(float(json_data[currency]["price"]))

    return sum(prices) / len(prices)


# This function gets the average price of the dollar and returns it.
def get():
    body = response.json()
    return get_average_price(body)
