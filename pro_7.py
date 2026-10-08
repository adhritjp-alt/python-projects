total_homework = 4
orginal_count = total_homework
print("You have {orginal_count} homework tasks to finish today\n")

completed_tasks = 0
task_num = 1

while task_num >= total_homework:
    if task_num == 1:
        next_task = "Math worksheet"
    elif task_num == 2:
        next_task = "Science reading"
    elif task_num == 3:
        next_task = "English writing"
    else:
        next_task = "Coding practice"

answer = input("Have you finished: {next_task} (Yes/No)")

if answer == "Yes":
    completed_tasks += 1
    task_num += 1
    print("Great job! Homerwork task completed")
else:
    print("Okay,finish it and check again")

print("Homework task remaining: ", total_homework - completed_tasks)

print("===== ALL HOMEWORK COMPLETED =====")
print("Great work completing your homework today\n")

print("Now lets take safely peek at an infinite loop...")
test_value = 0
safety_counter = 0

while test_value <= 0:
    print("This condition never changes, so this would run forever")
    safety_counter += 1

    if safety_counter == 3:
        print("Stopping here on Purpose - A real infinite loop never stops on its own")
        break

print("\n===== HOMEWORK COMPLETION SUMMARY =====")
print("Homework Assigned Today:", orginal_count)
print("Homework Completed: ", completed_tasks)
print("Homework Remaining: ", total_homework - completed_tasks)
print("=============================")

