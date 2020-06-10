import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("v.srinivassunnya5@gmail.com","voorefamily7")
server.sendmail("v.srinivassunnya5@gmail.com@gmail.com",
                "jithendrakatta999@gmail.com",
                "Hello World!!! from python")

server.quit()
