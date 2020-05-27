import smtplib
import getpass

w = '\033[0m'
g = '\033[32m'
c = '\033[1;36;40m'


# Gmail Login
# username = input("Your email: ")
username = "dragogogo1234@gmail.com"
password = getpass.getpass("Password: ")

# From adrress & To address
# fromaddress = username
# toaddress = input("To address: ")
fromaddress = "dragogogo1234@gmail.com"
toaddress = "593849302dzq@gmail.com"


# message
# message = eval(input("Your message: "))
message = c+"\n[*]"+w+" Running . . ."+w + "\n"+g+"[*]"+w
file = open("spam.txt","r+") 
message1 = file.read()
file.close() 

# Creating a connection
server =smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)

# for loop to send multiple spam
total = 1
for i in range (total):
	print(message1)
	server.sendmail(fromaddress,toaddress,message1)
	print("Mail "+str(i)+" send")

server.quit()
