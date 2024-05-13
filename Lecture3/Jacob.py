import pprint

class Jacob:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def print_sum(self):
        print(__name__)
        print(self.a+self.b)

def fun(a, b, c, *args, **kwargs):
    sum = a+b+c
    for i in args:
        sum += i
        
    sum += kwargs["first"]
    sum += kwargs["second"]
    sum += kwargs["third"]
    print(sum)
    
    return sum

if __name__ == '__main__':
    print("Hello world!")

#    print(fun(1,2,3, 4, 5, 6, 7, 8, 9, first=4, second=5, third=10))
    j = Jacob(1,2)
    j.print_sum()

    postal = {'guldheden':41323,'Munkedal':45592, 'person':j, 'tuple':(123,234), 5:4, "test":"This is a very looooooong string that has some interresting story to it. But now my creativity is running out, so i dont really know what more to write"}
    """
    print(postal['guldheden'])
    print(postal['tuple'])
    print(postal[5])
    print(postal.keys())
    print(postal.values())
    print(postal.items())
    print(postal['Munkedal'])
    """
    
    print("Print\n========================================")
    print(postal)
    print("\nPPrint\n========================================")
    pprint.pprint(postal, width=45)
    
    set = {1,2,3,4,3,3,2}
#    print(set)