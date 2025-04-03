from configuration import *
from file_organizer import *
from logger import *
import os

DIR = '~/Documents/file-rehab-test'
CONFIG = '../rules.json'

def main():
    config = Configuration(CONFIG)
    logger = setup_logger(DIR)
    file_org = FileOrganizer(DIR, config, logger)
    file_org.organize()
    print("Files have been organized!")

main()