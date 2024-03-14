print("How much did you pay for your meal")
meal = float(input())
tip15 = meal *.15
tip18 = meal *.18
tip20 = meal *.20
print("With 15%", "\n Total:", "$" "{:.2F}" .format(meal),"\nTip", "$" "{:.2F}" .format(tip15), "\nTotal with tip","{:2F}" .format(meal + tip15))

print("With 18%", "\n Total:", "$" "{:.2F}" .format(meal),"\nTip", "$" "{:.2F}" .format(tip18), "\nTotal with tip","$" "{:.2f}".format(meal + tip18))

print("With 20%", "\n Total:", "$" "{:.2F}" .format(meal),"\nTip", "$" "{:.2F}" .format(tip20), "\nTotal with tip" "$" "{:.2f}".format(meal + tip20))