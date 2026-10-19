# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'

sequence = [0]

for i in range (1,L+1):
    print(i)
    print(sequence)
    if sequence[i-1] > 0:
        count = 0
        running = True
        while running:
            for num in sequence:
                if num == sequence[i-1]:
                    count += 1
                    if count == 2:
                        running = False
            running = False
        if count < 2:
            sequence.append(sequence[i-1] - i)
    else:
        sequence.append(sequence[i-1] + i)
    

# You may wish to use further output for testing purposes while you develop your code


#[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence