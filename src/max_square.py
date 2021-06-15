'''
"가장 큰 정사각형 찾기"

1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 
표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. 
(단, 정사각형이란 축에 평행한 정사각형을 말합니다.)


1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0

가 있다면 가장 큰 정사각형은

1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0

가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.

제한사항
표(board)는 2차원 배열로 주어집니다.
표(board)의 행(row)의 크기 : 1,000 이하의 자연수
표(board)의 열(column)의 크기 : 1,000 이하의 자연수
표(board)의 값은 1또는 0으로만 이루어져 있습니다.

'''


def solution(board):
    answer = 0

    for i in range(1,  len(board)):
        for j in range(1, len(board[0])):
            # 둘다 1일때
            if board[i][j] == 1:
                # 좌측상단, 위, 좌측 값 +1 = 3이되는곳이 가장 큰 정사각형의 위치
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
    
    for bo in board:
        maxvalue = max(bo)
        print (maxvalue)
        if maxvalue > answer:
            answer = maxvalue

    return answer**2