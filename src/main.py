from solver import solver

N = None

game = [
    [1, N, N, 0, N, N],
    [N, N, 0, 0, N, 1],
    [N, 0, 0, N, N, 1],
    [N, N, N, N, N, N],
    [0, 0, N, 1, N, N],
    [N, 1, N, N, 0, 0],
]

game1 = [
    [0, N, N, N, 1, N, N, N, 1, N, 0, N],
    [N, N, 1, N, N, N, N, N, N, N, 0, N],
    [N, 0, N, N, N, 1, N, N, N, N, N, N],
    [N, N, N, 1, N, N, N, N, 0, 0, N, N],
    [1, 1, N, N, N, 0, N, N, N, 0, N, N],
    [1, N, N, N, N, N, N, N, N, N, N, N],
    [N, 1, N, N, N, N, N, N, N, 0, N, N],
    [1, 1, N, N, N, N, 0, N, N, N, 1, 0],
    [N, N, N, N, N, 0, N, N, 0, N, 1, N],
    [N, N, 0, N, 1, N, N, N, N, N, N, 1],
    [N, 1, N, 0, N, N, 0, N, N, N, 0, N],
    [0, N, N, N, N, N, N, N, N, 1, N, N],
]

if __name__ == "__main__":
    print(solver(game1))
