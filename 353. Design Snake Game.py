from collections import deque


class SnakeGame(object):
    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.m = height
        self.n = width
        self.food = food
        self.gameover = False
        self.positions = deque([(0, 0)])
        self.result = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        if self.gameover:
            return -1

        x, y = self.positions[0]
        if direction == 'U':
            x -= 1
        elif direction == 'L':
            y -= 1
        elif direction == 'R':
            y += 1
        else:
            x += 1

        if x < 0 or x >= self.m or y < 0 or y >= self.n or ((x, y) in self.positions and (x, y) != self.positions[-1]): # 特殊情况，当新的头是当前的尾巴是可以的
            self.gameover = True
            return -1

        if len(self.food) > 0 and x == self.food[0][0] and y == self.food[0][1]: # 尾部就是新的头部
            self.result += 1
            self.positions.appendleft((x, y))
            self.food.pop(0)
        else:
            self.positions.appendleft((x, y))
            self.positions.pop()
        return self.result


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)