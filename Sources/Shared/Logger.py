import logging


class Logger:
    observers = {}

    @classmethod
    def Logger(cls, module_name):
        if cls.observers.get(module_name) is not None:
            return cls.observers[module_name]

        # create logger
        logger = logging.getLogger(module_name)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter('%(asctime)s %(levelname)s\t %(name)s(%(filename)s:%(lineno)d)\t- %(message)s', '%H:%M:%S')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(ch)

        cls.observers[module_name] = logger
        return logger
