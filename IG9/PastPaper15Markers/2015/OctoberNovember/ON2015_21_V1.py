# A new born baby is kept in a cot in a hospital; the temperature of the baby is monitored every
# 10 minutes. The temperature of the baby is recorded in degrees Celsius to one decimal place and
# must be within the range 36.0°C to 37.5°C.

# TASK 1

# To simulate the monitoring required, write a routine that allows entry of the baby’s temperature in
# degrees Celsius. The routine should check whether the temperature is within the acceptable range,
# too high or too low and output a suitable message in each case.

# TASK 2

# Write another routine that stores the temperatures taken over a three hour period in an array. This
# routine should output the highest and lowest temperatures and calculate the difference between
# these temperatures.

# TASK 3

# For a baby who has a temperature difference of more than one degree Celsius, and/or has been
# outside the acceptable range more than twice in the three hour period, output a suitable message
# giving a summary of the problem.
# Your program must include appropriate prompts for the entry of data. Error messages and other
# outputs need to be set out clearly and understandably. All variables, constants and other identifiers
# must have meaningful names. Each task must be fully tested.

def is_num(input_value):
    try:
        float(input_value)
        return True
    except ValueError as ve:
        print("Invalid input.")
        print(ve)
        return False
    except Exception as e:
        print(e)
        return False


# def is_valid_temperature(input_temperature):
#     if is_num(input_temperature) is True:
#         input_temperature = float(input_temperature)
#         if 36.0 <= input_temperature <= 37.5:
#             return True
#         else:
#             return False
#     else:
#         return False

if __name__ == "__main__":
    temperatures = []
    hours = 3
    interval_min = 10
    temperature_record_count = int((hours * 60) / interval_min)
    count = 0
    outside_temperature_range_count = 0
    outside_temp_range = []
    while len(temperatures) < temperature_record_count:
        temperature = input(f"Please enter temperature of the baby at the {count * 10} minute, in degrees Celsius. ")
        if is_num(temperature) is True:
            temperature = float(temperature)
            temperatures.append(temperature)
            count = count + 1
    for i in range(len(temperatures)):
        if temperatures[i] < 36.0 or temperatures[i] > 37.5:
            outside_temperature_range_count = outside_temperature_range_count + 1
            outside_temp_range.append(temperatures[i])
    maximum_temp_index = 0
    minimum_temp_index = 0
    for i in range(len(temperatures)):
        if temperatures[i] > temperatures[maximum_temp_index]:
            maximum_temp_index = i
        if temperatures[i] < temperatures[minimum_temp_index]:
            minimum_temp_index = i

    difference = temperatures[maximum_temp_index] - temperatures[minimum_temp_index]

    if (difference > 1) or (outside_temperature_range_count > 2):
        for i in range(len(outside_temp_range)):
            print(f"The baby's temperature has exceeded the given range {outside_temperature_range_count} times.")
            print(f"For the {i+1}th time, it went to {outside_temp_range[i]}ºC. ")
            print(f"The difference between the baby's temperatures was also greater than 1ºC. ")
