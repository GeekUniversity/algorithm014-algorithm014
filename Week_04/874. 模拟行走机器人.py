class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        x = y = di = 0
        obstaclesSet = set(map(tuple, obstacles))
        ans = 0
        for command in commands:
            if command == -2:
                di = (di - 1)%4
            elif command == -1:
                di = (di + 1)%4
            else:
                while command:
                    if (x+dx[di],y+dy[di]) not in obstaclesSet:
                        x += dx[di]
                        y += dy[di]
                    command -= 1
                ans = max(ans, x*x + y*y)
        return ans