import gym
import time
env = gym.make('Pong-v0')
env.reset()
for _ in range(1000):
    env.render()
    time.sleep(0.1)
    obs, rew, done, info = env.step(3) # take a random action
    
