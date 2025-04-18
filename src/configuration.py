import json

class Configuration:

    def __init__(self, config_file):
        self.config_file = config_file
        self.rules = {}
        self.ignore_files = []
        self.load_config()

    def load_config(self):
        # parse the config json and loads the config in config map
        with open(self.config_file, 'r') as file:
            config = json.load(file)

        self.rules = config['rules']
        self.unpack_rules()
        self.ignore_files = config['ignore_files']

    
    def unpack_rules(self):
        unpacked_rules = {}
        for exts, dir in self.rules.items():
            extensions = [ext.strip() for ext in exts.split(",")]
            for ext in extensions:
                unpacked_rules[ext] = dir

        self.rules = unpacked_rules