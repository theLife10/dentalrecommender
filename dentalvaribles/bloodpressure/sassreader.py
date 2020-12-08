import xport

with open('BPX_J.XPT', 'rb') as f:
    for row in xport.Reader(f):
        print(row)
