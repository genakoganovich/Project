import logging

class MyLogger:
    def __init__(self, name: str, level=logging.INFO, filename=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Не добавлять обработчики повторно (если уже добавлены)
        if not self.logger.handlers:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

            # Консольный обработчик
            # console_handler = logging.StreamHandler()
            # console_handler.setLevel(level)
            # console_handler.setFormatter(formatter)
            # self.logger.addHandler(console_handler)

            # Файловый обработчик (если указан файл)
            if filename:
                file_handler = logging.FileHandler(filename)
                file_handler.setLevel(level)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    def debug(self, msg): self.logger.debug(msg)
    def info(self, msg): self.logger.info(msg)
    def warning(self, msg): self.logger.warning(msg)
    def error(self, msg): self.logger.error(msg)
    def critical(self, msg): self.logger.critical(msg)
