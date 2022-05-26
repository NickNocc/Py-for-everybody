string = 'X-DSPAM-Confidence: 0.8475'

colPos = string.find(':')
piece = string[colPos+1:]
value = float(piece)
print(piece)
