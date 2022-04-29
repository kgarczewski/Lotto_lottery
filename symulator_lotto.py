import random

def lotto_draw():
     """Lotto draw - get 6 random numbers from range 1 - 49"""
     lotto_numbers = set()
     while len(lotto_numbers)<6:
         rnd = random.randint(1, 49)
         lotto_numbers.add(rnd)
     return lotto_numbers
print(lotto_draw())


def get_the_numbers():
    """Get numbers from user"""
    user_numbers = set()
    while len(user_numbers) < 6:
        try:
            user_number = int(input("Please enter six numbers:  "))
            if user_number not in range(0, 50):
                print("Choose the number from range 1 - 49.")
            elif user_number in user_numbers:
                print("You already entered this number")
            else:
                user_numbers.add(user_number)
        except ValueError:
            print("It is not a number!")
    return user_numbers



def lotto():
    lotto = lotto_draw()
    user = get_the_numbers()
    count = lotto - user
    if len(count) > 3:
        return "Unfortunately you did not win!"
    elif len(count) == 3:
        return "Congratulations you hit 3!"
    elif len(count) == 2:
        return "Congratulations you hit 4!"
    elif len(count) == 1:
        return "Congratulations you hit 5!"
    elif len(count) == 0:
        return "Congratulations you hit 6!"
print(lotto())

lotto()


     
     

    




















