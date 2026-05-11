rooms = [
    {"number": 101, "status": "empty"},
    {"number": 102, "status": "busy"},
    {"number": 103, "status": "empty"},
    {"number": 104, "status": "busy"}
]

free_rooms = []

for room in rooms:
    if room["status"] == "empty":
        free_rooms.append(room["number"])

print("Bo'sh xonalar:")

for room in free_rooms:
    print(room)

selected = int(input("Xona tanlang: "))

if selected in free_rooms:
    print("Bron qilindi")
else:
    print("Xona band")
