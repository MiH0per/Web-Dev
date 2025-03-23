#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0]>arr[1]:
        max = arr[0]
        sec_max = arr[1]
    else: 
        max = arr[1]
        sec_max = arr[0]

    for i in range(2, len(arr)):
        if arr[i]>max:
            sec_max = max
            max = arr[i]
    print(sec_max)

