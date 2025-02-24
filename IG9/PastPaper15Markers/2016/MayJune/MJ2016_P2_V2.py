# TASK 1 – Check the contents and weight of a single sack

# Each sack must obey the following rules to be accepted:
# • contain cement, gravel or sand, with a letter on the side for easy identification
#   o C - cement
#   o G - gravel
#   o S - sand
#   • sand or gravel must weigh over 49.9 and under 50.1 kilograms
#   • cement must weigh over 24.9 and under 25.1 kilograms
# Input and store the weight and contents for one sack. The contents must be checked and an incorrect
# sack rejected. The weight must be validated on entry and an overweight or underweight sack rejected.
# Output the contents and weight of an accepted sack. If a sack is rejected, output the reason(s).

# TASK 2 – Check a customer’s order for delivery

# Input and store the number of sacks of each type required for the order. Use TASK 1 to check the
# contents and weight of each sack. Ensure that the delivery contains the correct number and type of
# sacks for the order.
# Output the total weight of the order.
# Output the number of sacks rejected from the order.

# TASK 3 – Calculate the price for a customer’s order

# Extend TASK 2 to calculate a price for an order. Prices for the sacks are as follows:
# • regular price for each sack
#   o cement, $3
#   o gravel, $2
#   o sand, $2
# Calculate and output the regular price for the order. Check how many special packs are in the order. If
# a discount price applies then output the new price for the order and the amount saved.
def isnum(inp):
    try:
        int(inp)
        return True
    except ValueError as ve:
        print(ve)
        return False


def isfloat(inp):
    try:
        float(inp)
        return True
    except ValueError as ve:
        print(ve)
        return False


def validate_sack(content, side_letter, weight):  # Task 1, Validating the bags
    reject_sacks = 0
    total_weight = 0
    content = content.strip(" ")
    content = content.lower()
    side_letter = side_letter.strip("")
    side_letter = side_letter.lower()

    if side_letter == "c" and content == "cement":
        if 24.9 < weight < 25.1:
            total_weight = total_weight + weight
            return True
        if weight > 25.1:
            print("Sack is overweight. Rejected.")
            reject_sacks += 1
            return False
        if weight < 24.9:
            print("Sack is underweight. Rejected.")
            reject_sacks += 1
            return False
    elif side_letter != "c" and content == "cement":
        if weight > 25.1:
            print("Sack is overweight and side letter is inaccurate. Rejected.")
            reject_sacks += 1
            return False
        if weight < 24.9:
            print("Sack is underweight and side letter is inaccurate. Rejected.")
            reject_sacks += 1
            return False
        else:
            print("Side letter is inaccurate. Rejected")
            reject_sacks += 1
            return False

    # Validating the bags of cement

    elif side_letter == "s" and content == "sand":
        if 49.9 < weight < 50.1:
            total_weight = total_weight + weight
            return True
        if weight > 50.1:
            print("Sack is overweight. Rejected.")
            reject_sacks += 1
            return False
        if weight < 49.9:
            print("Sack is underweight. Rejected.")
            reject_sacks += 1
            return False
    elif side_letter != "s" and content == "sand":
        if weight > 50.1:
            print("Sack is overweight and side letter is inaccurate. Rejected.")
            reject_sacks += 1
            return False
        if weight < 49.9:
            print("Sack is underweight and side letter is inaccurate. Rejected.")
            reject_sacks += 1
            return False
        else:
            print("Side letter is inaccurate. Rejected")
            reject_sacks += 1
            return False

    # Validating the bags of sand

    elif side_letter == "g" and content == "gravel":
        if 49.9 < weight < 50.1:
            total_weight = total_weight + weight
            return True
        if weight > 50.1:
            print("Sack is overweight. Rejected.")
            reject_sacks += 1
            return False
        if weight < 49.9:
            print("Sack is underweight. Rejected.")
            reject_sacks += 1
            return False
    elif side_letter != "g" and content == "gravel":
        if weight > 50.1:
            print("Sack is overweight and side letter is inaccurate. Rejected.")
            reject_sacks += 1
            return False
        if weight < 49.9:
            print("Sack is underweight and side letter is inaccurate. Rejected.")
            reject_sacks += 1
            return False
        else:
            print("Side letter is inaccurate. Rejected")
            reject_sacks += 1
            return False
    print(f"Total number of sacks rejected is {reject_sacks}")
    print(f"The total weight of all the sacks is {total_weight}")
    # Validating the bags of gravel


def price(sack_type, quantity):
    cost = 0
    sack_type = sack_type.strip(" ")
    sack_type = sack_type.lower()

    if sack_type == "c":
        cost = cost + (quantity * 3)
    if sack_type == "s":
        cost = cost + (quantity * 2)
    if sack_type == "g":
        cost = cost + (quantity * 2)
    return cost
    # Calculating the price, a part of Task 3


if __name__ == "__main__":
    total_qty = 0
    sacktypes = ["C", "S", "G"]
    sackqtys = [0, 0, 0]
    input_order = None
    cement_index = sacktypes.index("C")
    sand_index = sacktypes.index("S")
    gravel_index = sacktypes.index("G")
    while input_order != "-1":
        print("Place your order for the sacks needed")
        print("C for cement")
        print("S for sand")
        print("G for gravel")

        input_order = input("Enter the type of sack needed, followed by the quantity. (EXAMPLE: C-5) ")
        # order = order.strip(" ")
        order = input_order.split("-")
        if input_order == '-1':
            print("Thank you for the order!")
        elif len(order) == 2:
            order[0] = order[0].strip()
            order[1] = order[1].strip()
            if isnum(order[1]) is True:
                if order[0] == sacktypes[0]:
                    sackqtys[0] = sackqtys[0] + 1
                if order[1] == sacktypes[1]:
                    sackqtys[1] = sackqtys[1] + 1
                if order[1] == sacktypes[2]:
                    sackqtys[2] = sackqtys[2] + 1
        else:
            print("Invalid entry.")

    for i in range(len(sackqtys)):
        total_qty = total_qty + sackqtys[i]

    for i in range(sackqtys[0]):
        sack_weight = input(f"Enter the weight of cement sack {i + 1} in kilograms. ")
        if isfloat(sack_weight) is True:
            sack_weight = float(sack_weight)
        sideletter = input(f"Enter the side letter of cement sack {i + 1}. ")
        validate_sack(content="cement", side_letter=sideletter, weight=sack_weight)
    for i in range(sackqtys[1]):
        sack_weight = input(f"Enter the weight of sand sack {i + 1} in kilograms. ")
        if isfloat(sack_weight) is True:
            sack_weight = float(sack_weight)
        sideletter = input(f"Enter the side letter of sand sack {i + 1}. ")
        validate_sack(content="sand", side_letter=sideletter, weight=sack_weight)
    for i in range(sackqtys[2]):
        sack_weight = input(f"Enter the weight of gravel sack {i + 1} in kilograms. ")
        if isfloat(sack_weight) is True:
            sack_weight = float(sack_weight)
        sideletter = input(f"Enter the side letter of gravel sack {i + 1}. ")
        validate_sack(content="gravel", side_letter=sideletter, weight=sack_weight)

    # Validating the sacks of sand, a part of Task 1
grand_total = 0

for i in range(len(sackqtys)):
    if sackqtys[i] == 0:
        pass
    grand_total = grand_total + price(sack_type=sacktypes[i], quantity=sackqtys[i])
    print(f"The grand total cost of all the sacks is ${grand_total}")


