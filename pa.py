# task to write a python program using match to print the table between 1 to 10

a = int(input("ENTER THE VALUE FROM (1-10) TO PRINT THE TABLES \n"))

match a:
    case 1:
        for b in range(10):
            print("the table of 1 is " ,1*b)
    
    case 2:
        for b in range(10):
            print("the table of 1 is " ,2*b)     
            
    case 3:
        for b in range(10):
            print("the table of 1 is " ,3*b)
            
    case 4:
        for b in range(10):
            print("the table of 1 is " ,4*b)

        
    case 5:
        for b in range(10):
            print("the table of 1 is " ,5*b)
    case 6:
        for b in range(10):
            print("the table of 1 is " ,6*b)
    case 7:
        for b in range(10):
            print("the table of 1 is " ,7*b)
    case 8:
        for b in range(10):
            print("the table of 1 is " ,8*b)
    case 9:
        for b in range(10):
            print("the table of 1 is " ,9*b)
    case 10:
        for b in range(10):
            print("the table of 1 is " ,10*b)
    case _:
        print("ENTER BETWEEN (1-10)")

              
              
              
             
      