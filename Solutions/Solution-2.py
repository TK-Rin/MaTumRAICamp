# ==========================================
# EXERCISE 2 — SOLUTION
# ==========================================

def ask(question):

    answer = input(question + " (yes/no): ")

    answer = answer.strip().lower()

    return answer == "yes"


def change_state(new_state):

    print("State changed to:", new_state)

    return new_state


# ==========================================
# TEST AREA
# ==========================================

current_state = "Idle"

if ask("Has the food been loaded?"):

    current_state = change_state("Waiting")

print("Current State:", current_state)