import time
def searcher():
    # Takes time to search
    book="Tarun is a student of cvr college"
    time.sleep(4)

    while True:
        text=(yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("The text is not in the book")
    
search=searcher()
print("Search started")
next(search)
search.send("Tarun")
search.close()
input("Press any key")
search.send("college")
input("Press any key")
search.send("s")
input("Press any key")
search.send("not")