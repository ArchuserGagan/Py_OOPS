from collections.abc import Callable


# lets say we have a function that takes another function as in put we will without callable our
#editor wont give us error while func call so it is ambigious so you use callable like used below


def printint(n:int) -> None:
    print(f'here is the : {n}')


def run(func: Callable[[int],None], n:int) -> None:
    func(n)


run(func=printint, n=5)
run(func=printint, n=a) #here we get the squigally