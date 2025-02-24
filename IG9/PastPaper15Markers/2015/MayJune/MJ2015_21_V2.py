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


total_students = 30
names = []
initial_weights = []
final_weights = []
differences = []

if __name__ == "__main__":
    count = 1
    while len(names) < total_students:
        print(f"----------STUDENT {count}----------")
        name = str(input(f"Enter the name of student {count}. "))
        if is_string(name) is True:
            names.append(name)
            initial_weight = input(f"Enter the initial weight of student {count}, in kilograms. ")
            if is_num(initial_weight) is True:
                initial_weight = float(initial_weight)
                if initial_weight > 0:
                    initial_weights.append(initial_weight)
                    final_weight = input(f"Enter the final weight of student {count}, in kilograms. ")
                    if is_num(final_weight) is True:
                        final_weight = float(final_weight)
                        if final_weight > 0:
                            final_weights.append(final_weight)
                        else:
                            print("Invalid final weight, it is less than 0.")
                            final_weight = input(f"Re-enter the final weight of student {count}, in kilograms. ")

                    else:
                        print("Invalid final weight, it is not a number.")
                        final_weight = input(f"Re-enter the final weight of student {count}, in kilograms. ")

                else:
                    print("Invalid initial weight, it is less than 0.")
                    initial_weight = input(f"Re-enter the initial weight of student {count}, in kilograms. ")
                    if is_num(initial_weight) is True:
                        initial_weight = float(initial_weight)
                        if initial_weight > 0:
                            initial_weights.append(initial_weight)
                            final_weight = input(f"Enter the final weight of student {count}, in kilograms. ")
                            if is_num(final_weight) is True:
                                final_weight = float(final_weight)
                                if final_weight > 0:
                                    final_weights.append(final_weight)
                            else:
                                print("Invalid final weight, it is not a number.")
                                final_weight = input(f"Re-enter the final weight of student {count}, in kilograms. ")
            else:
                print("Invalid initial weight, it is not a number.")
                initial_weight = input(f"Re-enter the initial weight of student {count}, in kilograms. ")
                if is_num(initial_weight) is True:
                    initial_weight = float(initial_weight)
                    if initial_weight > 0:
                        initial_weights.append(initial_weight)
                        final_weight = input(f"Enter the final weight of student {count}, in kilograms. ")
                        if is_num(final_weight) is True:
                            final_weight = float(final_weight)
                            if final_weight > 0:
                                final_weights.append(final_weight)
                        else:
                            print("Invalid final weight, it is not a number.")
                            final_weight = input(f"Re-enter the final weight of student {count}, in kilograms. ")
        else:
            print("Invalid name.")
        count = count + 1
        if len(names) >= total_students and len(initial_weights) >= total_students and len(
                final_weights) >= total_students:
            break
    for i in range(total_students):
        print(f"Student {i+1}, {names[i]} weighs {initial_weights[i]} kilograms")

    # Inputting the name, initial and final weight of each student.
    for i in range(total_students):
        difference = final_weights[i] - initial_weights[i]
        differences.append(difference)
        if differences[i] > 2.5:
            print(f"Student {i + 1}, {names[i]} has a weight increase of {differences[i]}. ")
        if differences[i] < -2.5:
            positive_diff_temp = differences[i] * -1
            print(f"Student {i + 1}, {names[i]} has a weight decrease of {positive_diff_temp}. ")
        # Calculating and printing out the differences.
