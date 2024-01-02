# ---------------------------------
# Programmer: Michael Barreto
# Course:     COSC 1315 Section 10
# Assignment: Tax Determiner
# ---------------------------------

# Declare 'constants' to be used in program

STATE_TAX_RATE = .0825
COUNTY_TAX_RATE = .025

# main
def main():
    # Prompt the user for the purchased amount
    purchase = float(input("Enter the purchase amount: "))

    # Calculate the state tax
    stateTax = purchase * STATE_TAX_RATE

    # Calculate the county tax
    countyTax = purchase * COUNTY_TAX_RATE

    # Call the function 'showSale'
    showSale(purchase, stateTax, countyTax)

    print("\nThis program was written by Michael Barreto.")
    print("End of program.")

# Define the function 'showSale'. It will accept
# 'purchase', 'stateTax', and 'countyTax'
def showSale(purchase, stateTax, countyTax):
    # Calculate the total tax and the total sale
    totalTax = stateTax + countyTax
    totalSale = purchase + totalTax

    # Print out information about the
    # Purchased amount and all the taxes
    print("\nPurchase amount: $", format(purchase, '.2f'), "\n")
    print("State tax: $", format(stateTax, '.2f'))
    print("County tax: $", format(countyTax, '.2f'))
    print("Total tax: $", format(totalTax, '.2f'))
    print("\nTotal sale: $", format(totalSale, '.2f'))

# Call the main function
main()
