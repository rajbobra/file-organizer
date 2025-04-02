
import os
import shutil

class FileOrganizer:

    def __init__(self, path, rules):
        self.path = os.path.expanduser(path)
        self.rules = rules

    
    def get_files(self):
        file_map = {}
        for dirpath,_,files in os.walk(self.path):
            for file in files:
                ext = os.path.splitext(file)[1]
                full_path = os.path.join(dirpath, file)
                if ext in file_map:
                    file_map[ext].append(full_path)
                else:
                    file_map[ext] = [full_path]
            break # only scan current level
        
        return file_map

    def organize(self):
        file_map = self.get_files()
        # go through the file map
            # if key (ext) exists in rule map
                # create rule dir if it does not exist
                # move all files to this dir
            # else create 'Other' dir if does not exist
                # add the files to Other
        for ext in file_map:
            if ext in self.rules:
                # create rule dir if it does not exist
                dir = f'{self.path}/{self.rules[ext]}'
                if not os.path.exists(dir):
                    os.mkdir(dir)
                for file in file_map[ext]:
                    shutil.move(file, dir)
                # move all files to this dir
            else:
                dir = f'{self.path}/Other'
                if not os.path.exists(dir):
                    os.mkdir(dir)
                for file in file_map[ext]:
                    shutil.move(file, dir)

