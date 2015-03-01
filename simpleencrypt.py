
def encrypt(string1):
    for i in range(0,len(string1)):
        if string1[i] in charas:
            p[i]=str(charas.find(string1[i]))
            print(string1[i],p[i])
        else:
            continue
   
    str1=''.join(p)
    print('the encrypted  string is:\n',str1)

def decrypt(string1):
    str2=[' ' for j in range(len(p))]
    for i in range(0,len(p)):
        str2[i] = charas[int(p[i])]
        
        
    print('the decrypted string is\n',''.join(str2))

def encryptfile(file1):  
    fo=open(file1,'r')
    encfile = open("encryptedfile.txt", "w")
    filestring=fo.read()
    encryptfile.key=[0 for j in range(len(filestring))]
    print(len(filestring))
    for i in range(0,len(filestring)):
        if filestring[i] in charas:
            encryptfile.key[i]=str(charas.find(filestring[i]))
            encfile.write(str(charas.find(filestring[i])))       
        else:
            continue
    fo.close()
    encfile.close()    
        
def decryptfile(key):
    #file2=input('write the file that you want to decrypt\n')
    fo=open("encryptedfile.txt",'r')
    decfile = open("decryptedfile.txt", "w")
    filestring=fo.read()
    print(len(filestring))
    for i in range(0,len(key)):
          deckey=charas[int(key[i])]
          decfile.write(deckey)       
    fo.close()
    decfile.close()

#MAIn prograMM
    
string1=input('Please enter a string for decryption\n')
p=[0 for j in range(len(string1))] #thats basically the encryption key
charas='abcdefghijklmnopqrstuvwxyz \#[]-=+ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./,()'                
encrypt(string1)
ask = input ('do you want to decyrpt the same string now?yes or no\n')
if ask =='yes':
   decrypt(string1)

ask2 = input ('do you want to encyrpt a file?yes or no\n')
if ask2 =='yes':
   file1 = input('write the file that you want to encrypt\n') 
   encryptfile(file1)
   decryptfile(encryptfile.key)
    
    
