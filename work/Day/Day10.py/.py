count = 0
is_running = True

while is_running:
    print("Count:", count)
    count += 1
    if count >= 5:
        is_running = False

print("Loop has ended")
