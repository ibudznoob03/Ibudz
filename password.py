import os, sys

print ("\033[0;34mLogin Username Dan Password")
print ("\033[0;34m$WA: 083873098030")
username = 'Ibudz'      
password = 'tampan'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mSELAMAT MENCOBA"
			sys.exit()

		else:
			print "\n\033[1;36mUsername atau password salah !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mUsername atau password salah !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
