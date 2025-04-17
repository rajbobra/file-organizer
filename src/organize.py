from configuration import *
from file_organizer import *
from logger import *
import os
from args import *

def main():
    cli_args = parse_args()
    config = Configuration(cli_args.config)
    logger = setup_logger(cli_args.path)
    file_org = FileOrganizer(cli_args.path, config, logger, cli_args.dry_run)
    file_org.organize()
    print("Files have been organized!")


if __name__ == '__main__':
    main()