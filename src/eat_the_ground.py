'''
"땅따먹기"

문제 설명
땅따먹기 게임을 하려고 합니다. 땅따먹기 게임의 땅(land)은 총 N행 4열로 이루어져 있고, 모든 칸에는 점수가 쓰여 있습니다. 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야 합니다. 단, 땅따먹기 게임에는 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없는 특수 규칙이 있습니다.

예를 들면,

| 1 | 2 | 3 | 5 |

| 5 | 6 | 7 | 8 |

| 4 | 3 | 2 | 1 |

로 땅이 주어졌다면, 1행에서 네번째 칸 (5)를 밟았으면, 2행의 네번째 칸 (8)은 밟을 수 없습니다.

마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return하는 solution 함수를 완성해 주세요. 위 예의 경우, 1행의 네번째 칸 (5), 2행의 세번째 칸 (7), 3행의 첫번째 칸 (4) 땅을 밟아 16점이 최고점이 되므로 16을 return 하면 됩니다.

제한사항
행의 개수 N : 100,000 이하의 자연수
열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
점수 : 100 이하의 자연수
입출력 예
land	answer
[[1,2,3,5],[5,6,7,8],[4,3,2,1]]	16

'''

def solution(land):
    answer = 0
    N = len(land)
    for i in range(0,N-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])
        # i+1번째 행에 0번째 열에는 i번째 행에 1,2,3 열 중 최대값을 더해준다. 이런식으로 계속 더해나가면
        # N-1번째에 열들을 각 선택지에서 가질 수 있는 최대값이 된다.
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])
        # 바로 위에 코드가 똑같은 코드다. N-1행에서의 최대값을 가지는 열 answer에 대입한다.
        answer = max(land[N-1])
        print (answer)
    
    # answer = max(land[N-1][0],land[N-1][1],land[N-1][2],land[N-1][3]) 
    return answer