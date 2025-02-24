# Write and test a program to complete the three tasks.
#
# TASK 1
#
# A data logger records the temperature on the roof of a school twice a day, at midday and midnight.
# Input and store the temperatures recorded for a month.
# You must store the temperatures in two one dimensional arrays,
#     One for the midday temperatures and one for the midnight temperatures.
# All the temperatures must be validated on entry and any invalid temperatures rejected.
# You must decide your own validation rules. You may assume that there are 30 days in a month.
#
# TASK 2
# Calculate the average temperature for midday and the average temperature for midnight.
# Output these averages with a suitable message for each one.
#
# TASK 3
#
# Select the day with the highest midday temperature and the day with the lowest midnight temperature.
# Then output each of these temperatures, the corresponding day and a suitable message.
# Your program must include appropriate prompts for the entry of data. Error messages and other
# outputs need to be set out clearly and understandably.
# All variables, constants and other identifiers must have meaningful names. Each task must be fully tested.
def is_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


# def take_valid_temp(mid_day):
#     done = False
#     while not done:
#         type = 'mid-day'
#         if not mid_day:
#             type = 'mid-night'
#         temp = input(f"Enter the {type} temperature.")
#         if is_num(temp) is True:
#             done = True


midday = []
midday_total = 0
midday_average = 0
midday_highest = 0

midnight = []
midnight_total = 0
midnight_average = 0
midnight_lowest = 0

if __name__ == '__main__':

    # while done is False:
    #     if (len(midday) < 30):
    #         # take mid day value
    #
    #     if (len(midnight) < 30):
    #         # take midnight value

    # while (len(midday) != 30) and (len(midnight) != 30):
    while True:
        if len(midday) < 30:
            midday_temp = input(
                f"Day {len(midday) + 1}: Enter the midday temperature in degrees Celsius (-100º to 100º)")
            if is_num(midday_temp) is False:
                print("Invalid input.")
            else:
                midday_temp = float(midday_temp)
                if -100 < midday_temp < 100:
                    midday.append(midday_temp)
                else:
                    print("Number should be between -100 to 100")
        if len(midnight) < 30:
            midnight_temp = input(
                f"Day {len(midnight) + 1}: Enter the midnight temperature in degrees Celsius (-100º to 100º) ")
            if is_num(midnight_temp) is False:
                print("Invalid input.")
            else:
                midnight_temp = float(midnight_temp)
                if -100 < midnight_temp < 100:
                    midnight.append(midnight_temp)
                else:
                    print("Number should be between -100 to 100")
        if len(midday) == 30 and len(midnight) == 30:
            break

    # Inputting all the 30 midday and midnight temperatures and adding to the list midday and midnight
    # Validation condition: The inputted temperature is a number AND is in between -100 and 100

    for i in range(30):
        midday_total = midday[i] + midday_total
        midnight_total = midnight[i] + midnight_total
    # Calculating the total midday and midnight temperatures

    midday_average = midday_total / 30
    midnight_average = midnight_total / 30
    # Calculating the average midday and midnight temperatures

    print(f"The average midday temperature is {midday_average}ºC.")
    print(f"The average midnight temperature is {midnight_average}ºC.")

    midday_highest_index = 0
    midnight_lowest_index = 0
    for i in range(30):
        if midday[i] > midday[midday_highest_index]:
            midday_highest_index = i
            midday_highest = midday[midday_highest_index]

        if midnight[i] < midnight[midnight_lowest_index]:
            midnight_lowest_index = i
            midnight_lowest = midnight[midnight_lowest_index]

    print(
        f"The highest midday temperature was on day {midday_highest_index + 1} which was a temperature of {midday_highest}ºC")
    print(
        f"The lowest midnight temperature was on day {midnight_lowest_index + 1} which was a temperature of {midnight_lowest}ºC"
    )

    # for i in range(29):
    #     mid_day_temp = take_valid_temp(mid_day=True)
    #     midday.append(mid_day_temp)
    #     mid_night_temp = take_valid_temp(mid_day=False)
    #     midnight.append(mid_night_temp)

    # while True:
