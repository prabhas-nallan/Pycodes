books={"Ikigai":299,"Wasted in Engineering":180,"The monk who sold his Ferrari":160}
print(books)
print("After sorting")
sorted_books=sorted(books)
print(sorted_books)
book_name=input("Enter the book name : ")
if book_name in books:
    print(f"Yes the book {book_name} is present in dictionary")
else:
    price=int(input("Enter the book price "))
    books[book_name]=price
    print(books)
