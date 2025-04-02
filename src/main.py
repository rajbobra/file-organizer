from configuration import *
from file_organizer import *

def main():
    config = Configuration('../rules.json')
    rules = config.load_config()
    print(rules)
    file_org = FileOrganizer('~/Documents/file-rehab-test', rules)
    file_org.organize()
    print("Files have been organized!")

main()