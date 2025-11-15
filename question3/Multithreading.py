import threading
import time
import math


def task(n, name, start_times, end_times, index):
    """
    thread function to calculate factorial and print messages
    """
    start_times[index] = time.perf_counter_ns()  # record actual start time
    print(f"{name}: Starting {n}!")
    result = math.factorial(n)
    digits = len(str(result))
    print(f"{name}: Finished {n}! ({digits} digits)")
    end_times[index] = time.perf_counter_ns()  # record actual end time


def run_round(round_num):
    """
    run one round of factorial calculations with 3 threads
    """
    print(f"\nRound {round_num}:")

    start_times = [0, 0, 0]  # store start times for each thread
    end_times = [0, 0, 0]  # store end times for each thread

    # create threads for 50!, 100!, 200!
    thread1 = threading.Thread(target=task, args=(50, "Thread-50", start_times, end_times, 0))
    thread2 = threading.Thread(target=task, args=(100, "Thread-100", start_times, end_times, 1))
    thread3 = threading.Thread(target=task, args=(200, "Thread-200", start_times, end_times, 2))

    # start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # wait for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    # total elapsed time = last thread finish - first thread start
    elapsed_ns = max(end_times) - min(start_times)

    print(f"Round {round_num} time: {elapsed_ns:,} ns ({elapsed_ns / 1_000_000:.4f} ms)")
    return elapsed_ns


def main():
    total_rounds = 10
    times = []

    for i in range(1, total_rounds + 1):
        t = run_round(i)
        times.append(t)

    avg_ns = sum(times) / len(times)
    print(f"\nAverage time over {total_rounds} rounds: {avg_ns:,} ns ({avg_ns / 1_000_000:.4f} ms)")


if __name__ == "__main__":
    main()
