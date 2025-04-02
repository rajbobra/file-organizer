from collections import defaultdict
import os
import shutil

class FileOrganizer:

    def __init__(self, path, rules, logger):
        self.path = os.path.expanduser(path)
        self.rules = rules
        self.logger = logger

    
    def get_files(self):
        file_map = defaultdict(list)
        for dirpath,_,files in os.walk(self.path):
            for file in files:
                ext = os.path.splitext(file)[1]
                file_map[ext].append(os.path.join(dirpath, file))
            break # only scan current level
        
        return file_map
    

    def ensure_directory(self, target_dir_name):
        target_dir = os.path.join(self.path, target_dir_name)
        if not os.path.exists(target_dir):
            try:
                os.mkdir(target_dir)
                self.logger.info(f'Created Directory: "{target_dir}" as it did not exist')
            except PermissionError:
                self.logger.info(f'Permission Denied: Failed to create "{target_dir}"')
                raise
            except Exception as e:
                self.logger.info(f'Failed to create "{target_dir}": {e}')
                raise
        return target_dir


    def organize(self):
        file_map = self.get_files()
        for ext in file_map:
            target_dir = self.ensure_directory(self.rules[ext]) if ext in self.rules else self.ensure_directory('Other')
            for file in file_map[ext]:
                try:
                    shutil.move(file, target_dir)
                    self.logger.info(f'Moved: {file} --> {target_dir}')
                except Exception as e:
                    self.logger.error(f'Failed to move {file} to {target_dir}: {e}')