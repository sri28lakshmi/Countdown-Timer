import time

def iter_countdown_timer(n):
    print(f"Counting down from : {n}")
    while n >= 0:
        print(n)
        time.sleep(1)
        n -= 1
    print("Times up!!")

def recur_countdown_timer(n):
    if n == 0:
        print(n)
    else:
        print(n)
        time.sleep(1)
        return recur_countdown_timer(n - 1)
    print("Times up!!")

def main():
    while True:
        print(" Welcome to COUNTDOWN TIMER!\nPress 1: Countdown by Iteration\nPress 2: Countdown by Recursion\nPress 3: Exit")
        choice = int(input("Enter your choice :"))
        if choice == 1:
            t = int(input("Enter Seconds :"))
            iter_countdown_timer(t)
        elif choice == 2:
            t = int(input("Enter Seconds :"))
            recur_countdown_timer(t)
        elif choice == 3:
            exit()
        else:
            print("Please enter a valid choice")

main()