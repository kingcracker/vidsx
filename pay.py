import os, sys

print ("\033[1;35mMasukan UserName&Password nya CUK!!!!")
print ("\033[1;32;1mKalo Gak Tau Pm Tanya Yang buat njing!!!")
username = 'BOKEPERS'      
password = 'BIGTITS'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mHello Welcome BOKEPERS", 
			sys.exit()

		else:
			print "\n\033[1;34mPasswordnya salah tod !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mUsernamenya Salah kontol !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()