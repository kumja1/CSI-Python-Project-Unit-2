from typing import Generator


def get_greater_or_less(num, compareNum):
    return "is_" + ("greater_than" if float(num) > compareNum else "less_than")

def collect(array,callback):
    results = []
    for item in array:
        if (callback(item)):
            results.append(item)
    return results

def dict_has_key(dict,value):
    return value in dict.keys()

# class Range:  # Got this from stack_overflow
# 
#    def __init__(self, end, start=0):
#        self.start = start
#        self.end = end
# 
#    def __iter__(self):
#        return self
# 
#    def __next__(self):
#        while self.start != self.end:
#            self.start
#            self.start += 1
# 
#    def jump_to(self, start):
#        self.start = start


def is_dict(any):
    try:
        dict(any)
        return True
    except:
        return False


def is_int(num):
    try:
        int(num)
        return True
    except:
        return False


# Jesse N - Custom Generator Class
class RangedGenerator(Generator):
    def __init__(self, array, start=0):
        self.start = start
        self.array = array
        self.end = len(array)

    def __next__(self):
        try:
            return self.next()
        except:
            self.throw()

    def next(self):
        ++self.start
        return self.array[self.start]

    def send(self, num):
        self.start = self.start + num

    def throw(e):
        raise StopIteration

    def set_array(self, array):
        self.array = array
