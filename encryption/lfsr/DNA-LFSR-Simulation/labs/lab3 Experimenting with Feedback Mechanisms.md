## Lab 3: Experimenting with Feedback Mechanisms
### Objective:
- Explore how different feedback functions impact LFSR outputs.
### Initialization:

- Review the basic LFSR from Lab 1.
### Tasks:

- Implement three different feedback mechanisms.
- Generate sequences using each feedback mechanism and compare the outputs.
### Evaluation:

- Explain the observed differences in sequences.
- Discuss potential implications of these differences in real-world applications.
---
Terminal Activity:

- Open your terminal.

Launch the Python interpreter:
```bash
$ python
```
Implement three different feedback mechanisms:

```py
def feedback1(lfsr):
    return lfsr[-1] ^ lfsr[0]

def feedback2(lfsr):
    return lfsr[-1] ^ lfsr[1]

def feedback3(lfsr):
    return lfsr[0] ^ lfsr[2]
```
Generate sequences using each feedback mechanism:
```py
lfsr = [1, 0, 1, 0]

for feedback_func in [feedback1, feedback2, feedback3]:
    sequence = []
    for _ in range(10):
        sequence.append(lfsr[0])
        new_bit = feedback_func(lfsr)
        lfsr = [new_bit] + lfsr[:-1]
    print(sequence)
```
---
### Solution using `itertools`

Launch the Python interpreter:
```py
$ python
```
First, you will need to import the itertools library:
```py
import itertools
```
Define the base LFSR and feedback mechanism. For this demonstration, we'll use `itertools.product` to create combinations for feedback positions:

```py
lfsr = [1, 0, 1, 0]

def generalized_feedback(lfsr, positions):
    return sum(itertools.compress(lfsr, positions)) % 2
```
Now, use `itertools.product` to generate a list of feedback mechanisms. Each mechanism will consider different bit positions in the `XOR` operation:

```py
feedback_positions = list(itertools.product([0, 1], repeat=len(lfsr)))
```
`Iterate` through each feedback mechanism to generate sequences:
```py
for positions in feedback_positions:
    sequence = []
    current_lfsr = lfsr.copy()
    for _ in range(10):
        sequence.append(current_lfsr[0])
        new_bit = generalized_feedback(current_lfsr, positions)
        current_lfsr = [new_bit] + current_lfsr[:-1]
    print(f"For positions {positions}: {sequence}")
```
This will display the sequences for each feedback mechanism, showing how different positions in the LFSR influence the generated sequence.

Using itertools, we've not only streamlined the process but also expanded our experimentation to consider all possible feedback mechanisms for our LFSR length. `It's a more exhaustive approach to understanding the dynamics of LFSRs`.

---
### Experimenting with Feedback Mechanisms using iter and next()

Define the LFSR and a simple feedback mechanism:

```py
lfsr = [1, 0, 1, 0]

def feedback(lfsr):
    return lfsr[-1] ^ lfsr[-2]
```
Use the iter function to create an infinite LFSR sequence generator, employing next() to retrieve items:

```py
def lfsr_generator(lfsr, feedback_func):
    while True:
        new_bit = feedback_func(lfsr)
        lfsr = [new_bit] + lfsr[:-1]
        yield lfsr[0]

lfsr_iter = iter(lfsr_generator(lfsr, feedback))
```
Generate a sequence using next():

```py
sequence = [next(lfsr_iter) for _ in range(10)]
print(sequence)
```
By incorporating iter and next(), we've provided a dynamic way to explore the LFSR's sequences in real-time, offering learners a more flexible approach to experimentation.