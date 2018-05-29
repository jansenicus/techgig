# _*_ utf-8

def main():

    x = raw_input()

    def valid(x):
        if len(x) <= 10000:
            v = True
        else:
            v = False

        return v

    while True:
        v = valid(x)
        if v: 
            print('Hello Techgig\n'+(x))
            break
        else:
            x = raw_input()

main()