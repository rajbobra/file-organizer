from configuration import *
from file_organizer import *
from logger import *
import os

DIR = '~/Documents/file-rehab-test'
CONFIG = '../rules.json'

def main():
    config = Configuration(CONFIG)
    rules = config.load_config()
    logger = setup_logger(DIR)
    file_org = FileOrganizer(DIR, rules, logger)
    file_org.organize()
    print("Files have been organized!")

main()