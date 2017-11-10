"""
Reinforcement learning SFC management example
Action = {'viaCache','viaMPTCP','viaServer'}
Reward = w1*QoS <throughput-bitrate ratio> + w2*OffloadedTraffic <packetsize_>
State = {'latency_cache','latency_MPTCP','jitter_cache','jitter_MPTCP',
           'packetloss_cache','packetloss_MPTCP'}

This script is the environment part of the MDP.
Build environment by using measured dataset of each actions during http video streaming.
"""


import numpy as np
import pandas as pd

# df = pd.read_fwf('output_list.txt')
# names = ["latency_C", "jitter_C", "packetloss_C", "retransmit_C", "throuput_C", "datasize_C"]
data_Cache = pd.read_csv('cacheData.csv', sep=",", header = None,
                names = ["latency_C", "jitter_C", "retransmit_C", "throuput_C", "datasize_C"])
data_MPTCP = pd.read_csv('MPTCPData.csv', sep=",", header = None,
                names = ["latency_M", "jitter_M", "retransmit_M", "throuput_M", "datasize_M"])
data_Server = pd.read_csv('LTEData.csv', sep=",", header = None,
                names = ["latency_S", "jitter_S", "retransmit_S", "throuput_S", "datasize_S"])

# convert each columns' data referring with specific range of unit
# dataC_Convert =
# dataM_Convert =
# dataS_Convert =

# group by same condition of dataset for make state and reward matrix
# ["latency_C", "jitter_C", "retransmit_C", "throuput_C",
#  "latency_M", "jitter_M", "retransmit_M", "throuput_M",
#  "latency_S", "jitter_S", "retransmit_S", "throuput_S"]

data_Agg =


# divide dataframe to States and Performance
data_State =
data_Perf =


# define step size
videBitrate = 1     # 1MBps
videoSize = 60      # 60MB (60sec)

bufferSize = 1
totalStep = videoSize/bufferSize

class Dataset:
    def __init__(self):
        self.action_space = ['c', 'm', 's']
        self.n_actions = len(self.action_space)
        self.states = data_State
        self.perf = data_Perf
        self.stepLength = totalStep

    # define builder for reward dataframe
    def builder_state(self):

    # define builder for reward dataframe
    def builder_reward(self):


    # define step and giving reward
    def step(self, actions):

        return s_, reward, done



def update():



# if __name__ == '__main__':
#     env = Dataset()
