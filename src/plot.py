import csv
import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def load_data(csv_path):
    data = []
    with open(csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["M"] = int(row["M"])
            row["N"] = int(row["N"])
            row["ratio"] = float(row["ratio"])
            row["time_sec"] = float(row["time_sec"])
            data.append(row)
    return data

def plot_scenario(data, scenario_name, x_key, x_label, title, filename):
    filtered = [row for row in data if row["scenario"] == scenario_name]
    algorithms = {}
    for row in filtered:
        alg = row["algorithm"]
        if alg not in algorithms:
            algorithms[alg] = {"x": [], "y": []}
        algorithms[alg]["x"].append(row[x_key])
        algorithms[alg]["y"].append(row["time_sec"])
    
    plt.figure(figsize=(9, 5), dpi=120)
    styles = {
        "two_pointers": ("#ff7f0e", "s", "Два указателя"),
        "binary_search": ("#1f77b4", "o", "Бинарный поиск"),
        "exponential": ("#d62728", "^", "Экспоненциальный"),
        "double_binary": ("#2ca02c", "D", "Двойной бинарный")
    }
    
    for alg_name, coords in algorithms.items():
        color, marker, label = styles.get(alg_name, ("black", "x", alg_name))
        plt.plot(coords["x"], coords["y"], marker=marker, color=color, label=label, linewidth=1.5)
    
    plt.xscale("log", base=10)
    plt.yscale("log", base=10)
    plt.xlabel(x_label)
    plt.ylabel("Время (секунды)")
    plt.title(title)
    
    ax = plt.gca()
    ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
    ax.yaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=15))
    ax.xaxis.set_major_formatter(ticker.LogFormatterMathtext(base=10))
    ax.yaxis.set_major_formatter(ticker.LogFormatterMathtext(base=10))
    
    plt.grid(True, which="major", linestyle="-", alpha=0.6)
    plt.grid(True, which="minor", linestyle=":", alpha=0.4)
    plt.legend()
    plt.tight_layout()
    
    os.makedirs("plots", exist_ok=True)
    plt.savefig(f"plots/{filename}", dpi=150)
    plt.close()
    print(f"Сохранен график: {filename}")

def main():
    csv_path = os.path.join("data", "results.csv")
    if not os.path.exists(csv_path):
        print("Ошибка: сначала запустите benchmark.py!")
        return
        
    data = load_data(csv_path)
    
    plot_scenario(data, "M=N", "N", "Размер N (при M = N)", "M = N", "equal_sizes.png")
    
    plot_scenario(data, "M=100", "N", "Размер N (при M = 100)", "M << N (M = 100)", "fixed_m.png")
    
    plot_scenario(data, "Varying ratio", "ratio", "Отношение N / M", "N = 100 000, N/M растёт", "varying_ratio.png")
    
    print("Все графики построены!")

if __name__ == "__main__":
    main()