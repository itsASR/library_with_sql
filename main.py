import mysql.connector




class Sqlclass:
    def __init__(self):
        
        self.cnx = mysql.connector.connect(user='root', password='9680415819Asr',
                              host='127.0.0.1',
                              database='library')
        query = 'create table if not exists book_info(book_id int, book_name varchar(125), author varchar(125), category varchar(100))'
        sqldata = self.cnx.cursor()
        sqldata.execute(query)
        print("Created")

    #book_id int, book_name varchar(125), author varchar(125), category varchar(100)

    #insert
    def insert_book(self,bookid,bookname,authorname,categoryname):
        query = ("insert into book_info(book_id,book_name,author,category) values({},'{}','{}','{}')").format(bookid,bookname,authorname,categoryname)

        sqldata = self.cnx.cursor()
        sqldata.execute(query)
        self.cnx.commit()
        print("Book saved succesfully")

        
    #fetch
   
    def fetch_data(self):
        
        while True:
            print("Press 1 to search by category")
            print("Press 2 to search by name")
            print("Press 3 to go back")
            searchbook = int(input(" enter input "))
            try:
                if (searchbook == 1):
                    print("_______________________________________________________")
                    print("Please select category from below list")
                    query2 = ("select distinct category from book_info")
                    sqldata = self.cnx.cursor()
                    sqldata.execute(query2)
                    for q in sqldata:
                            
                            print("category name ",q)
                    print("_______________________________________________________")
                    categorysearch = input("enter category name  ")
                    print()

                    def option1(self,categorysearch):
                        
                        query = ("select * from book_info where category = '{}' ").format(categorysearch)
                        sqldata = self.cnx.cursor()
                        sqldata.execute(query)
                        print("_______________________________________________________")
                        print()
                        for i in sqldata:
                            print("Book ID :        ", i[0])
                            print("Book Name :      ", i[1])
                            print("Book Author :    ", i[2])
                            print("Book Category :  ", i[3])
                            print()
                            print()
                            
                        print("_______________________________________________________")
                    option1(self,categorysearch)     

                elif searchbook == 2:
                    
                    namesearch = input("enter Book name  ")
                    def option2(self,namesearch):
                        query = ("select * from book_info where book_name = '{}' ").format(namesearch)
                        sqldata = self.cnx.cursor()
                        sqldata.execute(query)
                        for i in sqldata:
                            print("_______________________________________________________")
                            print(i)
                            print("_______________________________________________________")
                    option2(self,namesearch)   

                elif searchbook == 3:
                    break

                else:
                    print("wrong key")
        
            except Exception as e:
                
            
                print("Mismatch or Not Found")



  

    #delete
    def delete_book(self,bookiddelete):
        
        query = ("delete from book_info where book_id = {} ").format(bookiddelete)

        sqldata = self.cnx.cursor()
        sqldata.execute(query)
        self.cnx.commit()
        self.cnx.commit()
        print("Book delete with ID: ",bookiddelete , "succesfully")



