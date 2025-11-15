import time
import math


def calculate_factorial(n, name):
    """
    function to calculate factorial and print start/finish messages
    """
    print(f"{name}: Starting {n}!")
    math.factorial(n)
    print(f"{name}: Finished {n}!")


def run_round(round_num):
    """
    run one round of sequential factorial calculations
    """
    print(f"\nRound {round_num}:")

    start_ns = time.perf_counter_ns()  # start timer

    # sequential calculation
    calculate_factorial(50, "Calc-50")
    calculate_factorial(100, "Calc-100")
    calculate_factorial(200, "Calc-200")

    elapsed_ns = time.perf_counter_ns() - start_ns
    print(f"Round {round_num} time: {elapsed_ns:,} ns ({elapsed_ns / 1_000_000:.4f} ms)")
    return elapsed_ns


def main():
    total_rounds = 10
    times = []

    for i in range(1, total_rounds + 1):
        times.append(run_round(i))

    avg_ns = sum(times) / len(times)
    print(f"\nAverage time over {total_rounds} rounds: {avg_ns:,} ns ({avg_ns / 1_000_000:.4f} ms)")


if __name__ == "__main__":
    main()
