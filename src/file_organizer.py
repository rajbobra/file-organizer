from collections import defaultdict
import os
import shutil

class FileOrganizer:

    def __init__(self, path, config, logger, dry_run=False):
        self.path = os.path.expanduser(path)
        self.config = config
        self.logger = logger
        self.dry_run = dry_run
    

    def get_files(self):
        file_map = defaultdict(list)
        for dirpath,_,files in os.walk(self.path):
            for file in files:
                if file in self.config.ignore_files:
                    continue
                ext = os.path.splitext(file)[1]
                print(f"Appended {file} to file map")
                file_map[ext].append(os.path.join(dirpath, file))
            break # only scan current level
        
        return file_map
    

    def ensure_directory(self, target_dir_name):
        target_dir = os.path.join(self.path, target_dir_name)
        if not os.path.exists(target_dir):
            try:
                if not self.dry_run:
                    os.mkdir(target_dir)
                    self.logger.info(f'Created Directory: "{target_dir}" as it did not exist')
            except PermissionError:
                self.logger.info(f'Permission Denied: Failed to create "{target_dir}"')
                raise
            except Exception as e:
                self.logger.info(f'Failed to create "{target_dir}": {e}')
                raise
        return target_dir


    def move_file(self, file, target_dir):
        if self.dry_run:
            self.logger.info(f"[DRY RUN] Would move: {file} --> {target_dir}")
        else:
            shutil.move(file, target_dir)
            self.logger.info(f"Moved: {file} --> {target_dir}")


    def organize(self):
        file_map = self.get_files()
        if len(file_map) <= 1:
            self.logger.warning(f"No files found in '{self.path}' to organize.")
        print(f'File map: {file_map}')
        for ext in file_map:
            target_dir = self.ensure_directory(self.config.rules[ext]) if ext in self.config.rules else self.ensure_directory('Other')
            for file in file_map[ext]:
                try:
                    if not os.access(file, os.W_OK):
                        self.logger.error(f"Skipping: {file}. (no write permissions)")
                        continue
                    self.move_file(file, target_dir)
                except FileNotFoundError:
                    self.logger.error(f"File not found: {file}. It may have been deleted")
                except PermissionError:
                    self.logger.error(f"Permission denied: Cannot move '{file}'")
                except Exception as e:
                    self.logger.error(f'Failed to move {file} to {target_dir}: {e}')