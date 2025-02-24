# TASK 1 – Check the size and weight of a single parcel
import math


# Each parcel must obey the following rules to be accepted for delivery:
#   • each dimension must be no more than 80 cm
#   • the sum of the three dimensions must be no more than 200 cm
#   • the weight of the parcel must be between one and ten kilograms inclusive
# Input and store the weight and dimensions for one parcel.
# All the dimensions and the weight must be validated on entry and an unsuitable parcel rejected.
# Output if the parcel is accepted or rejected. If rejected, output all the reasons why the parcel was
# rejected.

# TASK 2 – Check a customer’s consignment of parcels

# Input and store the number of parcels in the consignment. Calculate the number of parcels accepted
# and the total weight of the parcels accepted. For each parcel that was rejected, output all the
# reasons why that parcel was rejected.
# Output the number of parcels accepted and the total weight of parcels accepted.
# Output the number of parcels rejected.

# TASK 3 – Calculate the price for a customer’s consignment of parcels

# Extend TASK 2 to also calculate the price for each parcel, using the following rules:
#   • 1 kg to 5 kg inclusive costs $10
#   • Each 100 grams over 5 kg, up to 10 kg, costs an extra $0.10
# Your output should also include the price for each parcel accepted and the total price of the consignment.

def isnum(inp):
    try:
        float(inp)
        return True
    except ValueError as ve:
        print(ve)
        return False


def valid_parcel(length, breadth, height, weight):
    dimension_sum = length + breadth + height

    if ((length <= 80) and (breadth <= 80) and (height <= 80)) and (dimension_sum <= 200) and (1 <= weight <= 10):
        return True
    else:
        if length > 80:
            print(
                "Since the length of the parcel is greater than 80cm, it does not meet the requirements, "
                "hence rejected.")
            return False
        if breadth > 80:
            print(
                "Since the breadth of the parcel is greater than 80cm, it does not meet the requirements, "
                "hence rejected.")
            return False
        if height > 80:
            print(
                "Since the height of the parcel is greater than 80cm, it does not meet the requirements, "
                "hence rejected.")
            return False
        if dimension_sum > 200:
            print(
                "Since the sum of all 3 dimensions is greater than 200, it does not meet the requirements, "
                "hence rejected.")
            return False
        if weight < 1:
            print(
                "Since the weight of the parcel is less than 1 kilogram, it does not meet the requirements, "
                "hence rejected.")
            return False
        if weight > 10:
            print(
                "Since the weight of the parcel is greater than 10 kilograms, it does not meet the requirements, "
                "hence rejected.")
            return False

    # Procedure for validating all the parcels
    # Task 1


def parcel_cost(weight):
    temp_weight = 0
    cost = 10
    if 1 <= weight <= 5:
        print(f"The total cost of your parcel is ${cost}")
    if 5 < weight <= 10:
        temp_weight_grams = (weight - 5) * 1000
        extra_weight_slab = int(temp_weight_grams / 100)
        fractional_weight = temp_weight_grams % 100
        if fractional_weight > 0:
            extra_weight_slab = extra_weight_slab + 1
        temp_weight_cost = extra_weight_slab * 0.1
        cost = cost + temp_weight_cost
        print(f"The total cost of your parcel is ${cost}")


# Calculating the cost of the parcel, TASK 3

if __name__ == "__main__":
    lengths = []
    breadths = []
    heights = []
    weights = []
    rejected_parcels = 0
    accepted_parcels = 0
    total_parcel_weight = 0
    valid_values = None
    parcel_detail = ""

    while parcel_detail != "-1":
        parcel_detail = input(
            "Enter the length(cm),breadth(cm),height(cm),weight(kg) (Ex: 5, 20, 7, 5): "
            # "Enter the length, breadth, height in centimetres and weight of the parcel in kilograms, comma seperated."
            "Enter -1 to cancel.")
        parcel_detail = parcel_detail.split(",")
        if len(parcel_detail) != 4:
            print("Invalid input")
        if len(parcel_detail) == 4:
            for i in range(4):
                parcel_detail[i] = parcel_detail[i].strip(" ")
                if isnum(parcel_detail[i]) is False:
                    valid_values = False  # Checking if the entered values are correct or not
                    print("Invalid details. Please Re-enter.")
                else:
                    parcel_detail[i] = float(parcel_detail[i])
                # Converting all the values to float format

            lengths.append(parcel_detail[0])
            breadths.append(parcel_detail[1])
            heights.append(parcel_detail[2])
            weights.append(parcel_detail[3])
            # Adding all the values to their respective arrays

            validparcel = valid_parcel(length=parcel_detail[0], breadth=parcel_detail[1],
                                       height=parcel_detail[2], weight=parcel_detail[3])
            if validparcel is True:
                accepted_parcels += 1  # Counting the total number of accepted parcels
                total_parcel_weight = total_parcel_weight + parcel_detail[3]
                # Counting the weight of the total number of accepted parcels
            if validparcel is False:
                rejected_parcels += 1  # Counting the total number of rejected parcels
            # Task 2
            parcel_cost(weight=parcel_detail[3])
            # Printing the cost of the parcel

    print(f"The total number of parcels accepted is {accepted_parcels} weighing a total of {total_parcel_weight}kg.")
    print(f"The total number of rejected parcels is {rejected_parcels}.")
