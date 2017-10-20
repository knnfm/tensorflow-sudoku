from __future__ import division

import argparse
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from catch_ball import CatchBall
from dqn_agent import DQNAgent


def init():
    img.set_array(state_t_1)
    plt.axis("off")
    return img

def print_result(env, ai_hand, challenger_hand, reward):
    log = []
    log.append("AI:")
    log.append(env.get_hand_name(ai_hand))
    log.append(" ")
    log.append("Challenger:")
    log.append(env.get_hand_name(challenger_hand))

    if reward == 0:
        print "AI EVEN " + "".join(log)
    elif reward == 1:
        print "AI WIN " + "".join(log)
    else:
        print "AI LOSE " + "".join(log)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model_path")
    args = parser.parse_args()

    env = CatchBall()
    agent = DQNAgent(env.enable_actions, env.name)
    agent.load_model(args.model_path)

    env.reset()
    env.set_question()
    state_t_1, reward_t, terminal = env.observe()
    action_t = agent.select_action(state_t_1, 0.0)
    print state_t_1
    print action_t
