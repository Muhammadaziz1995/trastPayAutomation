import datetime as d


# a = "1 000 UZS".split(' ')
# b = "4 UZS"
# res = int(a[0] + a[1]) + int(b.split(' ')[0])
# print(res)

today = d.datetime.now()
year = today.year
month = today.month
current_date = today.day
res = "{}.{}.{}".format(current_date, month, year)
cur_date = today.strftime("%y.%m.%d")
print(cur_date)