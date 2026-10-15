

def split_and_join(line):
    # write your code here
    sp=line.split()
    join2="-".join(sp)
    return join2

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
