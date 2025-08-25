import numpy as np
import my_logger
import logging

logger = my_logger.MyLogger(name="MyAppLogger", level=logging.INFO, filename="app.log")


def run():
    # Исходные данные: x с непостоянным шагом и соответствующие y
    x_original = np.array([0.0, 1.5, 2.2, 3.8, 5.0])
    y_original = np.array([0.0, 1.0, 0.5, 1.5, 1.0])

    logger.info(f"x_original: {x_original}")
    logger.info(f"y_original: {y_original}")

    # Новая сетка по x с постоянным шагом
    x_uniform = np.linspace(x_original[0], x_original[-1], 50)
    logger.info(f"x_uniform: {x_uniform}")

    # Интерполяция
    y_interpolated = np.interp(x_uniform, x_original, y_original)
    logger.info(f"y_interpolated: {y_interpolated}")



if __name__ == '__main__':
    run()
