#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 09:52:03 2026
@author: subhankarmittra

path.exists()
path.mkdir()
path.parent
path.name
path.suffix
path.read_text()
path.write_text()

Path.home()
Path.cwd()

"""

"""
trading_beta/
    data/
    reports/
    config/
    logs/

"""

from pathlib import Path

base_dir = Path("trading_beta")

data_dir = base_dir / "data"
reports_dir = base_dir / "reports"
config_dir = base_dir / "config"
logs_dir = base_dir / "logs"

folders = [data_dir, reports_dir, config_dir, logs_dir]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)
    print(folder, "exists:", folder.exists())

print("Current working directory:", Path.cwd())
print("Base directory:", base_dir.resolve())
    
    
    
"""
now learn

path.write_text()
path.read_text()
path.name
path.parent
path.suffix
path.stem

"""    

summary_file = reports_dir / 'summary.txt'

summary_file.write_text("begining of trading project")
    
print("file created: ", summary_file.exists())
print("file path: ", summary_file.resolve())

content = summary_file.read_text()

print('file content is: ', content)

settings_file = config_dir / 'settings.txt'

settings_file.write_text("symbol=NIFTY\n"
                         "timeframe=5min\n"
                         "timezone=Asia/Kolkata\n"
                         )
                         

print('File name: ', settings_file.name)
print('Parent folder: ', settings_file.parent)
print('Extension: ', settings_file.suffix)
print('File stem: ', settings_file.stem)                        
    
    
log_file = logs_dir / 'activity.log'

with log_file.open("a") as file:
    file.write("Folder structure created.\n")
    file.write("Settings file created.\n")
    file.write("Pathlib practice completed.\n")
    
content_after_appending = log_file.read_text()

print('contents of appended file is ')
print(content_after_appending)    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

