"""
==============================================================================
                         STOCK PORTFOLIO TRACKER
==============================================================================

Project : Stock Portfolio Tracker
Author  : Muhammad Ali Haider
Language: Python

Description:
------------
This is a console-based Stock Portfolio Tracker that allows users to build
a simple stock portfolio using predefined stock prices. Users can purchase
multiple stocks, calculate their total investment, and generate a formatted
portfolio report saved as a text file.

Features:
---------
- Displays available stocks and their prices
- Accepts multiple stock purchases
- Validates stock names and quantity input
- Updates quantity for duplicate stock purchases
- Calculates individual and total investment
- Generates a formatted portfolio report
- Saves the report as a .txt file
- Includes current date and time in the report

Key Concepts Used:
------------------
- Dictionary
- Loops
- Conditional Statements
- Input Validation
- Arithmetic Operations
- File Handling
- Date and Time Module

==============================================================================
"""

from datetime import datetime

# Dictionary containing stock symbols and their prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 450,
    "AMZN": 200
}

# Display available stocks
print("\nAvailable Stocks\n")
for char in stock_prices:

    print("\t", char, end="\t:   ")
    print("\t", stock_prices[char], "$")

# Stores the total investment value
total_investment = 0

# Dictionary to store purchased stocks and their quantities
portfolio = {}

# Main program loop
while True:

    # Take stock name as input
    stock = input("\nEnter Stock Name: ").upper()

    # Validate stock name input
    if stock.isalpha():

        # Check if the stock exists
        if stock in stock_prices:

            # Quantity input loop
            while True:

                quantity = input("\nEnter Quantity: ")

                # Validate quantity input
                if quantity.isdigit():

                    quantity = int(quantity)

                    # Update quantity if stock already exists
                    if stock in portfolio:
                        portfolio[stock] += quantity

                    # Otherwise add the stock to portfolio
                    else:
                        portfolio[stock] = quantity

                    # Calculate investment for current purchase
                    investment = stock_prices[stock] * quantity

                    # Update total investment
                    total_investment += investment

                    add_another = False

                    # Ask user whether to continue
                    while True:

                        choice = input("\nDo you want to enter another stock (Y/N): ").upper()
                        print("\n")

                        # Continue adding stocks
                        if choice == "Y":
                            add_another = True
                            break

                        # Generate report and exit
                        elif choice == "N":

                            with open("Stock-Portfolio-Tracker.txt", "w") as file:

                                # Report title
                                file.write("=" * 67 + "\n")
                                file.write(f"{'Stock Portfolio Tracker':^67}\n")
                                file.write("=" * 67 + "\n\n")

                                # Get current date and time
                                now = datetime.now()

                                date_str = now.strftime("%B %d, %Y")
                                hour_min = now.strftime("%I:%M")

                                # Remove leading zero from hour
                                if hour_min.startswith("0"):
                                    hour_min = hour_min[1:]

                                # Format AM/PM
                                am_pm_raw = now.strftime("%p").lower()
                                am_pm_formatted = f"{am_pm_raw[0]}.{am_pm_raw[1]}"

                                # Write date and time
                                file.write(
                                    f"{'Date: ' + date_str:<33}"
                                    f"{'Time: ' + hour_min + am_pm_formatted:>25}\n\n"
                                )

                                # Table header
                                file.write("-" * 67 + "\n")
                                file.write(
                                    f"{'Stock':^15}"
                                    f"{'Price ($)':^15}"
                                    f"{'Quantity':^15}"
                                    f"{'Investment ($)':^20}\n"
                                )
                                file.write("-" * 67 + "\n")

                                # Write portfolio details
                                for char in portfolio:

                                    file.write(
                                        f"{char:^15}"
                                        f"{stock_prices[char]:^15}"
                                        f"{portfolio[char]:^15}"
                                        f"{stock_prices[char] * portfolio[char]:^20}\n"
                                    )

                                # Write total investment
                                file.write("-" * 67 + "\n")
                                file.write(
                                    f"\n{'Total Investment = ' + str(total_investment) + ' $':^67}\n\n"
                                )

                                # Footer
                                file.write("=" * 67 + "\n")
                                file.write(
                                    f"{'Thank You for Using Stock Portfolio Tracker':^67}\n"
                                )
                                file.write("=" * 67)

                                print("Stock-Portfolio-Tracker.txt has been created successfully.")
                                print("Thank you for using Stock Portfolio Tracker!")
                                exit()

                        # Handle invalid Y/N input
                        else:
                            print("Invalid Input! Please enter Y or N.")

                    # Break quantity loop if user wants another stock
                    if add_another:
                        break

                # Handle invalid quantity input
                else:
                    print("\nPlease enter digits (0-9).")
                    continue

        # Handle invalid stock name
        else:
            print("\n")
            print("Stock not Found!\nEnter a valid stock name.")

    # Handle invalid alphabet input
    else:
        print("\nPlease enter alphabets (A-Z/a-z).")
        continue