import csv
import time
from os import times


def menu():
    with open('projects.csv', 'r') as f:
        reader = csv.reader(f)
        print("List of Projects:")
        for row in reader:
            print(row[0],":",row[1])

def new_project():
    name = input("Type name of project: ")
    length = 0
    with open('projects.csv', 'r') as f:
        reader = csv.reader(f)
        length = 0
        for row in reader:
            length = length + 1

    with open('projects.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([length, name])

    print(name, "has been created")

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))

def record():
    project_id = input("Type the ID of the project you are starting: ")
    project_name = ""
    with open('projects.csv', 'r') as f:
        reader = csv.reader(f)
        found = False
        for row in reader:
            if row[0] == project_id:
                found = True
                start_time = time.time()
                project_name = row[1]
                break
        if not found:
            print("Project not found")

    input("Currently working on "+project_name+". Press enter to end timer\n")
    end_time = time.time()

    time_elapsed = end_time - start_time

    time_convert(time_elapsed)

    with open('time_log.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([project_id, start_time, end_time])

    print("Entry has been logged")


def main():
    user_input = int(input("Choose an option:\n[0] - Record new entry\n[1] - Print all projects\n[2] - Add new project\n[3] - Exit\n"))

    if user_input == 0:
        record()
    elif user_input == 1:
        menu()
    elif user_input == 2:
        new_project()
    else:
        print("Exiting...")

main()