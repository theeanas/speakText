N = 10

# make chunks ... also, who cares about efficiency?!
for i in range(N):
    text = open(f"texts/{i}.txt")
    lines = text.readlines()
    # you're speaking Arabic, so the number of tokens is the number of chars.
    j = 0
    while True:
        if j == len(lines) - 1:
            break

        if len(lines[j]) + len(lines[j + 1]) < 3000:
            s1 = lines.pop(j)
            s1 = s1.rstrip(s1[-1])
            s1 += ' '

            s2 = lines.pop(j)
            s2 = s2.rstrip(s2[-1])
            s2 += ' '

            lines.insert(j, s1 + s2)
        else: j += 1

    # now, lines should contain chunks
    chunk = open(f"chunks/chunk{i}.txt", "w")
    for line in lines:
        chunk.write(line)
        chunk.write('\n')

    chunk.close()

