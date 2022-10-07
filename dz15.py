seconds = int(input())

minutes = 0
hours = 0
days = 0

dayName = str()
zero1 = str()
zero2 = str()
zero3 = str()

while seconds >= 60:
   seconds -= 60
   minutes += 1

while minutes >= 60:
   minutes -= 60
   hours += 1

while hours >= 24:
   hours -= 24
   days +=1

if(seconds / 10 < 1):
   zero3 = str(0)

if(minutes / 10 < 1):
   zero2 = str(0)

if(hours / 10 < 1):
   zero1 = str(0)

if(days % 1 == 1):
   dayName = "день,"

if(days % 10 > 1 and days % 10 < 5):
   dayName = "дня,"

if(days % 10 >= 5 or days == 0):
   dayName = "дней"

print(f"{days} {dayName}, {zero1}{hours}:{zero2}{minutes}:{zero3}{seconds}")