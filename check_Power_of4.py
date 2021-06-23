def is_power_of_4(n):
     if n==4:
         return True
        
    
     elif n > 4:
         n=n/4
         return is_power_of_4(n)
     else:
        return False
         
print(is_power_of_4(20))
    

        