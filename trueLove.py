
name1 = input("Write a name of first person: ") # Write a name of first person
name2 = input("Write a name of second person") # Write a name of second person
combined_name = name1 + name2
lower_name = combined_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
print("The Love Calculator is calculating your score...")
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")