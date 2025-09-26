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

def listToDos(todos):
    #Adding or removing ToDo
        for _ in range(100000):
            print("Das sind die Elemente:")
            for todo in todos:
                print(f"- {todo}")
                print("")
            newitem = input("Was möchtest du schreiben?: ")
            if newitem == str(0):
                menu(todos)

            else:

                if newitem in todos:

                    todos.remove(newitem)
                    saveList(todos)
            
                else:
                    todos.append(newitem)
                    saveList(todos)
            

def menu(todos):
    print("Menü")
    help = input("Für Hilfe (1), sonst (0): ")
    if int(help) == 1:
        
        print("")
        print("Gebe eine Eingabe ein, um was in die Liste zu schreiben")
        print("Wenn das selbe eingegeben wird, dann wird die Eingabe aus der Liste gelöscht!")
        print("Hauptmenü ist die Taste 0")

    if int(help) == 0:

        inlist = input("In die Liste gehen (2), sonst 'exit': ")
        if int(inlist) == 2:
            listToDos(todos)
            

        if str(inlist) == "exit": 
                
            print("")
            print("Ende Gelände")


#UI
print("Laden")  
time.sleep(2) 
print("Starten") 
time.sleep(1)
print("Willkommen")
time.sleep(0.5)

menu(todos)