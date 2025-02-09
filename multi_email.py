import smtplib as s

# Connect to Gmail's SMTP server
ob = s.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

# Login securely
EMAIL = "hammadzaki2004@gmail.com"
PASSWORD = "zaki@#1234"  # Use an App Password for security
ob.login(EMAIL, PASSWORD)

# Email content
subject = "test python"
body = "I Love Python"
message = "Subject: {}\n\n{}".format(subject, body)

# Recipients
listadd = ['shammadzaki24@gmail.com', 'vilezaki@gmail.com']

# Send email
ob.sendmail(EMAIL, listadd, message)
print("Email sent successfully")

# Close the connection
ob.quit()
