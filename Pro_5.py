CAMERA = 1
MICROPHONE = 2
STORAGE = 4
LOCATION = 8

approved_apps = ["coding app, math app, reading app, science app"]

student_name = input("Enter your name: ")
requested_app = input("Enter the app you want to access: ").lower()

print("\n--- Identity Operator Check---")

if type(student_name) is str:
    print("The student name is stored as text")

if type(requested_app) is not int:
    print("The requested app is not stored as number")

print("\n---Membership Operator Check ---")

if requested_app in approved_apps:
    print(requested_app, "is a student approved app")
else:
    print(requested_app, "is not a student approved app")

restricted_apps = ["Gamming app", "Shopping app", "Social Media App"]

if requested_app not in restricted_apps:
    print("App is not in the restricted list")
else:
    print("Access denied because it is restricted")

print("\n---App Perimission Setting---")

student_perimission = CAMERA | MICROPHONE | STORAGE

print("Perimission value:", student_perimission)
print("perimission bits:", bin(student_perimission))

if student_perimission & CAMERA:
    print("Camera perimission : Enabled")
if student_perimission & MICROPHONE:
    print("Microphone perimission : Enabled")
if student_perimission & STORAGE:
    print("Storage perimission : Enabled")
if student_perimission & LOCATION:
    print("Location perimission : Enabled")
else:
    print("Location perimission : Disabled")

print("\n--- Bit Shift Demostration")

next_perimission = CAMERA << 1

print("Camera bit: ", bin(CAMERA))
print("After left shift : ", bin(next_perimission))

previous_perimission = STORAGE >> 1

print("Storage bit :", bin(STORAGE))
print("After Right Shift :", bin(previous_perimission))

print("\n---Final Access Result---")

if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access Granted to ", requested_app)
else:
    print("Access denied to ", requested_app)