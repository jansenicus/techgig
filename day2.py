# _*_ utf-8

def main():

    x = raw_input()

    def valid(x):
        if len(x) <= 10000:
            v = True
        else:
            v = False
        return v
    
    def get_type(x):
        # it = input type
        it = 'string.'
        if '.' in x:
            try: float(x); it = 'Float.'
            except: pass
        else:
            try: int(x); it = 'Integer.'
            except: pass
        return it

    while True:
        v = valid(x)
        if v: 
            print('Input is of type '+get_type(x))
            break
        else:
            pass

main()