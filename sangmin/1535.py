'''
세준이는 성형수술을 한 후에 병원에 너무 오래 입원해 있었다. 이제 세준이가 병원에 입원한 동안 자기를 생각해준 사람들에게 감사하다고 말할 차례이다.

세준이를 생각해준 사람은 총 N명이 있다. 사람의 번호는 1번부터 N번까지 있다. 세준이가 i번 사람에게 인사를 하면 L[i]만큼의 체력을 잃고, J[i]만큼의 기쁨을 얻는다. 세준이는 각각의 사람에게 최대 1번만 말할 수 있다.

세준이의 목표는 주어진 체력내에서 최대한의 기쁨을 느끼는 것이다. 세준이의 체력은 100이고, 기쁨은 0이다. 만약 세준이의 체력이 0이나 음수가 되면, 죽어서 아무런 기쁨을 못 느낀 것이 된다. 세준이가 얻을 수 있는 최대 기쁨을 출력하는 프로그램을 작성하시오.
6:05 ->
1 번 접근: 배낭문제?
2 -> 백트렉킹?
'''

N = int(input())
health = list(map(int,input().split())) 
joy = list(map(int,input().split()))
value = []
for i in range(N):
    value.append([health[i],joy[i]])

value.sort()
dp = [[0]*(100) for i in range(N+1)] #물건을 한개 넣었을 때 부터 N 개를 넣었을 때까지
for i in range(value[0][0],100):
    dp[0][i] = value[0][1]
# print(dp)

for i in range(1,N):
    for j in range(1,100):
        if value[i][0] <= j:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-value[i][0]] + value[i][1])
        else:
            dp[i][j] = dp[i-1][j]

result = [dp[i][-1] for i in range(N)]
print(max(result))
# print(dp)
