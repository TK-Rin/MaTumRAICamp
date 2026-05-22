# ==========================================
# EXERCISE 3 — FIX THE FSM
# ==========================================

def ask(question)
    answer = input(question + " (yes/no): ")

    answer = answer.strip().lower()

    return answer == yes


def change_state(new_state):

print("State changed to:", new_state)

    return state


current_state = "Idle"


while True

    if current_state == "Idle":

        print("Robot is idle.")

        if ask("Has the food been loaded?"):

            current_state = change_state("Waiting")


    elif current_state = "Waiting":

        print("Waiting for table confirmation.")

        if ask("Is the table confirmed?")

            current_state = change_state("Navigating")


    elif current_state == "Navigating":

        print("Robot is navigating.")

        if ask("Is there an obstacle?"):

            current_state = change_state("Obstacle")

        elif ask("Has robot arrived?"):

            current_state = change_state("Delivering")


    elif current_state == "Obstacle":

        print("Waiting for obstacle to clear.")

        if ask("Obstacle cleared?"):

            current_state = change_state("Navigating")


    elif current_state == "Delivering":

        print("Waiting for customer pickup.")

        if ask("Food picked up?"):

            current_state = change_state("Success")


    elif current_state == "Success":

        print("Delivery completed.")

        break