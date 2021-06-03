import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


REGRESSION = LinearRegression()


def linear_reg_anim(x_values, y_values, time):
    """
    Creates animated linear regression with randomly
    created dataset.

    Params:
        x_values -> list:
            Empty list where we add random items to x-plane.
        y_values -> list:
            Empty list where we add random items to y-plane.

        Return:
            Show animated linear regression with randomly created dataset.
    """
    for item in range(1000):
        plt.clf()
        x_values.append(random.randint(0, 100))
        y_values.append(random.randint(0, 100))

        x = np.array(x_values)
        x = x.reshape(-1, 1)

        y = np.array(y_values)
        y = y.reshape(-1, 1) 

        if item % 5 == 0:
            REGRESSION.fit(x, y)
            plt.xlim(0, 100)
            plt.ylim(0, 100)
            plt.scatter(x_values, y_values, color='black')
            plt.plot(list(range(100)), REGRESSION.predict(np.array([x for x in range(100)]).reshape(-1, 1)))
            plt.pause(time)

    return plt.show()


if __name__ == '__main__':
    speed = {
        'fast': 0.0000000001,
        'normal': 0.0001,
        'slow': 0.1,
    }

    speed_input = str(input('Please, choose speed of the animation:\n'
                            'fast | normal | slow\n'))

    x_data = []
    y_data = []
    linear_reg_anim(x_data, y_data, speed[speed_input])
