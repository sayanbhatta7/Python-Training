#actions, there are 6 built in actions for arguments
#store,store_const,(store_false,store_true),append[]
# append_const,version
import argparse

parse= argparse.ArgumentParser(description="test1")

parse.add_argument('-s', action='store',dest='simple_value',help='store simple value')
parse.add_argument('-S', action='store_const',dest='const_value',const='100',help='store const value')
parse.add_argument('-t', action='store_true',default=True,dest='boolen_switch',help='default boolean switch')
parse.add_argument('-f', action='store_false',default=False,dest='boolen_switch',help='default boolean switch')
parse.add_argument('-a', action='append',dest='collection',default=[],help='add repeated  values to list')
parse.add_argument('-A', action='append_const',dest='constant_collection',const='300',help='add diff values to list')
parse.add_argument('--version', action='version',version='1.0')

restlt = parse.parse_args()
print('simple_value: ',restlt.simple_value)
print('const_value: ',restlt.const_value)
print('true_value: ',restlt.boolen_switch)
print('append_value: ',restlt.collection)
print('const_append_value: ',restlt.constant_collection)



