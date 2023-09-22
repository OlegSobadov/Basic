## Lab 1: Basic LFSR Implementation
### Objective:
- Implement a basic LFSR and generate a binary sequence.

### Initialization:

- Set up a 4-bit LFSR with an initial seed.
- Define a feedback function that uses the XOR operation on the last two bits.
### Tasks:

- Generate and print a sequence of 20 bits.
- Change the seed and observe the new sequence.
### Evaluation:

- Explain how changing the seed affects the sequence.
- Discuss potential applications of this sequence.

---

Terminal Activity:

- Open your terminal.

Launch the Python interpreter:

```bash
$ python
```
Set up your basic 4-bit LFSR and define the feedback function:

```bash
lfsr = [1, 0, 1, 0]

def feedback(lfsr):
    return lfsr[-1] ^ lfsr[-2]
```
Generate a sequence of 20 bits:

```bash
for _ in range(20):
    print(lfsr[0], end="")
    new_bit = feedback(lfsr)
    lfsr = [new_bit] + lfsr[:-1]
```