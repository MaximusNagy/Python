print("\n--- Welcome to place rabbit ---")

leaves = [["🍃", "🍃", "🍃"], ["🍃", "🍃", "🍃"], ["🍃", "🍃", "🍃"]]
print(f"{leaves[0]} \n{leaves[1]} \n{leaves[2]}")

print("where should the rabbit go?🐇")
row_column =input("please enter row and column: ")
row = int(row_column[0]) -1
column = int(row_column[1]) -1
leaves[row][column] ="🐇"
print(f"{leaves[0]} \n{leaves[1]} \n{leaves[2]}")
