"""
Reinforcement learning for sevice function chaining
Action = {'viaCache','viaMPTCP','viaServer'}
Reward = w1*QoS <throughput-bitrate ratio> + w2*OffloadedTraffic <packetsize_>
State = {'latency_cache','latency_MPTCP','CWND_cache','CWND_MPTCP','jitter_cache','jitter_MPTCP','packetloss_cache','packetloss_MPTCP'}

This script is the main part which controls the update method of the MDP.
The RL is in Qlearning.py.
"""

from DatasetGen import Dataset
from QLearning import QLearningTable


def run_data():
    # step = 0
    for episode in range(len(Dataset)):
        observation = 0

        while True:
            # RL choose action based on state description
            action = RL.choose_action(str(observation))

            # RL take action and get next observation and reward
            observation_, reward, done = env.step(action)

            # RL.store_transition(observation, action,reward, observation_)
            RL.learn(str(observation), action, reward, str(observation_))

            # RL replace target parameter
            # if (step > 200) and (step % 5 == 0):
            #     RL.learn()

            # swap observation
            observation = observation_

            # break while loop when end of this episode
            if done:
                break
            # step += 1

            # end of learning
            print ('finish entire episodes')

if __name__=="__main__":

    # QNetwork for offloading on mobile infrastructure
    env = Dataset()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    # run MDP process
    run_data()
    # env.after(100, run_data)
    # env.mainloop()
