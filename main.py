import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="This script does nothing fancy",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("in_file", type=str, help="Input filename")
    parser.add_argument("out_file", type=str, help="Output filename")
    return parser.parse_args()

if __name__ == '__main__':
    x = 0
    for i in range(10000):
        for j in range(1000):
            x += i
    print(x)

    args = parse_args()
    in_file = args.in_file
    out_file = args.out_file

    f = open(in_file, 'r')
    lines = f.readlines()
    f.close()

    f = open(out_file, 'w')
    for line in lines:
        line = line.strip()
        f.write('HAHA ' + line + '\n')
    f.close()

    l = []
    for i in range(100000):
        l.append( str(i) )
    l.sort()
    print(l[0])

    print('DONE!')
