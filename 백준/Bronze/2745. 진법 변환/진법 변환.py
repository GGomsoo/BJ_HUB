# 진법 변환
# 브론즈 II
# 백준 허브 test

N, B = input().split()
numbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0
N_reverse = ''

for i in range(len(N)-1,-1,-1):
    N_reverse += N[i]

for i in range(len(N)):
    for j in range(len(numbers)):
        # 입력문자[i] 값이랑 numbers[j]랑 같으면?
        if N_reverse[i] == numbers[j]:
            # 진법변환 시작
            ans += j * (int(B) ** i)

print(ans)