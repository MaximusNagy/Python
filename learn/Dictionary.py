book ={
    "title": "Red Queen",
    "author": "Victoria Aveyard",
    "year": 2015,
    "pages": 383,
    "is_many": "True",
    "rating": 4.1,
}

for name in book:
    if book[name] =="True":
        print(book[name])
    else:
        print(0)