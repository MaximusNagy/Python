baskt= [['Apples', 'bananas'], ['milk', 'water']]
numbers= [1,2,3]
print(baskt)
enter= input("Press enter to change the content .....: ")

baskt[0].insert(0, 'Oranges')
baskt[0].append('Kiwis')
baskt[1].append('Tea')
baskt[1].remove("water")
baskt[1].insert(0, 'Coffee')
baskt.append(numbers)

print("Here is the updated basket")

print(baskt)