import numpy as np
from matplotlib import pyplot as plt

from hw2.TravellingSalesmanProblem.solvers.KGB.kgb import KGBSolver
from hw2.TravellingSalesmanProblem.solvers.evolutionary.evolutionary import EvolutionarySolver, ChernobylKids
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simple_hillclimbing import SimpleNeighborSwapHillclimbing, \
    RandomSwapHillclimbing, SegmentReversalHillclimbing
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.simulated_annealing import SimulatedAnnealing
from hw2.TravellingSalesmanProblem.solvers.hillclimbing.tabusearch import TabuSearchHillClimbing


def extract_best_history(solver_result):
    if isinstance(solver_result, dict):
        # solver_result is dict[index, list_of_values]
        # Find the min value at each iteration index across all climbers/individuals
        lists = list(solver_result.values())
        if not lists:
            return np.array([])
        length = len(lists[0])
        best_history = []
        for i in range(length):
            best_history.append(min(lst[i] for lst in lists))
        return np.array(best_history)
    elif isinstance(solver_result, list):
        return np.array(solver_result)
    elif isinstance(solver_result, np.ndarray):
        if solver_result.ndim == 1:
            return solver_result
        else:
            return np.min(solver_result, axis=0)
    return np.array([])


def plot_all(data, iterations):
    # Clear any previous KGB solver global results to ensure fresh run data
    from hw2.TravellingSalesmanProblem.solvers.KGB.kgb import results as kgb_results
    kgb_results.clear()

    solvers = {}

    solvers["Neighbor Swap Hillclimbing"] = SimpleNeighborSwapHillclimbing(problem=data, iterations=iterations, climbers=25)
    solvers["Random Swap Hillclimbing"] = RandomSwapHillclimbing(problem=data, iterations=iterations, climbers=25)
    solvers["Segment Reversal Hillclimbing"] = SegmentReversalHillclimbing(problem=data, iterations=iterations, climbers=25)
    solvers["Tabu Search Hillclimbing"] = TabuSearchHillClimbing(problem=data, iterations=iterations, climbers=25)
    solvers["Simulated Annealing Hillclimbing"] = SimulatedAnnealing(problem=data, iterations=iterations, climbers=25)

    solvers["Genetic algorithm permutation crossover"] = EvolutionarySolver(problem = data, iterations = iterations, population_size = 100, mutation_rate = 0.1, sample_size = 75)
    solvers["Inbreading Genetic Algorithm"] = ChernobylKids(problem = data, iterations = iterations, population_size = 100, mutation_rate = 0.1, sample_size = 15)

    solvers["My Thing"] = KGBSolver(problem = data, iterations = iterations, tree_height = 4, nr_of_children = 4)

    results = {}
    for name, solver in solvers.items():
        print(f"\n[TSP Plotter] Running solver: {name}...")
        raw_r = solver.solve()
        r = extract_best_history(raw_r)
        results[name] = r

    # Create the plot
    fig, ax = plt.subplots(figsize=(13, 8), dpi=300)
    
    # Premium visual design configuration
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8F9FA')
    ax.grid(True, linestyle='--', alpha=0.5, color='#CCCCCC')

    # Distinct premium color palette
    colors = {
        "Neighbor Swap Hillclimbing": "#95A5A6",   # Muted Grey
        "Random Swap Hillclimbing": "#BDC3C7",     # Silver
        "Segment Reversal Hillclimbing": "#2980B9", # Muted Blue
        "Tabu Search Hillclimbing": "#16A085",      # Emerald Teal
        "Simulated Annealing Hillclimbing": "#E67E22", # Amber Orange
        "Genetic algorithm permutation crossover": "#8E44AD", # Royal Purple
        "Inbreading Genetic Algorithm": "#27AE60", # Forest Green
        "My Thing": "#C0392B" # Bold Crimson/Red to highlight the user's custom solver
    }

    # Custom line styles to differentiate solvers
    linestyles = {
        "Neighbor Swap Hillclimbing": ":",
        "Random Swap Hillclimbing": "-.",
        "Segment Reversal Hillclimbing": "--",
        "Tabu Search Hillclimbing": "-",
        "Simulated Annealing Hillclimbing": "-",
        "Genetic algorithm permutation crossover": "--",
        "Inbreading Genetic Algorithm": "--",
        "My Thing": "-"
    }

    best_solver_name = None
    min_final_distance = float('inf')

    for name, history in results.items():
        if len(history) == 0:
            continue
            
        color = colors.get(name, "#34495E")
        linestyle = linestyles.get(name, "-")
        
        # Make the custom "My Thing" solver stand out
        if name == "My Thing":
            linewidth = 3.0
            alpha = 1.0
            zorder = 5
        else:
            linewidth = 1.5
            alpha = 0.8
            zorder = 3

        # Plot the history curve
        x_vals = np.arange(len(history))
        ax.plot(x_vals, history, label=name, color=color, linestyle=linestyle, linewidth=linewidth, alpha=alpha, zorder=zorder)
        
        # Track the best final cost value
        final_val = history[-1]
        if final_val < min_final_distance:
            min_final_distance = final_val
            best_solver_name = name

        # Plot a small dot at the end of the line
        ax.scatter(x_vals[-1], final_val, color=color, s=45, zorder=zorder + 1)
        
        # Add text label showing the final value next to the dot
        ax.text(x_vals[-1] + (iterations * 0.01), final_val, f"{int(final_val)}", 
                color=color, va='center', ha='left', fontsize=9.5, weight='bold' if name == "My Thing" else 'normal')

    # Adjust layout boundaries to fit annotations
    ax.set_xlim(-iterations * 0.02, iterations * 1.12)

    # Titles and Labels
    ax.set_title("TSP Solver Convergence Comparison (berlin52)", fontsize=16, fontweight='bold', pad=18, color='#2C3E50')
    ax.set_xlabel("Iteration / Cycle", fontsize=12, fontweight='bold', labelpad=10, color='#2C3E50')
    ax.set_ylabel("Tour Distance / Cost (Lower is Better)", fontsize=12, fontweight='bold', labelpad=10, color='#2C3E50')

    # Legend
    legend = ax.legend(loc='upper right', frameon=True, facecolor='#FFFFFF', edgecolor='#BDC3C7', fontsize=10)
    legend.get_frame().set_boxstyle("round,pad=0.5")

    # Spines styling
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['left', 'bottom']:
        ax.spines[spine].set_color('#BDC3C7')

    plt.tight_layout()

    # Save to file
    filename = "tsp_solver_comparison_100.png"
    plt.savefig(filename, bbox_inches='tight', dpi=300)
    print(f"\n[TSP Plotter] Comparison plot successfully saved as '{filename}'")

    # Try to display GUI window, catch error if headless
    try:
        plt.show()
    except Exception as e:
        print(f"[TSP Plotter] Could not open GUI window to show plot: {e}")


