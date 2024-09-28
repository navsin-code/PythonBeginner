import smtplib
import datetime as dt  # gets current date and time
import random

my_email = "pythonwork5670@gmail.com"
password = "fqhwxbqvhkezvlqo"

now = dt.datetime.now()  # module then class, gives current time
day = now.weekday()

if day == 0:  # Sends the quote only if it's Monday (0 represents Monday)
    with open("quotes.txt", 'r') as file:
        quotes = file.readlines()
        random_quote = random.choice(quotes).strip()  # Strip newline characters

    # Create a connection to the SMTP server
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="onethousandwordsmore@gmail.com",
            msg=f"Subject:Motivational Quote\n\n{random_quote}"
        )



