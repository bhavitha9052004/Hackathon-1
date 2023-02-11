import os
import encrypt_decrypt
import colorama
import logging
import joblib
import string

logging.basicConfig(filename="logging.log",format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

#f=open("vault.txt","x")
#f.close()
f=open("vault.txt","w")
f.write("Key value : ")
f.close()
f=open("vault.txt","a")
key=str(encrypt_decrypt.key)
f.write(key)
f.close()
f=open("vault.txt","r")
print(f.read())
f.close()

#storing encrypted and decrypted message

f=open("vault.txt","a")
enc=encrypt_decrypt.encMessage
dec=encrypt_decrypt.decMessage
f.write("\nEncrypted message : "+str(enc))
#f.write(enc)
f.close()

f=open("vault.txt","a")
f.write("\nDecrypted message : "+str(dec))
#f.write(dec)
f.close()

f=open("vault.txt","r")
print(f.read())

def startautomation(iterations,threadid):
    counter = 0
    print(iterations)
    logger.debug("Harmless debug Message for automation set "+str(threadid)+"\nTransaction " + str(threadid+1)+" complete")


    while counter <= int(iterations):

        print(
            colorama.Fore.CYAN + "\n" + "Automation Set [" + str(counter) + "] " )
        counter = counter + 1
    else:
        print(
            colorama.Fore.GREEN + "\n################################################## Automation Completed ##################################################")
        
if __name__=="__main__":
    startautomation(iterations)