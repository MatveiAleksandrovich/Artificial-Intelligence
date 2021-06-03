import random
import matplotlib.pyplot as plt


PAUSE_TIME = 0.0001


def bar_animation(values):
    """
    Creates bar data animation of random numbers


    Param:
        values -> list: amount of random numbers.

    Return:
        Show animated random stat data bars.
    """
    for item in range(50):
        values[item] = random.randint(0, 100)
        plt.xlim(0, 50)
        plt.ylim(0, 100)
        plt.bar(list(range(50)), values)
        plt.pause(PAUSE_TIME)
    return plt.show()


if __name__ == '__main__':
    amount_of_data = [0] * 50
    bar_animation(amount_of_data)
