import argparse

parse= argparse.ArgumentParser(description="test")

parse.add_argument('count', action='store',type=int)
parse.add_argument('units', action='store')
parse.add_argument('name', action='store',type=str)
parse.add_argument('color', action='store')
