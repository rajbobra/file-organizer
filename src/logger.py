import logging, os, datetime

def setup_logger(log_dir):

    # TODO: Add Error Handling and put in another function
    log_dir_expanded = os.path.expanduser(log_dir)
    log_file = f'{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
    log_file_path = os.path.join(log_dir_expanded, log_file)
    with open(log_file_path, 'x') as file:
        pass

    logger = logging.getLogger('FileOrganizer')
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    return logger