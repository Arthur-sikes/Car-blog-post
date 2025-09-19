import hashlib
pass_found = 0
print(' '*20,end=' ')
print('PASSWORD CRACKER',end=' '*5)
print(" ")
input_hash = input("Enter the hashed passwords : ")
pass_doc = input("Enter the password filename :")
try:
    pass_file = open(pass_doc,'r')
except:
    print("Erorr")
    print(f"{pass_doc} is not found")
    quit()
for word in pass_file:
    enc_word = word.encode()
    hash_word = hashlib.sha256(enc_word.strip())
    digest = hash_word.hexdigest()
    if digest == input_hash:
        print(f"password found \n password: {word}")
        pass_found = 1
        break
        
if not pass_found:
        print('password is not found in the password file',)
        print("\n")
print("Thank you")
        
