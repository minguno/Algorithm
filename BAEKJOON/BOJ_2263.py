# 트리의 순회
'''
재귀식 접근 구현법

1. postorder의 마지막 숫자는 전체 루트 노드
2. inorder의 특성을 이용해서 루트 기준 왼쪽 섭트리 오른쪽 섭트리의 노드 수를 구할 수 있다
3. 왼쪽 노드수, 오른쪽 노드수를 이용하여 inorder를 왼쪽 inorder, 루트, 오른쪽 inorder로 분류
4. 동일하게 postorder를 왼쪽, 오른쪽, 루트로 분류
5. 왼쪽 postorder의 마지막 숫자는 왼쪽 섭트리의 루트 -> 반복 작업 (재귀)
'''

import sys
sys.setrecursionlimit(10**6)

# preorder
def idunno(instart, inend, poststart, postend):
    if (instart > inend) or (poststart > postend):
        return

    # postorder에서 부모노드 찾기
    parent = postlst[postend]
    print(parent, end=" ")

    # 왼쪽 섭트리 노드 개수
    left = idx[parent] - instart
    # 오른쪽 섭트리 노드 개수
    right = inend - idx[parent]

    # 왼쪽 노드
    idunno(instart, instart + left - 1, poststart, poststart + left - 1)
    # 오른쪽 노드
    idunno(inend - right + 1, inend, postend - right, postend - 1)


N = int(input())
inlst = list(map(int, input().split()))
postlst = list(map(int, input().split()))

idx = [0] * (N + 1)
for i in range(N):
    idx[inlst[i]] = i

idunno(0, N - 1, 0, N - 1)

