from main import Sqlclass

def main():
    db = Sqlclass()
    
    

    while True:
        print("_______________________________WELCOME to Library___________________________")
        print("Press 1 to add new book")
        print("Press 2 to search book")
        print("Press 3 to modify library data")
        print("press 4 to exit")

        

        try:
            case = int(input())
            if(case == 1):
                bookid  = int(input("please enter Book ID "))
                bookname = input("Please enter Book Name ")
                authorname = input("Please enter Author Name ")
                categoryname = input("Please enter Category Name ")
                db.insert_book(bookid,bookname,authorname,categoryname)

            
            elif case == 2:
                #op.fetch_data()
                db.fetch_data()

                

            elif case == 3:
                try:
                    bookiddelete = int(input("Please enter book id "))
                    db.delete_book(bookiddelete) 

                except :
                    print("-------------------------------------------")
                    print("Wrong input xxxxxxxx")
                    print("-------------------------------------------")
                
                

            elif case == 4:
                print("_________Thanks for using_________")
                break

            else:
                print("wrong input, Try again")

    
        except Exception as e:
            print(e)
            
            print("Invalid Details ! Try again")


if __name__ == "__main__":
    main()