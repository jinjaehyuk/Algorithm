import sys
input = sys.stdin.readline
from collections import deque


s = int(input())

visited = [[False]*(s+1) for _ in range(s+1)]

queue = deque()

queue.append((1,0,0)) #(화면, 클립보드, 횟수)

visited[1][0] = True
while queue:
    now, clip, cnt = queue.popleft()
    
    if now == s:
        print(cnt)
        break
    for i in range(3):
        if i == 0:
            #화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
            new_now, new_clip = now, now
        elif i == 1:
            #클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
            new_now, new_clip = now+clip, clip
        else:
            #화면에 있는 이모티콘 중 하나를 삭제
            new_now, new_clip = now-1, clip
        
        if new_now >= (s+1) or new_now < 0 or new_clip>=(s+1) or new_clip <0 or visited[new_now][new_clip]:
            continue
        
        visited[new_now][new_clip] = True
        queue.append((new_now,new_clip,cnt+1))
            
            