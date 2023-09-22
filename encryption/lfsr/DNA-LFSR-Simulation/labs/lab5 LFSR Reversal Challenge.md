## Lab 5: LFSR Reversal Challenge
### Objective: 
- Understand the challenges in reversing LFSR transformations and attempt to reverse-engineer given sequences.

### Initialization:

- Review LFSR processing and the concept of feedback functions.
### Tasks:

- Given a series of LFSR outputs (without knowledge of the seeds or feedback functions used), attempt to reverse-engineer and determine the original inputs or the feedback functions applied.
- Implement any discovered feedback functions and verify their accuracy.
### Evaluation:

- Reflect on the challenges faced during the reversal attempts.
- Discuss the security implications of LFSRs when used in cryptographic contexts based on the lab's findings.
---
Terminal Activity:

- Open your terminal.

Launch the Python interpreter:
```bash
$ python
```
Implement a basic reverse LFSR function:

```py
def reverse_lfsr(binary_seq, lfsr):
    output = []
    for bit in reversed(binary_seq):
        original_bit = int(bit) ^ feedback(lfsr)
        output.append(str(original_bit))
        lfsr = lfsr[1:] + [original_bit]
    return ''.join(reversed(output))
```
Attempt to reverse an LFSR-processed sequence:

```py
original = text_to_binary("SECRET")
processed = lfsr_process(original, [1, 0, 1, 0])
reversed_seq = reverse_lfsr(processed, [1, 0, 1, 0])
print(binary_to_text(reversed_seq))
```