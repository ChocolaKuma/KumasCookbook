import hashlib
def hashIt(key_string,HashAlgr="md5"):    
    key_string = key_string.encode('utf-8')
    if(HashAlgr == "md5"):
        e_pass = hashlib.md5(key_string).hexdigest()       
    elif(HashAlgr == "sha1"):
        e_pass = hashlib.sha1(key_string).hexdigest()        
    elif(HashAlgr == "sha224"):
        e_pass = hashlib.sha224(key_string).hexdigest()
    elif(HashAlgr == "sha256"):
        e_pass = hashlib.sha256(key_string).hexdigest()
    elif(HashAlgr == "sha512"):
        e_pass = hashlib.sha512(key_string).hexdigest()     
    return e_pass  

ToBeHashed = input("Word To Be hashed:")
print("\n\n")
print("md5:",hashIt(ToBeHashed,"md5"),"\n")
print("sha1:",hashIt(ToBeHashed,"sha1"),"\n")
print("sha224:",hashIt(ToBeHashed,"sha224"),"\n")
print("sha256:",hashIt(ToBeHashed,"sha256"),"\n")
print("sha512:",hashIt(ToBeHashed,"sha512"),"\n")
 
