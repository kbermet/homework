seconds = int(input('Enter time in seconds: '))
h = (seconds / 3600) % 24
m = ( seconds /60 ) %60
s = seconds % 60

print('%02d:%02d:%02d' % (h, m, s))

