import json
import update_dollar as update

# This function updates the dollar value in the `dollar_value.json` file.


def update_dollar():

    with open("dollar_value.json") as f:
        data = json.load(f)

    new_value = round(update.get(), 2)

    data["dollar_value"] = new_value

    with open("dollar_value.json", "w") as f:
        json.dump(data, f, indent=2)


# This function gets the dollar value from the `dollar_value.json` file.
def get_dollar_value():

    with open("dollar_value.json") as f:
        data = json.load(f)

    value = data["dollar_value"]
    return value


# This function converts a currency amount from Bolivars to Dollars and vice versa.
def convert_currency(amount, dollar_value):

    dollar_to_bolivar = float(amount / dollar_value)

    bolivar_to_dollar = float(dollar_value * amount)

    # This line returns a formatted string with the converted currency amounts.
    return f"""D: {dollar_value}bs\nB to D: {dollar_to_bolivar}\nD to B: {bolivar_to_dollar}"""


# This function replaces commas in a string with empty spaces.
def replace_commas(text):

    return text.replace(',', '')
