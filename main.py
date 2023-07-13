
from operations import operation



def selection_validate():
    
    valid_selections = ('1', '2', '3', '4', '5', '6')
    print("                  ")
    input(" -------- Press Enter to Continue -------- ")


    while True:
        selection = input (
            
            "\nPlease select from the following Options: "
            "\n"
            "\n"
            "🔹 1. To Add.\n"
            "🔹 2. To Subtract.\n"
            "🔹 3. To Divide.\n"
            "🔹 4. To Multiply\n"
            "🔹 5. For Modulo\n"
            "\n🟢 Enter choice:  "
        )

        if selection == 'exit':
          break
    
        if selection in valid_selections:
            return selection


        print('\nValue: {} did not match any menu choice'.format(selection))

    return None



def Additions():
    a = int(input("Enter No 1: "))
    b = int(input("Enter No 2: "))
    operation.Add(a,b)

def subtraction():
    a = int(input("Enter No 1: "))
    b = int(input("Enter No 2: "))
    operation.Subtract(a,b)

def divide():
    a = int(input("Enter No 1: "))
    b = int(input("Enter No 2: "))
    operation.Divide(a,b)

def multiplication():
    a = int(input("Enter No 1: "))
    b = int(input("Enter No 2: "))
    operation.multiply(a,b)
    
def modulo():
    a = int(input("Enter No 1: "))
    b = int(input("Enter No 2: "))
    operation.Modulo(a,b)




def selection_calls():
    selection = selection_validate()
    print("          ")


    if selection == '1':
        Additions()

    
    if selection == '2':
        subtraction()


    if selection == '3':
        divide()

        
    if selection == '4':
        multiplication()
  

    if selection == '5':
        modulo()



if __name__ == '__main__':
    selection_calls()

