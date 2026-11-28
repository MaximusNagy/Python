Attendance = ["Maximus" , "Nagy", "Domadios" , "mosa" ]


for parson in Attendance:
    print(parson)
    attendance_confirmed = input("Is this parson attending (Yes, No): ").capitalize()
    if attendance_confirmed == "Yes":
        print("Attendance confirmed")
        print("------")
    elif attendance_confirmed == "No":
        print("Attendance not confirmed")
        print("------")
    else:
        print("Please enter your choose")


# prasons = input("Enter the names of attendees separated by commas: ").split(", ")
# for confirmed in prasons:
#     print(confirmed)
#     attendance_confirmed = input("Is this parson attending (Yes, No): ").capitalize()
#     if attendance_confirmed == "Yes":
#         
#         print("Attendance confirmed")
#         print("------")
#     elif attendance_confirmed == "No":
#         print("Attendance not confirmed")
#         print("------")
#     else:
#         print("Please enter your choose")
