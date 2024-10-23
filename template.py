import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format ='[%(asctime)s]: %(message)s :')


list_of_files =[
    "src/__init__.py","src/helper.py","src/prompt.py",
    ".env","requirements.txt","setup.py",
    "research/trials.ipynb",
    "app.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    logging.info(filepath)
    filedir,filename = os.path.split(filepath)
    # logging.info(filedir,filename)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0 ):
        with open(filepath, "w") as f:
            pass

    else:
        logging.info(f"{filename} is already exists")