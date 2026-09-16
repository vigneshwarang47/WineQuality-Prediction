import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(messgage)s:')
project_name = "Datascience"

list_of_files  = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py", ##Components contain the actual ML/data-processing building blocks.
    f"src/{project_name}/utils/__init__.py", ##Utilities are reusable helper functions.
    f"src/{project_name}/utils/common.py", #This is where you keep generic helper functions that can be reused throughout your project.
    f"src/{project_name}/config/common.py",
    f"src/{project_name}/config/configuration.py",#This is responsible for reading configuration files and creating configuration objects.
    f"src/{project_name}/pipeline/__init__.py",#This package contains your pipeline execution logic.
    f"src/{project_name}/entity/__init__.py", #The entity package contains configuration/data classes.
    f"src/{project_name}/entity/config_entity.py",#It defines structured configuration objects.
    f"src/{project_name}/constants/__init__.py", #Constants are values that should remain consistent throughout the project.
    "config/config.yaml",#YAML is useful because it separates configuration from Python code.
    "params.yaml",#Usually contains ML parameters.
    "schema.yaml",#This describes your data schema.
    "main.py",#This is normally the main entry point of your application/pipeline.
    "Dockerfile",#This creates a Docker image containing your application.
    "setup.py", #This tells Python how your project should be packaged/installed.
    "research/research.ipynb",#This is your experimentation notebook.
    "templates/index.html",#This is related to your web application.,
    "app.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename = os.path.split(filepath)
    
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file: {filename}")
    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info({f"{filename} is already exists"})