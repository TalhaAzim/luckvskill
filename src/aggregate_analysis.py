import matplotlib.pyplot as plt
import seaborn as sns


class AggregateAnalysis(object):

    def __init__(self, agents, luck_fn):
        self.agents = agents
        self.luck_fn = luck_fn
        self.total_capital_over_time = []

    def run(self, num_ticks):
        total_capital = 0
        for tick in range(num_ticks):
            for agent in self.agents:
                agent.tick(tick, self.luck_fn(tick))
                total_capital = agent.capital
            self.total_capital_over_time.append(total_capital)
        return self

    def plot(self):
        final_capitals = [agent.capital for agent in self.agents]
        skill_levels = [agent.skill_fn.level for agent in self.agents]

        # Set Seaborn style
        sns.set(style="whitegrid")

        plt.subplot(2, 2, 1)  # First plot
        sns.histplot(final_capitals, bins=20, kde=True, edgecolor='black')
        plt.xlabel('Final Capital')
        plt.ylabel('Frequency')
        plt.title('Distribution of Final Capital Across Agents')

        plt.subplot(2, 2, 2)  # Second plot
        sns.scatterplot(x=skill_levels, y=final_capitals)
        plt.xlabel('Skill Level')
        plt.ylabel('Final Capital')
        plt.title('Skill Level vs Final Capital')

        plt.subplot(2, 2, 3)  # Third plot
        plt.plot(self.total_capital_over_time)
        plt.xlabel('Tick')
        plt.ylabel('Total Capital')
        plt.title('Total Capital in the System Over Time')

        plt.tight_layout()
        plt.show()
