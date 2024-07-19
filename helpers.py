import random
import csv


def generate_processes(n):
    processes = []

    for i in range(0, n):
        arrival_time = random.randint(0, 100)
        burst_time = random.randint(0, 100)

        process = [i, arrival_time, burst_time]
        processes.append(process)

    return processes


def sort_by_arrival_time(processes):
    return sorted(processes, key=lambda x: x[1])


def read_from_csv(file):
    processes = []
    with open(file) as csvfile:
        lines = csv.reader(csvfile)

        for row in lines:

            process = [int(value) for value in row]
            processes.append(process)

    return processes


def generate_pages(amount):
    pages = []
    for i in range(amount):
        i = random.randint(0, 7)
        pages.append(i)

    return pages
