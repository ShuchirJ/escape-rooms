import os
import glob

ROOMS_FOLDER = "rooms"
room_files = sorted(glob.glob(os.path.join(ROOMS_FOLDER, "*.py")))

if not room_files:
    print(f"No room files found in '{ROOMS_FOLDER}/' folder.")
    exit()

print("[1] Attempt to Escape\n[2] Try a Specific Room\nEnter an option (1 or 2): ", end="")
option = input().strip()
if option == "2":
    possible_rooms = [os.path.basename(f) for f in room_files]
    print(f"Available rooms: {', '.join(possible_rooms)}")
    print("Enter the name of the room you want to try (e.g., 'room1.py'): ", end="")
    chosen_room = input().strip()
    if chosen_room in possible_rooms:
        room_files = [os.path.join(ROOMS_FOLDER, chosen_room)]
    else:
        print(f"Room '{chosen_room}' not found. Exiting.")
        exit()

print(f"  You have {len(room_files)} room(s) to tackle.")
print("  Have fun!")
print("_" * 50)
print()


for i, room_file in enumerate(room_files):
    room_name = os.path.basename(room_file)

    print()
    print(f"[Room {i + 1} of {len(room_files)}]")
    print()

    namespace = {
        "escaped": False,
    }

    try:
        with open(room_file, "r") as f:
            code = f.read()
        exec(code, namespace)

    except SystemExit:
        print()

    except Exception as e:
        # If a room crashes, skip it rather than breaking the whole game
        print()
        print(f"[ERROR in {room_name}: {e}]")
        print("This room has a bug — skipping it.")
        continue

    # Read results back from the room
    escaped = namespace.get("escaped", False)

    if not escaped:
        print()
        print("=" * 50)
        print("           GAME OVER")
        print("=" * 50)
        print(f"  You made it through {i} of {len(room_files)} room(s) :(")
        print("=" * 50)
        break


else:
    print()
    print("_" * 50)
    print("        YOU ESCAPED!!")