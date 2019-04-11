import os, sys

print  ("\033[1;32m Login dulu cuk!")
username :'Mr.51mb4h'
password :'tobatlah'

def restart () :
    ngulang = sys.excecutable
    os.execl(ngulang,ngulang,*sys.argv)
 
 def main () :
     uname = raw_input ("username : ")
     if uname == username :
         pwd = raw_input ("password : ")
         if pwd == password :
             print "\n\033[1;32m welcome siapkan sabunya ya..",
             sys.exit
             
          else : 
             print "\n\033[1;32mPassword salah anjing!!!\033[00m"
                restart()
                
     else :
         print "\n\033[1;32mUsername salah cuk!!"
             restart()



try: 
    main ()
except Keyboard Interrupt :
    os.system('clear')
    restart()