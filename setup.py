import os
import venv

# Fungsi untuk membuat virtual environment
def create_virtualenv(env_name='.venv'):
    venv_dir = os.path.join(os.getcwd(), env_name)
    venv.create(venv_dir, with_pip=True)
    print(f'Virtual environment created at: {venv_dir}')

# Fungsi untuk membuat struktur folder
def create_structure():
    folders = ['models', 'controllers', 'routes']
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f'Created folder: {folder}')
        
def create_project_structure():
    folders = ["models", "controllers", "routes"]
    for folder_item in folders:
        os.makedirs(folder_item, exist_ok=True)

    # Create necessary files
    open("app.py", "w").close()
    open("config.py", "w").close()
    open("requirements.txt", "w").close()

    print("Struktur proyek berhasil dibuat.")
    print("Folder yang dibuat: ", ", ".join(folders))
    print("File yang dibuat: app.py, config.py, requirements.txt\n")


if __name__ == '__main__':
    create_virtualenv()
    create_project_structure()
