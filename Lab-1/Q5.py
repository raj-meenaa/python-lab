# from datetime import datetime, date, time
# dt=datetime(2011, 10, 29, 20, 30, 21)
# dt.day
# dt.minute
# dt.year
# conv=datetime.strptime("20091012", "%Y%m%d")
# print(conv)

number=int(input("enter any number: "));
year=int(number/365);
reminder=int(number%365)
weeks=int(reminder/7)
days=int(reminder%7)
print("Total years is: ",year)
print("total weeks is: ",weeks)
print("Total days is: ", days)