handle = open('file.type')

di = dict
for line in handle:
    line = line.rstrip
    words = line.split
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])

tmp = list
for k, v in di.items:
    print(k, v)
    newTup = (v, k)
    tmp.append(newTup)
tmp = sorted(tmp, reverse=True)
print('Sorted', tmp[:5])
