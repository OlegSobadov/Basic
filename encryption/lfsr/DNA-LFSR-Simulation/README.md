DNA Mutation Simulation using LFSR
This project simulates DNA mutations using a Linear Feedback Shift Register (LFSR) to influence the randomness and determinism of the mutations.

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

DNA mutations are changes that can happen to DNA base sequences. In this simulation, the likelihood and position of a mutation are influenced by an LFSR, introducing a deterministic randomness to the process. This can be useful for controlled simulations where repeatable results are desired.

## Setup
- Prerequisites
- Python 3.x
- Installation

Clone the repository:

```bash
git clone https://github.com/OlegSobadov/DNA-LFSR-Simulation.git
```
Navigate into the cloned directory:

```bash
cd DNA-LFSR-Simulation
```
No additional dependencies are required as the simulation uses the Python standard library.

## Usage
Run the simulation:

```bash
python dna_lfsr_simulation.py
```
This will generate a DNA sequence, apply a possible mutation influenced by the LFSR, and then detect where the mutation occurred, if at all.

## Contribution
Contributions, bug reports, and improvements are very welcome and greatly appreciated. Please fork the repository and then raise a PR for any changes.

## License
This project is licensed under the [MIT License](#). See the [LICENSE](#) file for details.