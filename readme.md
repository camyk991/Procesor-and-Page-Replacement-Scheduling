# Simulation of CPU Scheduling and Page Replacement Algorithms


## Description of Testing Procedure

The testing procedure aims to compare the results of different process scheduling algorithms (FCFS and SJF) and page replacement algorithms (FIFO and LRU) using the same input data, which will be fetched from a file. I will compare the average waiting time, processing time, and completion time for the process scheduling algorithms, and for the page replacement algorithms, I will compare the hit rate and page faults.

## Comparison of CPU Scheduling Algorithms

### FCFS (First-Come, First-Served)

FCFS is one of the simplest scheduling algorithms in operating systems. It works on a "first come, first served" basis. Processes are handled in the order they arrive in the queue. Each process added to the queue is placed at the end, and the process at the front of the queue is handled first.

### SJF (Shortest Job First)

SJF, also known as the shortest execution time algorithm, always selects the process with the shortest execution time from the available processes. The main idea of the SJF algorithm is to minimize the average waiting time, making it one of the most efficient process scheduling algorithms.

### Measurements

#### List of Processes:

| PID | Arrival Time | Execution Time |
|-----|--------------|----------------|
| 1   | 0            | 8              |
| 2   | 1            | 4              |
| 3   | 2            | 9              |
| 4   | 3            | 5              |

#### FCFS:

| PID | Start Time | Waiting Time | Completion Time | Processing Time |
|-----|------------|--------------|----------------|-----------------|
| 1   | 0          | 0            | 8              | 8               |
| 2   | 8          | 7            | 12             | 11              |
| 3   | 12         | 10           | 21             | 19              |
| 4   | 21         | 18           | 26             | 23              |

#### SJF:

| PID | Start Time | Waiting Time | Completion Time | Processing Time |
|-----|------------|--------------|----------------|-----------------|
| 1   | 0          | 0            | 8              | 8               |
| 2   | 8          | 7            | 12             | 11              |
| 4   | 12         | 9            | 17             | 14              |
| 3   | 17         | 15           | 26             | 24              |

### Comparison of Average Times for Two Algorithms with Different Numbers of Processes:

| Algorithm | Number of Processes | Average Waiting Time | Average Processing Time | Average Completion Time |
|-----------|---------------------|----------------------|-------------------------|-------------------------|
| FCFS      | 4                   | 8.75                 | 15.25                   | 16.75                   |
| SJF       | 4                   | 7.75                 | 14.25                   | 15.75                   |
| FCFS      | 25                  | 461.96               | 508.4                   | 550.88                  |
| SJF       | 25                  | 333.6                | 380.04                  | 422.52                  |
| FCFS      | 75                  | 1988.6               | 2040.55                 | 2090.28                 |
| SJF       | 75                  | 1290.69              | 1342.64                 | 1392.37                 |
| FCFS      | 125                 | 2930.43              | 2977.91                 | 3026.62                 |
| SJF       | 125                 | 1874.81              | 1922.29                 | 1971.0                  |

The detailed list of processes used for the above simulations can be found in the folder "procesy_pliki".

### Conclusions:

SJF is more efficient compared to FCFS as it minimizes the waiting and processing times. This means that in practical applications where response time and processing speed are critical, the SJF algorithm can provide better results. However, it is worth noting that SJF may be harder to implement in situations where the process durations are not known in advance.

## Comparison of Page Replacement Algorithms

### FIFO (First-In, First-Out)

FIFO is one of the simplest page replacement algorithms in memory management systems. It operates on a "first in, first out" basis. Pages are placed in the queue in the order they are loaded into memory. When a page replacement is needed, the page that has been in memory the longest (at the front of the queue) is removed first. The FIFO algorithm is easy to implement but is not always the most efficient as it does not consider the frequency of page use.

### LRU (Least Recently Used)

LRU is a page replacement algorithm that selects the least recently used page for removal. The main idea of the LRU algorithm is that if a page has not been used for a long time, it is likely not needed in the near future. LRU requires tracking the last usage time of each page, which can be resource-intensive. Despite this, LRU is often more efficient than FIFO as it better adapts to page usage patterns, minimizing page replacements.

### Measurements

| Algorithm | Number of Frames | Number of Pages | Page Faults | Hit Ratio (%) |
|-----------|------------------|-----------------|-------------|---------------|
| FIFO      | 4                | 13              | 7           | 46.15         |
| LRU       | 4                | 13              | 6           | 53.85         |
| FIFO      | 4                | 26              | 17          | 34.62         |
| LRU       | 4                | 26              | 20          | 23.08         |
| FIFO      | 4                | 52              | 34          | 34.62         |
| LRU       | 4                | 52              | 32          | 38.46         |
| FIFO      | 6                | 13              | 7           | 46.15         |
| LRU       | 6                | 13              | 7           | 46.15         |
| FIFO      | 6                | 26              | 10          | 61.54         |
| LRU       | 6                | 26              | 10          | 61.54         |
| FIFO      | 6                | 52              | 16          | 69.23         |
| LRU       | 6                | 52              | 17          | 67.31         |

### Conclusions:

FIFO often achieves stable page fault results but may have a lower hit ratio compared to LRU, especially with smaller sets of pages. LRU generally tends to have fewer page faults and often a higher hit ratio compared to FIFO, making it more efficient for cases where there is a high demand for access to recently used pages.

These findings suggest that in systems where it is possible to predict the duration of processes, it is worth considering the use of the SJF algorithm to increase processing efficiency.