import Admin
import User

def main():
    start()

#having it separate allows the program to call start again 
# without the need for loops at the start. 
def start():
    try:
      firstinput = int(input("Press 1 for admin, 2 for user "))
    except:
        print("Not a number")
        print("Please Try Again")
        start()
    if(firstinput == 1):
          Admin.textout() #goes to the admin page
    elif(firstinput == 2):
          User.textout() #goes to user page
    else:
        print("please try again")
        #if it is not one of the two, it calls the function again 
        #for users to reenter
        start() 


if __name__ == "__main__":
    main()
    