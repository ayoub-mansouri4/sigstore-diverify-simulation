import time
import random
from typing import List, Dict, Tuple
import matplotlib.pyplot as plt

# Simule la signature classique
def regular_sigstore_sign() -> float:
    start_time = time.time()
    time.sleep(random.uniform(3.2, 3.3))  # Simulated signing time
    return time.time() - start_time

# Simule la signature avec DiVerify
def divery_sign() -> Tuple[float, float, float]:
    start_time = time.time()
    # Simulate verification with multiple IdPs
    system_time_start = time.time()
    for _ in range(3):  # Example: 3 IdPs
        time.sleep(random.uniform(0.2, 0.3))  # Simulated request time
    system_time = time.time() - system_time_start

    # Simulate signing
    signing_time_start = time.time()
    time.sleep(random.uniform(3.2, 3.3))  # Simulated signing time
    signing_time = time.time() - signing_time_start

    return signing_time, system_time, time.time() - start_time

# Effectue des tests sur 20 itérations
def benchmark(num_runs: int = 20) -> Tuple[List[Dict[str, float]], List[Dict[str, float]]]:
    regular_results = []
    divery_results = []

    for _ in range(num_runs):
        # Regular Sigstore
        regular_time = regular_sigstore_sign()
        regular_results.append({"signing_time": regular_time, "total_time": regular_time})

        # Sigstore + DiVerify
        signing_time, system_time, total_time = divery_sign()
        divery_results.append({
            "signing_time": signing_time,
            "system_time": system_time,
            "total_time": total_time,
        })

    return regular_results, divery_results

# Affiche les résultats et génère un graphique
def display_results_and_graph(regular_results: List[Dict[str, float]], divery_results: List[Dict[str, float]]) -> None:
    """
    Display the average results of Regular Sigstore and Sigstore + DiVerify,
    and visualize the results using a bar chart.
    """
    # Compute averages
    def compute_averages(results: List[Dict[str, float]]) -> Tuple[float, float, float]:
        signing_avg = sum(r["signing_time"] for r in results) / len(results)
        system_avg = sum(r.get("system_time", 0) for r in results) / len(results)
        total_avg = sum(r["total_time"] for r in results) / len(results)
        return signing_avg, system_avg, total_avg

    regular_averages = compute_averages(regular_results)
    divery_averages = compute_averages(divery_results)

    # Print averages
    print("Benchmark Results")
    print("=" * 30)
    print(f"Regular Sigstore: Signing = {regular_averages[0]:.2f}s, "
          f"System = {regular_averages[1]:.2f}s, Total = {regular_averages[2]:.2f}s")
    print(f"Sigstore + DiVerify: Signing = {divery_averages[0]:.2f}s, "
          f"System = {divery_averages[1]:.2f}s, Total = {divery_averages[2]:.2f}s")
    print("=" * 30)

    # Create bar chart
    labels = ['Signing Time', 'System Time', 'Total Time']
    regular_values = list(regular_averages)
    divery_values = list(divery_averages)
    x = range(len(labels))

    plt.bar(x, regular_values, width=0.4, label='Regular Sigstore', color='blue', align='center')
    plt.bar([p + 0.4 for p in x], divery_values, width=0.4, label='Sigstore + DiVerify', color='orange', align='center')

    # Customize chart
    plt.xticks([p + 0.2 for p in x], labels)
    plt.ylabel('Time (seconds)')
    plt.title('Performance Comparison: Regular Sigstore vs Sigstore + DiVerify')
    plt.legend()

    # Display chart
    plt.show()

# Main execution
if __name__ == "__main__":
    regular_results, divery_results = benchmark()
    display_results_and_graph(regular_results, divery_results)
