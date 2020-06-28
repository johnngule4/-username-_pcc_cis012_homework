# this program calculate a person gross pay

hours = input("please input your hours to calculate your gross pay: ")
rate = input("please input your rate to calculate your gross pay: ")

if int(hours) <= 40:
    print("Your gross pay is", int(hours) * int (rate), "dollars")

elif int(hours) > 40:
    print("Your gross pay is", (int(hours) - 40) * (int(rate) *1) + 40 * int(rate))