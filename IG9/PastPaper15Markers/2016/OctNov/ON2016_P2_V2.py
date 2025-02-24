#
# You will need to complete these three tasks. Each task must be fully tested.
#
# TASK 1 – Set up the donation system
#
# Set up a routine that allows:
#     • the names of three charities to be input and stored
#     • the charity names to be displayed with a number (1, 2 or 3) beside each name
#     • a choice of 1, 2 or 3 to be entered to choose the charity, all other entries rejected
#     • the value of a customer’s shopping bill to be entered
#     • the donation to be calculated
#     • three totals to be set to zero ready to total each charity donation
#
# TASK 2 – Record and total each donation
#
# For a customer’s shopping bill:
#     • input a charity choice of 1, 2 or 3
#     • input the value of a customer’s shopping bill
#     • calculate the donation
#     • add the donation to the appropriate total
# Output the name of the charity and the amount donated.
#
# TASK 3 – Show the totals so far
# Extend TASK 2 to accept:
#     • donations from more customers
#     • a charity choice of -1 to show the totals so far
# Display the charities’ names and the totals in descending order of totals.
# Calculate a grand total of all three totals.
# Output ‘GRAND TOTAL DONATED TO CHARITY’ and the amount of the grand total.

def isnum(inp):
    try:
        float(inp)
        return True
    except ValueError as ve:
        print(ve)
        return False


def isbool(inp):
    try:
        bool(inp)
        return True
    except ValueError as ve:
        print(ve)
        return False


if __name__ == '__main__':
    max_donations_index = 0
    charities = ["A", "B", "C"]
    donations = [0, 0, 0]
    chosen_charity = None
    more_customers = True
    shopping_bill = 0.0
    c1_donated_total = 0.0
    c2_donated_total = 0.0
    c3_donated_total = 0.0
    grand_total_donated = c1_donated_total + c2_donated_total + c3_donated_total
    print(f"You have 3 charities to choose from,")
    print(f"Enter 1 to opt for {charities[0]}.")
    print(f"Enter 2 to opt for {charities[1]}.")
    print(f"Enter 3 to opt for {charities[2]}.")
    print("Enter -1 to show grand total donated.")

    # Task 1, Giving the user to opt for any of 3 charities

    while more_customers is True:
        more_customer = input("Do you wish to accept donations from more customers? (True/False)")
        if isbool(more_customer) is False:
            print("Invalid input")
        else:
            more_customer = bool(more_customer)
            if more_customer is False:
                break
            else:
                chosen_charity = input("Enter your chosen charity. 1, 2, or 3. ")
                chosen_charity = chosen_charity.strip(" ")
                if chosen_charity == "1":
                    shopping_bill = input("Enter the value of your shopping bill. ")
                    if isnum(shopping_bill) is True:
                        shopping_bill = float(shopping_bill)
                        donation = shopping_bill / 100
                        c1_donated_total = c1_donated_total + donation
                        donations[0] = c1_donated_total
                        # Finding the grand total donated, and the total amount donated to charity 1 when the user
                        # chooses to donate to charity 1 Task 1 and Task 2
                    else:
                        print("Invalid input.")
                elif chosen_charity == "2":
                    shopping_bill = input("Enter the value of your shopping bill. ")
                    if isnum(shopping_bill) is True:
                        shopping_bill = float(shopping_bill)
                        donation = shopping_bill / 100
                        c2_donated_total = c2_donated_total + donation
                        donations[1] = c2_donated_total
                        # Finding the grand total donated, and the total amount donated to charity 2 when the user
                        # chooses to donate to charity 2 Task 1 and Task 2
                    else:
                        print("Invalid input.")
                elif chosen_charity == "3":
                    shopping_bill = input("Enter the value of your shopping bill. ")
                    if isnum(shopping_bill) is True:
                        shopping_bill = float(shopping_bill)
                        donation = shopping_bill / 100
                        c3_donated_total = c3_donated_total + donation
                        donations[2] = c3_donated_total
                        # Finding the grand total donated, and the total amount donated to charity 3 when the user
                        # chooses to donate to charity 3 Task 1 and Task 2
                    else:
                        print("Invalid input.")
                elif chosen_charity == "-1":
                    while len(charities) > 0:
                        for i in range(3):
                            if donations[i] > donations[max_donations_index]:
                                max_donations_index = i
                        if len(charities) == 3:
                            print(f"The charity with the greatest donation value is {charities[max_donations_index]}, "
                                  f"raising ${donations[max_donations_index]}")
                            charities.remove(charities[max_donations_index])
                            donations.remove(donations[max_donations_index])
                        if len(charities) == 2:
                            print(
                                f"The charity with the second-greatest donation value is {charities[max_donations_index]}, "
                                f"raising ${donations[max_donations_index]}")
                            charities.remove(charities[max_donations_index])
                            donations.remove(donations[max_donations_index])
                        if len(charities) == 1:
                            print(f"The charity with the least donation value is {charities[0]}"
                                  f"raising ${donations[0]}")
                            charities.remove(charities[max_donations_index])
                            donations.remove(donations[max_donations_index])
                    grand_total_donated = c1_donated_total + c2_donated_total + c3_donated_total
                    print(f"GRAND TOTAL DONATED TO CHARITY: ${grand_total_donated}")
                    # Task 3

                else:
                    print("Invalid input. Please re-enter.")
