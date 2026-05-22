# ==========================================
# EXERCISE 2 — FSM HELPER FUNCTIONS
# ==========================================

# Function to ask yes/no questions

def ask(question):

    answer = _____(question + " (yes/no): ")

    answer = answer.strip().lower()

    return answer == _____


# Function to change robot state

def change_state(new_state):

    print("State changed to:", _____)

    return _____


# ==========================================
# TEST AREA
# ==========================================

current_state = "Idle"

if ask("Has the food been loaded?"):

    current_state = change_state("Waiting")

print("Current State:", current_state)