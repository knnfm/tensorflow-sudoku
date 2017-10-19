#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

from catch_ball import CatchBall
from dqn_agent import DQNAgent


if __name__ == "__main__":
    n_epochs = 100
    env = CatchBall()
    agent = DQNAgent(env.enable_actions, env.name)
    win = 0

    for e in range(n_epochs):
        frame = 0
        loss = 0.0
        Q_max = 0.0
        env.reset()
        env.set_question()
        state_t_1, reward_t, terminal = env.observe()

        # 全部数字が埋まるまでループ
        while not terminal:
            state_t = state_t_1
            action_t = agent.select_action(state_t, agent.exploration)
            env.execute_action(action_t)

            state_t_1, reward_t, terminal = env.observe()

            agent.store_experience(state_t, action_t, reward_t, state_t_1, terminal)
            agent.experience_replay()

            # for log
            frame += 1
            loss += agent.current_loss
            Q_max += np.max(agent.Q_values(state_t))
            if reward_t == 1:
                win += 1


        # print("EPOCH: {:03d}/{:03d} | WIN: {:03d} | LOSS: {:.4f} | Q_MAX: {:.4f}".format(e, n_epochs - 1, win, loss / frame, Q_max / frame))
        print("{:03d}\t{:.4f}\t{:.4f}\t{:.4f}".format(e, float(win)/(e+1), loss / frame, Q_max / frame))

    # save model
    agent.save_model()
