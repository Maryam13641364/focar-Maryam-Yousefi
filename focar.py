# Maryam
# 17.10.2026
# forward 1 m





# main.py
from focar import move_forward
from focar import move_backward
from focar import turn_right
from focar import turn_left
from focar import control_led

def main_mission():
    try:
        # start LED for begining
        control_led(True)
        
        # move forward 1 meter
        move_forward(1.0)
        
        #  Three-point turn
        print("Starting 3-point turn...")
        # turn to right 90 degrees
        turn_right(90)
        # move forward 0.5 meter
        move_forward(0.5)
        # turn to left 180 degrees
        turn_left(180)
        # move backward 0.5 meter
        move_backward(0.5)
        # turn to right 90 degrees
        turn_right(90)
        
        # back to the starting point
        print("Returning to starting point...")
        move_forward(1.0)
        
        # turn off LED at the end part
        control_led(False)
        
    except Exception as e:
        print(f"An error occurred during the mission: {e}")

if __name__ == "__main__":
    main_mission()