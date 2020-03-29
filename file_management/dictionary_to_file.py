performances = {'Ventriloquism':       '9:00am', 
                'Snake Charmer':       '12:00pm', 
                'Amazing Acrobatics':  '2:00pm', 
                'Enchanted Elephants': '5:00pm'}

with open('schedule.txt', 'wt', encoding='utf-8') as schedule_file:
    for key, val in performances.items():
        schedule_file.write(key+" - "+val+"\n")


schedule_file = open('schedule.txt', 'r')
performances_read = {}
for line in schedule_file:
    key, value = line.replace("\n","").split("-")
    performances_read[key] = value

print(performances_read)