# Members of a litter picking group complete a litter pick every month. Members’ names are stored
# in one-dimensional (1D) array PickerName[]
#  Each member stores the weight of the litter they have picked in another one-dimensional (1D)
# array PickedWeight[]
#  The weights are in kilograms with one decimal place, for example 8.4
#  The position of each member’s data in the two arrays is the same. For example, the member
# stored at index 10 in PickerName[] and at index 10 in PickedWeight[] is the same.
#  Every month, there is a small prize awarded to the members of the group who have the two
# heaviest weights. Certificates are awarded to all members with a pick weight of over three
# kilograms.
#  Write a program that meets the following requirements:
#   • allows the weight of members’ picks to be input and validated
#   • sorts the arrays PickedWeight[] and PickerName[] in descending order of weight
#   • outputs the member names and the pick weights of the members with the two heaviest picks
#       and identifies them as “Best in Group” and “Second best in Group”
#   • stores the names of all the members who will receive a certificate in the array
#       PickerCertificate[]
#   • outputs a message stating the number of certificates to be printed.

#  You must use pseudocode or program code and add comments to explain how your code works.
#  You do not need to declare any arrays or variables; you may assume that this has already been
# done.
#  All inputs and outputs must contain suitable messages.
#  You do not need to initialise the data in the array PickerName[]

groupcount = int(input("Enter the total number of people in the group. "))
pickername = []
pickedweight = []
pickercertificate = []
for i in range(groupcount):
    name = str(input("Enter your name. "))
    weight = float(input("Enter the weight of the litter you have picked, rounded to one decimal point. "))
    pickername.append(name)
    pickedweight.append(weight)

# Adding the name of the person, and the weight picked to the respective arrays
heaviest_weight = -1
for i in range(groupcount):
    if pickedweight[i] > 3:
        pickercertificate.append(pickername[i])
        if pickedweight[i] > heaviest_weight:
            heaviest_weight = i
            heaviest_weight_name = pickername[i]
            pickedweight.remove(pickedweight[i])
            pickername.remove(pickername[i])
# Finding the names of the people that receive a certificate for picking a weight of more than 3 kilograms
# Also finding the heaviest weight picked

heaviest_weight = -1
for i in range(groupcount):
    if pickedweight[i] > heaviest_weight:
        second_heaviest_weight = i
        second_heaviest_weight_name = pickername[i]
        pickedweight.remove(pickedweight[i])
        pickername.remove(pickername[i])
# Finding the second-heaviest weight picked

print(f"Best in group is {heaviest_weight_name} who has picked a total of {heaviest_weight} kilograms")
print(f"Second best in group is {second_heaviest_weight_name} who has picked a total of {second_heaviest_weight} kilograms")
print(f"A total number of {len(pickercertificate)} will recieve a certificate")







