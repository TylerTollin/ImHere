from time import sleep
try:
    import mouse
    import keyboard

    print("Required modules found.")

except:
    print("Required module(s) not found!")
    print("Installing requirements...")
    
    import pip

    pip.main(["install", "mouse"])
    sleep(5)
    pip.main(["install", "keyboard"])

    print()
    print("---------------")
    print("Required modules installed.")
    print("Please restart the program.")
    
    input("Press enter to close...")

def GetMousePos():
    waiting = True
    mousePos = None

    while waiting == True:
        if mouse.is_pressed("left") == True:
            mousePos = mouse.get_position()
            waiting = False

    print(f"Position of click: {str(mousePos)}")

    mouse.unhook_all()

    sleep(1)

    return mousePos

print("Click on the first conversation location...")
posConv1 = GetMousePos()

print()

print("Click on the second conversation location...")
posConv2 = GetMousePos()

print()

waitTime = int(input("Enter number of minutes that you'll be 'here': "))

print()

print("READ ME")
print("Bring Slack to foreground on appropriate screen")
print("To exit early, hold the CONTROL key and press the C key")

print()

print("Starting timer...")

i = 0

while i < waitTime:
    i = i + 1

    if i > 1: 
        sleep(57)
    else:
        sleep(60)

    # This "resets" the mouse position since its all relative
    mouse.move(-9999, -9999)

    mouse.move(posConv1[0], posConv1[1])
    sleep(1)
    mouse.click()

    sleep(1)

    mouse.move(posConv2[0], posConv2[1])
    sleep(1)
    mouse.click()

    print(f"Time elapsed: {str(i)} minutes")

print("Timer complete. Press any key to close...")
keyboard.read_key()