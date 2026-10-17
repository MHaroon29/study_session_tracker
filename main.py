import tracker

def main():
    while True:
        print("\n--- Study Session Tracker Main Menu ---")
        print("1. Add Study Session")
        print("2. View All Sessions")
        print("3. View Summary Statistics")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            tracker.add_session()
        elif choice == '2':
            tracker.view_all()
        elif choice == '3':
            tracker.view_summary()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
