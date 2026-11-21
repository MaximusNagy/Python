names = input("Enter the first and last name of your friends separated by comma: ").split(", ")

summray_name = []

for name in names:
    name_parts = name.split()
    
    first_name = name_parts[0]
    last_name = name_parts[1]

    summray_first_name = first_name[0].upper()
    summray_last_name = last_name[0].upper()
    p_summray = summray_first_name +"."+ summray_last_name+"."
    summray_name.append(p_summray)

    print(name_parts)
print("summray_name")
for i in (summray_name):
    print(i)
