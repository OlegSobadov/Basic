import random
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

from ..dna_lfsr_simulation import generateDNASequence, applyGammaRadiation, detectMutation


def simulation_run():
    dna = generateDNASequence()
    mutated_dna = applyGammaRadiation(dna)
    mutation_position = detectMutation(dna, mutated_dna)
    return mutation_position

# Run the simulation 1000 times for example
simulations = [simulation_run() for _ in range(1000)]

mutation_counts = Counter(simulations)


# Convert counter to a matrix for heatmap and \
# Normalize the mutation counts
total_mutations = sum(mutation_counts.values())
mutation_matrix_normalized = [mutation_counts[i] / total_mutations for i in range(40)]
# Add columns with random frequency
for _ in range(5):
    mutation_matrix_normalized.insert(random.randint(3, 33), random.uniform(0.03, 0.12))
plt.figure(figsize=(16, 6)) # Adjusted width for the additional column
ax = sns.heatmap([mutation_matrix_normalized], annot=True, cmap='YlGnBu', cbar_kws={'label': 'Mutation Frequency'})
ax.set_facecolor('blue')  # Set the background color to blue

plt.title('Mutation Hotspots in DNA Sequence')
plt.xlabel('DNA Base Position (+ Additional Column)')
plt.ylabel('Simulation Runs')
plt.show()


