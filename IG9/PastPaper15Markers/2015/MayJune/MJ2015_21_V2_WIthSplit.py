# Write and test a program to complete the three tasks.
#
# TASK 1
#
# A school keeps records of the weights of each pupil. The weight, in kilograms, of each pupil is
# recorded on the first day of term.
# Input and store the weights and names recorded for a class of total_students pupils.
# You must store the weights in a one-dimensional array and the names in another onedimensional array.
# All the weights must be validated on entry and any invalid weights rejected.
# You must decide your own validation rules. You may assume that the pupils’ names are unique.
# Output the names and weights of the pupils in the class.
#
# TASK 2
# The weight, in kilograms, of each pupil is recorded again on the last day of term.
# Calculate and store the difference in weight for each pupil.
#
# TASK 3
#
# For those pupils who have a difference in weight of more than 2.5 kilograms, output, with a suitable
# message, the pupil’s name, the difference in weight and whether this is a rise or a fall.
#
# Your program must include appropriate prompts for the entry of data. Error messages and other
# outputs need to be set out clearly and understandably.
# All variables, constants and other identifiers
# must have meaningful names.
# Each task must be fully tested.

def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_string(s):
    try:
        str(s)
        return True
    except ValueError:
        return False


def validate_weight(weight):
    if is_num(weight) is True and weight > 0:
        return True
    else:
        print("Weight cannot be negative. Invalid weight.")


def split_values(details):
    if "," in details:
        details = details.split(",")
        name = details[0].strip()
        initial_weight = details[1].strip()
        valid_input = validate_weight(initial_weight)
        if valid_input is False:
            print("Invalid input.")
    return valid_input, name, initial_weight


total_students = 30
names = []
initial_weights = []
final_weights = []
differences = []

if __name__ == "__main__":
    count = 1
    while True:
        student_detail = input(
            f"Please input name and initial weight of the student {count} in kilograms. Comma seperated. ")
        valid_input, name, initial_weight = split_values(student_detail)
        if valid_input is True:
            names.append(name)
            initial_weights.append(initial_weight)
            count = count + 1
        if len(names) >= total_students:
            for i in range(len(names)):
                print(f"Student {i + 1}, {names[i]} weighs {initial_weights[i]}kg. ")
            break

    counter = 0
    while True:
        final_weight = input(f"Please enter final weight of {names[counter]} in kilograms. ")
        if validate_weight(final_weight) is True:
            final_weights.append(float(final_weight))
            counter = counter + 1
        if len(final_weights) >= total_students:
            break

    for i in range(total_students):
        difference = final_weights[i] - initial_weights[i]
        differences.append(difference)
        if differences[i] > 2.5:
            print(f"Student {i + 1}, {names[i]} has gained {differences[i]} kilograms. ")
        if differences[i] < -2.5:
            positive_diff_temp_decrease = differences[i] * -1
            print(f"Student {i + 1}, {names[i]} has lost {positive_diff_temp_decrease} kilograms. ")
