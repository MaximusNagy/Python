Library = []
Wishlist = []

book = input("Enter the name of a book you own: ")
another_book = input("Enter the name of another book you own (or press 'Enter' to skip): ")

Library.append(book)
if another_book:
    Library.append(another_book)
print("\n Your Library:", Library)

wish_book = input("Enter the name of a book you wish to have in the future: ")
another_wish_book = input("Enter the name of another book you wish to have in the future (or press 'Enter' to skip): ")

Wishlist.append(wish_book)
if another_wish_book:
    Wishlist.append(another_wish_book)
print("\n Your Wishlist:", Wishlist)

wishlist_own = input("Enter the name of a book from wishlist that you've acquired (or press 'Enter' to skip): ")
if wishlist_own in Wishlist:
    Library.append(wishlist_own)
    Wishlist.remove(wishlist_own)

print("\nUpdated Library:", Library)
print("Updated Wishlist:", Wishlist)

donated_book = input("Enter the name of a book from library you wish to donate (or press 'Enter' to skip): ")

if donated_book in Library:
    Library.remove(donated_book)
print("Final Library after Donations:", Library)