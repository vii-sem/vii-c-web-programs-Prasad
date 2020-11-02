
import smtplib 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication 
s.login("abdulazizhassan.1956@gmail.com", "a770233102A") 

# message to be sent 
message = "Hi there"

# sending the mail 
s.sendmail("abdulazizhassan.1956@gmail.com", "omarhassan-2016@outlook.com", message) 

# terminating the session 
s.quit() 
