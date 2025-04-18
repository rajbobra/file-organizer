# 🗂️ File Organizer CLI Tool

A lightweight Python command-line tool to organize messy folders by automatically sorting files into directories based on customizable JSON rules.

---

## 🚀 Getting Started

### 🔧 Prerequisites
- Python 3 installed on your system

### 📦 Installation
```bash
git clone https://github.com/rajbobra/file-organizer.git
cd file-organizer-cli-tool/src
```

### Usage
```bash
python3 organize.py --path={directory_path} --configuration={config_path}
```
- --path: Path to the folder you want to organize
- --configuration: Path to your JSON config file with extension-to-folder rules. Refer to the sample rules.json in the repo for the format

- You can also run it using an absolute path:
  ```bash
  python3 /your/full/path/to/src/organize.py --path={directory_path} --configuration={config_path}
  ```

### 🔍 Dry Run Mode
- Preview file movements without changing anything on disk:
  ```bash
  python3 organize.py --path={directory_path} --configuration={config_path} --dry-run
  ```
- Outputs the simulated operations to the console instead of writing to a log file
- Helps avoid unintended changes


### 📄 Logs
- Each run generates a timestamped .log file containing detailed operations and errors
- Log files are moved to the "Other" directory if no rule is defined for .log extensions

---
### Still under development and more Enhancements coming up
- 🔄 Recursive folder organization
- 💾 Backup before move
- 🐛 Bug Fixes


Contact me at rajbobra.py@gmail.com for any ideas or queries.
