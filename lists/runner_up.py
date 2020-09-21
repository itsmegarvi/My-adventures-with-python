# QUESTION: You are given  scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lis = list(arr)
    z = max(lis)
    while max(lis) == z:
         lis.remove(max(lis))
print (max(lis))
