import csv

# Importowanie funkcji pomocniczych zewnętrznego modułu
from helpers import read_from_csv, generate_pages


def fifo_page_replacement(page_requests, frame_size):
    # Inicjalizacja zmiennych dla algorytmu FIFO
    page_frame = []
    page_faults = 0
    page_hits = 0
    current_time = 0

    # Iteracja przez żądania stron
    for page in page_requests:
        if page in page_frame:
            # Obsługa trafienia strony w ramce
            page_hits += 1
        else:
            # Obsługa błędu strony (miss)
            page_faults += 1
            if len(page_frame) < frame_size:
                # Jeśli ramka nie jest pełna, dodaj stronę
                page_frame.append(page)
            else:
                # Jeśli ramka jest pełna, usuń pierwszy element i dodaj nową stronę
                page_frame.pop(0)
                page_frame.append(page)

        # Wyświetlenie stanu ramki w danym momencie
        print(f"Czas: {current_time} | Strona: {page} | Ramka: {page_frame}")
        current_time += 1

    # Obliczenie wskaźników trafień i błędów stron
    total_requests = len(page_requests)
    hit_ratio = (page_hits / total_requests) * 100
    miss_ratio = (page_faults / total_requests) * 100

    return page_faults, hit_ratio, miss_ratio


def lru_page_replacement(page_requests, frame_size):
    # Inicjalizacja zmiennych dla algorytmu LRU
    page_frame = []
    page_usage = []
    page_faults = 0
    page_hits = 0
    current_time = 0

    # Iteracja przez żądania stron
    for page in page_requests:
        if page in page_frame:
            # Obsługa trafienia strony w ramce
            page_hits += 1

            # Aktualizacja listy używanych stron (LRU)
            page_usage.remove(page)
            page_usage.append(page)
        else:
            # Obsługa błędu strony (miss)
            page_faults += 1
            if len(page_frame) < frame_size:
                # Jeśli ramka nie jest pełna, dodaj stronę
                page_frame.append(page)
            else:
                # Jeśli ramka jest pełna, usuń najstarszą stronę i dodaj nową stronę
                lru_page = page_usage.pop(0)
                page_frame.remove(lru_page)
                page_frame.append(page)

            # Dodanie strony do listy używanych stron (LRU)
            page_usage.append(page)

        # Wyświetlenie stanu ramki w danym momencie
        print(f"Czas: {current_time} | Strona: {page} | Ramka: {page_frame}")
        current_time += 1

    # Obliczenie wskaźników trafień i błędów stron
    total_requests = len(page_requests)
    hit_ratio = (page_hits / total_requests) * 100
    miss_ratio = (page_faults / total_requests) * 100

    return page_faults, hit_ratio, miss_ratio


def save_results(filename, page_requests, frame_size, fifo_results, lru_results):
    # Zapis wyników do pliku tekstowego
    with open(filename, mode='w') as file:
        file.write("Żądania stron: " + str(page_requests) + "\n")
        file.write("Rozmiar ramki: " + str(frame_size) + "\n\n")

        file.write("Wyniki FIFO\n")
        file.write("Błędy stron: " + str(fifo_results[0]) + "\n")
        file.write("Hit Ratio: " + f"{fifo_results[1]:.2f}" + "\n")
        file.write("Miss Ratio: " + f"{fifo_results[2]:.2f}" + "\n\n")

        file.write("\n")

        file.write("Wyniki LRU\n")
        file.write("Błędy stron: " + str(lru_results[0]) + "\n")
        file.write("Hit Ratio: " + f"{lru_results[1]:.2f}" + "\n")
        file.write("Miss Ratio: " + f"{lru_results[2]:.2f}" + "\n\n")


if __name__ == '__main__':
    # Wybór opcji przez użytkownika
    choise = int(input("1. Wygeneruj strony \n2. Wczytaj strony z pliku\n"))

    pages = []

    if choise == 1:
        # Generowanie stron
        qty = int(input("Ilość stron: "))
        pages = generate_pages(qty)
    elif choise == 2:
        # Wczytywanie stron z pliku
        pages = read_from_csv("pages.txt")
    else:
        exit()

    # Wprowadzenie rozmiaru ramki przez użytkownika
    frame_size = int(input("Wprowadź ilość ramek: "))

    # Wyświetlenie wprowadzonych danych
    print(f"Strony: {pages}")
    print(f"Rozmiar ramki: {frame_size}\n")

    # Uruchomienie algorytmów FIFO i LRU
    print("\nZastępowanie stron FIFO:")
    fifo_results = fifo_page_replacement(pages, frame_size)
    print(f"\nCałkowita liczba błędów stron: {fifo_results[0]}")
    print(f"Hit Ratio: {fifo_results[1]:.2f}")
    print(f"Miss Ratio: {fifo_results[2]:.2f}")

    print("\nZastępowanie stron LRU:")
    lru_results = lru_page_replacement(pages, frame_size)
    print(f"\nCałkowita liczba błędów stron: {lru_results[0]}")
    print(f"Hit Ratio: {lru_results[1]:.2f}")
    print(f"Miss Ratio: {lru_results[2]:.2f}")

    # Zapis wyników do pliku
    save_results("ram_results.txt", pages, frame_size, fifo_results, lru_results)
