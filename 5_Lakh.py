import gym_super_mario_bros
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from matplotlib import pyplot as plt
from gym.wrappers import FrameStack
from stable_baselines3.common.vec_env import VecFrameStack, DummyVecEnv
from gym.wrappers import GrayScaleObservation

env = gym_super_mario_bros.make('SuperMarioBros-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
env = GrayScaleObservation(env, keep_dim=True)
env = DummyVecEnv([lambda: env])
env = VecFrameStack(env, 4, channels_order='last')
state=env.reset()
state, reward, done, info = env.step([5])

import os 
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback

# class TrainAndLoggingCallback(BaseCallback):

#     def __init__(self, check_freq, save_path, verbose=1):
#         super(TrainAndLoggingCallback, self).__init__(verbose)
#         self.check_freq = check_freq
#         self.save_path = save_path

#     def _init_callback(self):
#         if self.save_path is not None:
#             os.makedirs(self.save_path, exist_ok=True)

#     def _on_step(self):
#         if self.n_calls % self.check_freq == 0:
#             model_path = os.path.join(self.save_path, 'best_model_{}'.format(self.n_calls))
#             self.model.save(model_path)

#         return True
    
# CHECKPOINT_DIR = './train/'
# LOG_DIR = './logs/'

# callback = TrainAndLoggingCallback(check_freq=10000, save_path=CHECKPOINT_DIR)
# model = PPO('CnnPolicy', env, verbose=1, tensorboard_log=LOG_DIR, learning_rate=0.000001, 
#             n_steps=512) 
# #model.learn(total_timesteps=1000000, callback=callback)
# #model.save('5lakhmodel')

model = PPO.load('./train/best_model_500000')
state = env.reset()
state = env.reset()
while True: 
    action, _ = model.predict(state)
    state, reward, done, info = env.step(action)
    env.render()



