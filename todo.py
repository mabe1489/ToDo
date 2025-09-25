import json
import time




#Lists
todos = []
# Speichern in einer .txt-Datei
def saveList(values):

    with open("SavedToDos.json", 'w') as f:
    # indent=2 is not needed but makes the file human-readable 
    # if the data is nested
        json.dump(values, f, indent=2)
with open("SavedToDos.json", 'r') as f:
    todos = json.load(f)

#UI
print("Laden")  
time.sleep(2) 
print("Starten") 
time.sleep(1)
print("Willkommen")



#Ading or removing ToDo
for _ in range(2):
    print("Das sind die Elemente:")
    for todo in todos:
        print(f"- {todo}")
    print("")
    newitem = input("Was möchtest du hinzufügen?: ")
    if newitem in todos:

        todos.remove(newitem)
        saveList(todos)
    
    else:
        todos.append(newitem)
        saveList(todos)



print("")
print("Ende Gelände")

