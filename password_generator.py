import random, string
def generatePassword():
     lenght_of_password = int(input("How long should the password be? Please tell me in numbers. "))
     password_candidate_characters = string.ascii_letters + string.digits + string.punctuation
     password = ""
     for x in range(lenght_of_password):
         password += (random.choice(password_candidate_characters))
         
     return password
     
print(generatePassword())
 
def main1():
     
 
     if __name__ == '__main__':
          generatePassword()
         