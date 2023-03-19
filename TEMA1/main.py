def is_accepted(cuvant, transitions, initial, final):
    current = initial
    states_visited = str(initial)  
    for char in cuvant:
        try:
            current = transitions[current][char]
        except KeyError:
            return False, states_visited
        states_visited += f"->{current}" 
    return current in final, states_visited

# functia se uita in dictionarul transitions pentru a vedea starea viitoare
# daca nu exista, va returna false
# daca ajungem la finalul cuvantului si starea in care se afla este si finala
# va returna true 



# citim din fisier sub forma:
# stare - caracter -starea urmatoare 
# adaugam fiecare stare noua in dictionar (daca nu exista)
with open("input.txt") as f:
    transitions = {}
    for linie in f:
        parts = linie.strip().split()
        if len(parts) == 3:
            state, char, next_state = parts
            if state not in transitions:
                transitions[state] = {}
            transitions[state][char] = next_state

#Luam starea intitiala si cea finala
initial = input("Starea initiala este: ")
final = set(input("Starea/Starile finale sunt(despartite prin spatiu): ").split())

#Cuvantul pe care il avem de verificat
cuvant = input("Cuvantul pe care vrei sa il verifici prin DFA: ")
accepted, states_visited = is_accepted(cuvant, transitions, initial, final)

#output
if accepted:
    print("Cuvantul este acceptat de DFA.")
    print("Starile prin care a trecut: ", states_visited)
else:
    print("Cuvantul nu este acceptat de DFA.")

