import csv

# Importowanie funkcji pomocniczych zewnętrznego modułu
from helpers import generate_processes, sort_by_arrival_time, read_from_csv


def FCFS(processes):
    # Symulacja algorytmu FCFS
    print("\nSymulacja FCFS:\n")
    
    current_time = 0
    results = []
    total_waiting_time = 0
    total_turnaround_time = 0
    total_finish_time = 0

    # Iteracja przez posortowane procesy
    for process in processes:
        pid, arrival_time, burst_time = process

        # Obliczenie czasu początkowego, czasu oczekiwania, czasu zakończenia i czasu przebiegu
        start_time = max(current_time, arrival_time)
        waiting_time = start_time - arrival_time
        finish_time = start_time + burst_time
        turnaround_time = finish_time - arrival_time

        # Aktualizacja bieżącego czasu
        current_time = finish_time

        # Sumowanie czasów dla obliczenia średnich wartości
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_finish_time += finish_time

        # Dodanie wyników do listy wynikowej i wydrukowanie szczegółów procesu
        results.append((pid, start_time, waiting_time, finish_time, turnaround_time))
        print(
            f"PID: {pid} | Start time: {start_time} | Waiting time: {waiting_time} | Finish time: {finish_time} | Turnaround time: {turnaround_time}")

    # Obliczenie średnich wartości dla FCFS
    num_processes = len(processes)
    avg_waiting_time = total_waiting_time / num_processes
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_finish_time = total_finish_time / num_processes

    # Wydrukowanie średnich wartości dla FCFS
    print(
        f"Średni czas oczekiwania: {avg_waiting_time} | Średni czas przetwarzania: {avg_turnaround_time} | Średni czas ukończenia: {avg_finish_time}")

    return results, avg_waiting_time, avg_turnaround_time, avg_finish_time


def SJF(processes):
    # Symulacja algorytmu SJF
    print("\nSymulacja SJF:\n")
    
    current_time = 0
    completed_processes = []
    results = []
    total_waiting_time = 0
    total_turnaround_time = 0
    total_finish_time = 0

    # Pętla główna algorytmu SJF
    while processes:
        arrived_processes = [p for p in processes if p[1] <= current_time]

        if not arrived_processes:
            current_time = processes[0][1]
            arrived_processes = [p for p in processes if p[1] <= current_time]

        shortest_burst_time_process = min(arrived_processes, key=lambda x: x[2])
        processes.remove(shortest_burst_time_process)

        pid, arrival_time, burst_time = shortest_burst_time_process

        # Obliczenie czasu początkowego, czasu oczekiwania, czasu zakończenia i czasu przebiegu
        start_time = max(current_time, arrival_time)
        waiting_time = start_time - arrival_time
        finish_time = start_time + burst_time
        turnaround_time = finish_time - arrival_time

        # Aktualizacja bieżącego czasu
        current_time = finish_time

        # Sumowanie czasów dla obliczenia średnich wartości
        total_waiting_time += waiting_time
        total_turnaround_time += turnaround_time
        total_finish_time += finish_time

        # Dodanie wyników do listy wynikowej i wydrukowanie szczegółów procesu
        completed_processes.append((pid, start_time, waiting_time, finish_time, turnaround_time))

    # Wydrukowanie wyników dla każdego procesu w SJF
    for process in completed_processes:
        pid, start_time, waiting_time, finish_time, turnaround_time = process
        results.append((pid, start_time, waiting_time, finish_time, turnaround_time))
        print(
            f"PID: {pid} | Start time: {start_time} | Waiting time: {waiting_time} | Finish time: {finish_time} | Turnaround time: {turnaround_time}")

    # Obliczenie średnich wartości dla SJF
    num_processes = len(completed_processes)
    avg_waiting_time = total_waiting_time / num_processes
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_finish_time = total_finish_time / num_processes

    # Wydrukowanie średnich wartości dla SJF
    print(f"Średni czas oczekiwania: {avg_waiting_time} | Średni czas przetwarzania: {avg_turnaround_time} | Średni czas ukończenia: {avg_finish_time}")

    return results, avg_waiting_time, avg_turnaround_time, avg_finish_time


def save_results_to_csv(filename, fcfs_results, sjf_results):
    # Zapis wyników do pliku CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Zapis wyników dla FCFS
        writer.writerow(["FCFS Results"])
        writer.writerow(["PID", "Start time", "Waiting time", "Finish time", "Turnaround time"])
        writer.writerows(fcfs_results[0])

        # Zapis średnich wartości dla FCFS
        writer.writerow([])
        writer.writerow(["FCFS Averages"])
        writer.writerow(["Average Waiting Time", "Average Turnaround Time", "Average Finish Time"])
        writer.writerow([fcfs_results[1], fcfs_results[2], fcfs_results[3]])

        # Dodanie pustego wiersza dla separacji
        writer.writerow([])

        # Zapis wyników dla SJF
        writer.writerow(["SJF Results"])
        writer.writerow(["PID", "Start time", "Waiting time", "Finish time", "Turnaround time"])
        writer.writerows(sjf_results[0])

        # Zapis średnich wartości dla SJF
        writer.writerow([])
        writer.writerow(["SJF Averages"])
        writer.writerow(["Average Waiting Time", "Average Turnaround Time", "Average Finish Time"])
        writer.writerow([sjf_results[1], sjf_results[2], sjf_results[3]])


if __name__ == '__main__':
    choise = int(input("1. Wygeneruj procesy \n2. Wczytaj procesy z pliku procesy.csv\n"))

    processes = []

    if choise == 1:
        qty = int(input("Ilość procesów: "))
        processes = generate_processes(qty)
    elif choise == 2:
        processes = read_from_csv("procesy.csv")
    else:
        exit()

    sortedProcesses = sort_by_arrival_time(processes)

    print("Lista procesów:\n")
    for process in processes:
        pid, arrival_time, burst_time = process
        print(f"PID: {pid} | Arrival time: {arrival_time} | Burst time: {burst_time}")

    # Wywołanie funkcji FCFS i SJF
    fcfs_results = FCFS(sortedProcesses)
    sjf_results = SJF(sortedProcesses.copy())

    # Zapis wyników do pliku CSV
    save_results_to_csv("cpu_results.csv", fcfs_results, sjf_results)
