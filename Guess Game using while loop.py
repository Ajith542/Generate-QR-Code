# Guess Game
import random
guess_number = random.randint(0,10)
print(guess_number)
def hardmode():
   
    try: 
       
        Secret_Number = guess_number
        guess_count = 0
        guess_Limit = 5
        
        while guess_count < guess_Limit :
          guess = int(input("Guess : ")) 
          if guess == Secret_Number:
             print('You Won')
             break
          
          elif guess > Secret_Number:
             print("The Number is greater than the Secret Number")
             guess_count += 1
             print(f" Guess count: {str(guess_count)}" )
             if guess_count == 5:
                print("you Exceeded your tries, Better Luck Next time")
             else:
                guess

          elif guess < Secret_Number:
             print("The Number is less than the Secret Number")
             guess_count += 1
             print(f" Guess count: {str(guess_count)}" )
             if guess_count == 5:
                print("you Exceeded your tries, Better Luck Next time")
             else:
                guess
                         
             
    except:
     print("Invalid, Try using number")
     
     hardmode()

hardmode()

 

   










