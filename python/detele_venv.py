import os
import shutil

def delete_venv_folders(directory):
    for root, dirs, files in os.walk(directory):
        if 'venv' in dirs:
            venv_path = os.path.join(root, 'venv')
            print(f"Deleting: {venv_path}")
            shutil.rmtree(venv_path)

# Set your project directory here
project_directory = '/path/to/your/project'
delete_venv_folders(project_directory)
