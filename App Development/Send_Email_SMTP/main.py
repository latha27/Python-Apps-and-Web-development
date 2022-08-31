#import smtplib

#my_email = "lathass199027@gmail.com"
#password = "Soppinahally@27"

#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email, password=password)
#    connection.sendmail(from_addr=my_email,
#                        to_addrs="lathass199027@yahoo.com",
#                        msg="Hello."
#    )
import datetime as dt
import random
import smtplib

my_email = "lathass199027@gmail.com"
password = "Soppinahally@27"

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 2:
    with open("quotes.txt") as data:
        read_text = data.readlines()
        random_select = random.choice(read_text)
    print(random_select)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Monday Motivation\n\n{random_select}")



