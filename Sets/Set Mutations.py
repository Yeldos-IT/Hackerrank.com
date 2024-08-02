_ = input()
A = set(map(int, input().split(" ")))
N = int(input())

for _ in range(N):
    operation, _ = input().split(" ")
    B = set(map(int, input().split(" ")))
    exec(f"A.{operation}({B})")

print(sum(A))