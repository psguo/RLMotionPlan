from car_obstacle_env import CarObstacleEnv
import numpy as np

env = CarObstacleEnv(render=False, start_render=10000, test_interval=50)
env.run()