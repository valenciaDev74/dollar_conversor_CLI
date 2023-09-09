import sys
import functions as f


# This function is the main entry point for the program.
def main():

    # This line gets the amount from the command line arguments.
    amount = sys.argv[1]

    # This if statement checks if the user wants to update the dollar value.
    if sys.argv[1] == 'upd':
        f.update_dollar()
    else:

        # This try-except block tries to convert the amount to a float.
        try:
            amount = float(f.replace_commas(sys.argv[1]))
        except (ValueError, TypeError):
            print('Invalid value')
            exit()

        # This line gets the dollar value from the `functions` module.
        dollar_value = f.get_dollar_value()

        # This line prints the converted currency.
        print(f.convert_currency(amount, dollar_value))


# This if statement ensures that the code is only executed when the file is run as a script.
if __name__ == "__main__":
    main()
