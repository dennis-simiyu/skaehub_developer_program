import math
def is_perfect_square():
     perfect_square = int(input("Enter the your preferd number"))

     square_root = math.sqrt(perfect_square)
     if int(square_root + 0.5) ** 2 == perfect_square:
         print(perfect_square, "is a perfect square")
     else:
         print(perfect_square, "is not a perfect square")
         
is_perfect_square()