# Thursday 26/01/2023 - Morning Exercises - Take a csv file, create functions that open, transform and write into a
# new csv file
import csv


def open_file(file_name):
    with open(file_name) as csvfile:
        csvreader = csv.reader(csvfile)
        new_list = []
        for line in csvreader:
            new_list.append(line)
        return new_list


def transform_csv(file_name):
    user_details = open_file(file_name)
    new_list = []
    for sublist in user_details:
        del sublist[0]
        del sublist[-2]
    print(user_details)

    return user_details


def write_csv(old_file, new_file):
    old = transform_csv(old_file)  # gives user_details from transform_csv func
    with open(new_file, "w") as old1:
        writer = csv.writer(old1)
        for row in old:
            writer.writerow(row)


write_csv("user_details.csv", "output.csv")
