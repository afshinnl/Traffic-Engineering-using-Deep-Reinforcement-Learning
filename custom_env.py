import numpy as np

from gym import Env
from gym.spaces import Box, Discrete

import mininet_backend

NUMBER_LINKS = 90
NUMBER_PATHS = 20

class CustomEnv(Env):
    def __init__(self):
        self.done = False
        self.backend = mininet_backend.MininetBackend()
        
        """low = np.zeros(8 * NUMBER_LINKS + 7 + 4, dtype=np.float32)
        high = np.array([1.0] * 8 * NUMBER_LINKS + [1.0] * 7 + [1.0] * 4,
                        dtype=np.float32)
        #high = np.full((8*90 + 7 + 4), 1, dtype=np.float32)
        self.observation_space = Box(low=low, high=high,
                        dtype=np.float32)"""

        #low = 
        self.action_space = Discrete(NUMBER_PATHS)
        self.state = np.zeros(8 * NUMBER_LINKS + 7 + 4, dtype=np.float32)

        #request=0


    def reset(self):
        self.done = False
        self.state = np.zeros(8 * NUMBER_LINKS + 7 + 4, dtype=np.float32)

        #reset measurements
        #build initial state
        #number of requests=0 ???

        return self.state


    def render(self, mode='human'):
        pass


    def step(self, action):
        reward: float = 0.0
        #done: bool = False

        #request++ ???
        #take action
        #get state
        #calculate reward 
        #done = True or False

        return self.state, reward, done, {}
        

    


