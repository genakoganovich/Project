import numpy as np
import re
import matplotlib.pyplot as plt

class LogPlotter:
    def __init__(self, log_filename='app.log'):
        self.log_filename = log_filename
        self.x_original = None
        self.y_original = None
        self.x_uniform = None
        self.y_interpolated = None

    def read_log(self):
        with open(self.log_filename, 'r') as f:
            lines = f.readlines()

        array_blocks = {
            'x_original': None,
            'y_original': None,
            'x_uniform': None,
            'y_interpolated': None
        }

        i = 0
        while i < len(lines):
            line = lines[i]
            for key in array_blocks.keys():
                if f"{key}:" in line:
                    array_lines = [line]
                    # Считываем до закрытия скобки
                    while ']' not in line:
                        i += 1
                        if i >= len(lines):
                            break
                        line = lines[i]
                        array_lines.append(line)
                    array_str = self._extract_array_block(array_lines)
                    array_blocks[key] = array_str
            i += 1

        # Преобразуем в numpy массивы
        self.x_original = np.fromstring(array_blocks['x_original'], sep=' ') if array_blocks['x_original'] else None
        self.y_original = np.fromstring(array_blocks['y_original'], sep=' ') if array_blocks['y_original'] else None
        self.x_uniform = np.fromstring(array_blocks['x_uniform'], sep=' ') if array_blocks['x_uniform'] else None
        self.y_interpolated = np.fromstring(array_blocks['y_interpolated'], sep=' ') if array_blocks['y_interpolated'] else None

        # Проверка
        missing = [k for k, v in array_blocks.items() if v is None]
        if missing:
            raise ValueError(f"Не найдены данные в логах: {', '.join(missing)}")

    def _extract_array_block(self, lines):
        """
        Объединяет несколько строк с массивом в одну строку чисел.
        Удаляет квадратные скобки и символы новой строки.
        """
        full = ' '.join(line.strip() for line in lines)
        match = re.search(r'\[([0-9eE\.\-\s]+)\]', full)
        return match.group(1) if match else None

    def plot(self):
        if any(arr is None for arr in [self.x_original, self.y_original, self.x_uniform, self.y_interpolated]):
            raise RuntimeError("Не все массивы считаны. Сначала вызовите read_log().")

        plt.plot(self.x_original, self.y_original, 'o', label='Оригинальные точки', markersize=10, color='red')
        plt.plot(self.x_uniform, self.y_interpolated, '-', label='Интерполяция (из лога)', color='blue')
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Визуализация из лога')
        plt.grid(True)
        plt.show()
