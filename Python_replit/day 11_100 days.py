sec = int(60)
min = 60
hour = 24
day = 31
month = 12
year = 365
yearnihours = hour * year # 8760h
yearnimin = yearnihours * 60
yearinsec = yearnimin * 60

leapyear = input("leap year yes or no")


if leapyear == "yes":
  print(yearinsec + int(86400))
else:
  print(yearinsec)
  
###############################
days_this_year = int(input("How many days are in this year?"))

days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60


result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute

leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute


if days_this_year == 366:
  print("Number of seconds in a leap year are", leapyear_result)
else:
  print("Number of seconds in a year are", result)
