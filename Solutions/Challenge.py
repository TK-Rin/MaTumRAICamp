# ==========================================
# FINAL CHALLENGE
# FOOD DELIVERY ROBOT FSM
# ==========================================


# ------------------------------------------
# Function: Ask yes/no question
# ------------------------------------------

def ask(question):

    answer = input(question + " (yes/no): ")

    answer = answer.strip().lower()

    return answer == "yes"


# ------------------------------------------
# Function: Change robot state
# ------------------------------------------

def change_state(new_state):

    print("\nState changed to:", new_state)

    return new_state


# ------------------------------------------
# Function: Display current state
# ------------------------------------------

def show_state(state):

    print("\nCurrent State:", state)
    print("-" * 50)


# ==========================================
# MAIN PROGRAM
# ==========================================

current_state = "Idle"


while True:

    # ======================================
    # IDLE STATE
    # ======================================

    if current_state == "Idle":

        show_state(current_state)

        while not ask("Has the food been loaded?"):

            print("Waiting for food to be loaded...")
            print("-" * 50)

        current_state = change_state("Waiting")


    # ======================================
    # WAITING STATE
    # ======================================

    elif current_state == "Waiting":

        show_state(current_state)

        while not ask("Is the table confirmed?"):

            print("Waiting for table confirmation...")
            print("-" * 50)

        current_state = change_state("Navigating")


    # ======================================
    # NAVIGATING STATE
    # ======================================

    elif current_state == "Navigating":

        show_state(current_state)

        if ask("Is there an obstacle?"):

            current_state = change_state("Obstacle")

        elif ask("Has the robot arrived at the table?"):

            current_state = change_state("Delivering")

        else:

            print("Robot is navigating...")
            print("-" * 50)


    # ======================================
    # OBSTACLE STATE
    # ======================================

    elif current_state == "Obstacle":

        show_state(current_state)

        while not ask("Has the obstacle been cleared?"):

            print("Waiting for obstacle to clear...")
            print("-" * 50)

        current_state = change_state("Navigating")


    # ======================================
    # DELIVERING STATE
    # ======================================

    elif current_state == "Delivering":

        show_state(current_state)

        while not ask("Has customer picked up the food?"):

            print("Waiting for customer pickup...")
            print("-" * 50)

        current_state = change_state("Success")


    # ======================================
    # SUCCESS STATE
    # ======================================

    elif current_state == "Success":

        show_state(current_state)

        if ask("Is there another table to serve?"):

            current_state = change_state("Navigating")

        else:

            current_state = change_state("GoingHome")


    # ======================================
    # GOING HOME STATE
    # ======================================

    elif current_state == "GoingHome":

        show_state(current_state)

        while not ask("Has the robot arrived home?"):

            print("Returning home...")
            print("-" * 50)

        current_state = change_state("Idle")

        print("\nRobot returned home successfully.")
        print("Program ended.")

        break
