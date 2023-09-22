import random

# Define the LFSR
def lfsr_generator(lfsr, tap_positions):
    while True:
        new_bit = sum([lfsr[pos] for pos in tap_positions]) % 2
        yield lfsr[0]
        lfsr = [new_bit] + lfsr[:-1]

# Convert LFSR sequence to a number between 0-100
def lfsr_to_number(gen, num_bits=7):
    return sum([next(gen) * (2 ** i) for i in range(num_bits)])

# Initial LFSR setup
lfsr = [1, 0, 1, 0, 1, 0, 1]
tap_positions = [0, 2, 3, 5]
lfsr_gen = lfsr_generator(lfsr, tap_positions)

# Function to generate dna strands
def generateDNASequence():
    l = ['C', 'A', 'G', 'T']
    res = ""
    for i in range(0, 40):
        res = res + random.choice(l)
    return res

# Function to alter dna strands using the LFSR
def applyGammaRadiation(dna):
    pos = lfsr_to_number(lfsr_gen)
    cdna = ''
    l = ['C', 'A', 'G', 'T']

    if pos > 50:
        changepos = lfsr_to_number(lfsr_gen) % 40
        dl = []
        dl[:0] = dna
        ch = "" + dl[changepos]
        l.remove(ch)
        ms = random.choice(l)
        dl[changepos] = ms
        cdna = ''.join(dl)
    else:
        cdna = dna

    return cdna

# Function to detect mutation
def detectMutation(dna, cdna):
    count = 0
    for x, y in zip(dna, cdna):
        if x == y:
            count = count + 1
        else:
            break
    return count

# Main execution
dna = generateDNASequence()
print(dna + " (Original DNA)")
cdna = applyGammaRadiation(dna)
print(cdna + " (DNA after radiation)")
count = detectMutation(dna, cdna)

if count == 40:
    print("No Mutation detected")
else:
    pos = "^"
    print(pos.rjust(count+1))
    print("Mutation detected at pos =", (count+1))
