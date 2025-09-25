todos = []

for _ in range(10):
    newitem = input("Was möchtest du hinzufügen?: ")
    if newitem in todos:

        todos.remove(newitem)
    
    else:
        todos.append(newitem)

    print("Das sind die Elemente:")
    for todo in todos:
        print(f"- {todo}")

print("Ente Gelende")