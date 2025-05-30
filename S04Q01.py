"""S04Q01
     - A Chemical plant has a tank for storing ethanol.
            - When the tank is more than 80% full, it
                 should raise an alarm to close the valve.
            - When the tank is less than 20% full, it
                 should send an SMS to buy more liquid.
            - The total tank capacity is 900 litres.
            - Write a program to simulate this.
            - Ask user to enter current level of ethanol in the tank.
            - Print the appropriate action based on value entered
            - Make sure that your program needs minimum changes
                 for a tank of different capacity."""
""" What does this program do ?
"""

def do_action(present, redmark, bluemark):
    # Compare present with redmark and bluemark
    # to decide the appropriate action
    if(level>=high):
        print("Close the valve")
    elif(level <= low):
        print("Add more liquid")
    else:
        print("No Immediate action required")
        
def get_current_level():
    # Get value from user
    # Return integer
    current_state = int(input("enter current level of ethanol in the tank:"))
    return current_state

# Main starts from here
capacity = 900
high = 0.8 * capacity
low = 0.2 * capacity
level = get_current_level()
do_action(level, high, low)