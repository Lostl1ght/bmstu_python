array = [int(x) for x in input().split()]

max_seq = []
seq = []
previous = array[0]
for x in array:
    if x > previous:
        seq.append(x)
    else:
        if len(seq) > len(max_seq):
            max_seq = seq
        seq = [x]
    previous = x

if len(seq) > len(max_seq):
    max_seq = seq

print(max_seq)
