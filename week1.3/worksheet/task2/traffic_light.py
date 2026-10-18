"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Enter the amount of steps you want: "))  # read an integer number of steps (>0)

state = "red"

print(f"Time {systime:03} State {state}")

state_time = int(states.get(state))

for i in range(0,maxtime):
    systime += 1
    print(f"Time {systime:03} State {state}")
    state_time -= 1
    if state_time == 0:
        if state == "red":
                state = "red_amber"
        elif state == "red_amber":
                state = "green"
        elif state == "green":
                state = "amber"
        elif state == "amber":
                state = "red"
        state_time = int(states.get(state))

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14