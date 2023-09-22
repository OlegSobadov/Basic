## Lab 4: Advanced LFSR Processing & Analysis
### Objective: 
- LFSR processing and develop skills for analyzing its outputs.

### Initialization:

- Encode a given problem statement into a binary sequence.
### Tasks:

- Process the binary-encoded problem statement through an LFSR.
- Write a function that analyzes the LFSR output to determine if the problem is "Solvable" or "Not Solvable" (based on specific criteria, e.g., the presence of certain patterns or numbers).
- Test this function on various problem statements.
### Evaluation:

- Reflect on the chosen criteria for solvability and its potential implications.
- Discuss challenges in analyzing LFSR outputs.
---
Terminal Activity:

- Open your terminal.

Launch the Python interpreter:

```bash
$ python
```
Implement the LFSR process function:

```py
def lfsr_process(binary_seq, lfsr):
    output = []
    for bit in binary_seq:
        new_bit = feedback(lfsr)  # Assuming feedback is defined
        output_bit = int(bit) ^ new_bit
        output.append(str(output_bit))
        lfsr = [new_bit] + lfsr[:-1]
    return ''.join(output)
```
Process a binary-encoded problem:

```py
problem = text_to_binary("SOLVABLE")
processed_problem = lfsr_process(problem, [1, 0, 1, 0])
print(processed_problem)
```