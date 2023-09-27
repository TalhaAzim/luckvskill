import matplotlib.pyplot as plt


class SingleSimulation(object):

    def __init__(self, agent, luck_fn):

        self.agent = agent
        self.capital_over_time = [agent.capital]
        self.luck_fn = luck_fn

    def run(self, num_ticks):

        for tick in range(num_ticks):
            self.agent.tick(tick, self.luck_fn(tick))
            self.capital_over_time.append(self.agent.capital)
        return self

    def plot(self):

        plt.plot(self.capital_over_time)
        plt.xlabel('Tick')
        plt.ylabel('Capital')
        plt.title('Agent Simulation with Skill and Luck')
        plt.show()
