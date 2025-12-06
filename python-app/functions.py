# functions.py
def safe_int_input(prompt):
    """Get an integer from the user safely."""
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        else:
            print("❌ Please enter a valid number.")

def add_exercise(exercises):
    name = input("Enter exercise name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    duration = safe_int_input("Enter duration (minutes): ")
    calories = safe_int_input("Enter calories burned: ")

    exercises.append({
        "name": name,
        "duration": duration,
        "calories": calories
    })
    print(f"✅ {name} added!")

def remove_exercise(exercises):
    if not exercises:
        print("⚠ No exercises to remove.")
        return

    name = input("Enter exercise name to remove: ").strip()
    for ex in exercises:
        if ex["name"].lower() == name.lower():
            exercises.remove(ex)
            print(f"✅ {name} removed!")
            return
    print("❌ Exercise not found.")

def edit_exercise(exercises):
    if not exercises:
        print("⚠ No exercises to edit.")
        return

    name = input("Enter exercise name to edit: ").strip()
    for ex in exercises:
        if ex["name"].lower() == name.lower():
            ex["duration"] = safe_int_input("New duration (minutes): ")
            ex["calories"] = safe_int_input("New calories burned: ")
            print(f"✅ {name} updated!")
            return
    print("❌ Exercise not found.")

def display_exercises(exercises):
    if not exercises:
        print("⚠ No exercises recorded.")
        return
    print("\n📋 Your Exercises:")
    for ex in exercises:
        print(f"- {ex['name']} | {ex['duration']} min | {ex['calories']} cal")

def sort_exercises(exercises):
    if not exercises:
        print("⚠ No exercises to sort.")
        return

    key = input("Sort by 'name', 'duration', or 'calories': ").lower()
    if key in ["name", "duration", "calories"]:
        exercises.sort(key=lambda x: x[key])
        print("✅ Exercises sorted!")
    else:
        print("❌ Invalid sort key.")

def total_calories(exercises):
    if not exercises:
        print("⚠ No exercises recorded.")
        return
    total = sum(ex["calories"] for ex in exercises)
    print(f"🔥 Total calories burned: {total}")
