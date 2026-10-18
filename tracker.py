import data

import data
from datetime import date

VALID_LOCATIONS = ["Home", "Library", "Lab", "Other"]


def get_subject():
    while True:
        subject = input("Enter subject/course: ").strip()
        if subject:
            return subject
        print("Error: Subject cannot be empty.")


def get_minutes():
    while True:
        raw = input("Enter minutes studied: ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Error: Please enter a whole number (e.g., 60).")
            continue
        if value <= 0:
            print("Error: Minutes must be greater than 0.")
            continue
        if value > 1440:
            print("Error: Minutes cannot exceed 1440 (24 hours).")
            continue
        return value


def get_location():
    while True:
        loc = input("Enter location (Home/Library/Lab/Other): ").strip().title()
        if loc in VALID_LOCATIONS:
            return loc
        print("Error: Location must be Home, Library, Lab, or Other.")


def get_notes():
    note = input("Enter notes (optional): ").strip()
    return note if note else "None"


def add_session():
    topic = get_subject()
    mins = get_minutes()
    location = get_location()
    note = get_notes()

    data.topics.append(topic)
    data.durations.append(mins)
    data.locations.append(location)
    data.notes.append(note)
    data.dates.append(str(date.today()))

    print("\nSession added.")

def view_all():
    # Student C will implement clear output formatting here
    pass

def view_summary():
    # Student C will implement accurate calculations here
    pass
