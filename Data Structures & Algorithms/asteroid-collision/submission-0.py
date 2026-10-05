class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        while True:
            collision = False

            for i in range(len(asteroids)-1):
                if asteroids[i] > 0 and  asteroids[i+1] < 0:
                    if abs(asteroids[i]) < abs(asteroids[i+1]):
                        asteroids.pop(i)
                    elif abs(asteroids[i])> abs(asteroids[i+1]):
                        asteroids.pop(i+1)
                    else:
                        asteroids.pop(i+1)
                        asteroids.pop(i)
                    collision = True
                    break
            if not collision:
                break
        return asteroids        