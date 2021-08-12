for _ in range(int(input())):               # read number of test cases
    n = int(input())                        # read input
    arr = list(map(int, input().split()))   # read array abd staore in list
    count =0                                # initialize cequals to 0
    for i in arr:                           # for every element in array checking the condition
        if i >= 2 or i <= -2:
            count += 1                      # increment count with 1 
    if count > 2:                           # if greater than 2, print no
        print("no")
    else:                                   # else list it and store true in ans
        s = list(set(arr))                  
        ans = True
        for i in range(len(s)):             # for every element in range between o and length of array
            for j in range(i+1,len(s)):
                if s[i]*s[j] not in s:      # if product of s[i] and s[j] not in s 
                    ans = False
        if ans:                             # if it satisfies print yes, then store false in ans
            print("yes")
        else:                               #else No
            print("no")