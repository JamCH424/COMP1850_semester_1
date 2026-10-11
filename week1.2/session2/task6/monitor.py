# Week 1.2, Session 2: Task 6
temp = int(input("What's the machine's temperature in degrees Celsius: "))
pressure = int(input("What's the machine's pressure in PSI: "))
status = int(input("What's the machine's operational status: "))

if temp > 80:
    print("Warning! Temperature too high, Consider turning of the machine.")
elif 80 >= temp >= 50:
    print("Temperature are within safe limits.")
elif 50 > temp:
    print("Temperature is low, no action needed.")

if pressure > 100:
    print("High pressure detected, maintenance is needed.")
elif 100 >= pressure >= 70:
    print("Pressure is stable")
elif 70 > pressure:
    print("Pressure is low, machine is operating normally.")

if status == 1 and pressure > 100 or temp > 80:
    print("The machine is running in unsafe conditions, consider shutting it down.")
elif status == 1 and pressure <= 100 or temp <= 80:
    print("The machine is running normally")
elif status == 0:
    print("The machine is turned off.")