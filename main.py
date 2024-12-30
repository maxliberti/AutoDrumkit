import os
import shutil
import zipfile
import ctypes, sys
import logging

# logging config
logging.basicConfig(filename='organize_kits.log', filemode='w', level=logging.DEBUG, format='%(asctime)s ; %(levelname)s ; %(message)s')

# paths
download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# checks if user is admin
def is_user_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def print_files_in_folder(ext, path): # debug function
  for root, dirs, files in os.walk(path):
    for name in files:
      if name.endswith(ext):
        print(name)  # printing file name

def organize_kits(path):
    logging.debug("Started organizing kits")
    for filename in os.listdir(path):
        src = path + "/" + filename # Original zip file path

        if "kit" in filename.lower() and filename.endswith(".zip"):
            # paths
            folder_name = os.path.splitext(filename)[0] # folder name without .zip at the end
            folder_for_kits = "C:\\Program Files\\Image-Line\\FL Studio 2024\\Data\\Patches\\Packs"
            new_folder_path = os.path.join(folder_for_kits, folder_name) # path that will contain the kit
            zip_destination = os.path.join(new_folder_path, filename) # path where the zip file is moved

            # make directory
            os.makedirs(new_folder_path, exist_ok=True)
            logging.debug(f"Created directory: {new_folder_path}")

            # move the file
            shutil.move(src, new_folder_path)
            logging.debug(f"Moved zip to: {new_folder_path}")

            # unzip
            with zipfile.ZipFile(zip_destination, "r") as zip_ref:
                zip_ref.extractall(new_folder_path)

            # delete original zip file
            os.remove(zip_destination)
            logging.debug(f"Extracted and deleted zip: {zip_destination}")

    logging.debug("Finished organizing kits")

def main():
    if not is_user_admin():
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        return
    logging.debug("Starting the script with admin rights")
    organize_kits(download_path)


if __name__ == '__main__':
  main()