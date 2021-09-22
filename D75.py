import argparse

class emp:
    def __init__(self,number_of_employee):
        self.number_of_employee=number_of_employee
        print("nno emp:",self.number_of_employee)

    def add(selfself,a,b):
        print(a+b)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('number_of_employee',
                        help='employee',type=int)
    parser.add_argument('a',
                        help='employee', type=int)
    parser.add_argument('b',
                        help='employee', type=int)
    args=parser.parse_args()
    g=emp(args.number_of_employee)
    g.add(args.a,args.b)
