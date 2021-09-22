import argparse

parse= argparse.ArgumentParser(description="example")

parse.add_argument('-a',action="store_true",default=False)
parse.add_argument('-b',action="store_true",dest='b')
parse.add_argument('-c',action="store_true",dest='c',type=int)

print(parse.parse_args((['-a','-bbhattacharjee','-c','3'])))