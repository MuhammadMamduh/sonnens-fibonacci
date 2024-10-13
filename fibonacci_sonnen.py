from typing import List

def is_even(n) -> bool:
    if n % 2 == 0:
        return True
    else:
        return False
    
def fibonacci(n: int) -> List:
    abs_n = abs(n)
    result = [0]
    if n == 0:
        print(result)
        return result[-1]

    result.append(1)
    if n == -1 or n == 1:
        print(result)
        return result[-1]

    # +ve
    for i in range(2, abs_n + 1):
        item = abs(result[i - 1]) + abs(result[i - 2])
        # print("item: " + str(item))
        if n > 0: # n is +ve
            result.append(item)
        else: # n is -ve
            if (is_even(i)):
                result.append(item * -1)
            else:
                result.append(item)
    print(result[:-1])
    return result[-1] # last item in the list



def main():
    print("Fib(0): " + str(fibonacci(0)))
    print("=========")
    print("Fib(1): " + str(fibonacci(1)))
    print("=========")
    print("Fib(2): " + str(fibonacci(2)))
    print("=========")
    print("Fib(3): " + str(fibonacci(3)))
    print("=========")
    print("Fib(4): " + str(fibonacci(4)))
    print("=========")
    print("Fib(5): " + str(fibonacci(5)))
    print("=========")
    print("Fib(6): " + str(fibonacci(6)))
    print("=========")
    print("Fib(7): " + str(fibonacci(7)))
    print("=========")
    print("Fib(8): " + str(fibonacci(8)))
    print("=========")

    print("Fib(-1): " + str(fibonacci(-1)))
    print("=========")
    print("Fib(-2): " + str(fibonacci(-2)))
    print("=========")
    print("Fib(-3): " + str(fibonacci(-3)))
    print("=========")
    print("Fib(-4): " + str(fibonacci(-4)))
    print("=========")
    print("Fib(-5): " + str(fibonacci(-5)))
    print("=========")
    print("Fib(-6): " + str(fibonacci(-6)))
    print("=========")
    print("Fib(-7): " + str(fibonacci(-7)))
    print("=========")
    print("Fib(-8): " + str(fibonacci(-8)))
    print("=========")


if __name__ == "__main__":
    main()