# N: number of args
# ? 0 or 1 args
# * 0 or all args
# + all and at least one
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--three',nargs=3)

parser.add_argument('--optional',nargs='?')
parser.add_argument('--all',nargs='*',dest='all')
parser.add_argument('--one-or-more',nargs='+')

print(parser.parse_args())
restlt = parser.parse_args()
print('value: ',restlt)