import random
def dice_rolling_sum_of_two_rolls():
    first_rolling= dice_rolling()
    print("First rolling: ", first_rolling)
    second_rolling= dice_rolling()
    print("Second rolling: ", second_rolling)
    sum= first_rolling+second_rolling
    return sum

#print(dice_rolling_sum())

def dice_rolling():
    roll= random.randint(1,6)
    return roll

def frequency_rolls():
    while True:
        try: 
            rolls = int(input("How many rolls do you want? "))
            break
        except ValueError:
            print("Please give valid number")



    dict_frequency = {i: 0 for i in range(2, 13)}
    print(dict_frequency)
    for i in range(rolls):
        rolling_result = dice_rolling_sum_of_two_rolls()
        dict_frequency[rolling_result]+=1
    return dict_frequency

print(frequency_rolls())