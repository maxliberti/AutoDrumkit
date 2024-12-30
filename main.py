import os
import shutil
import zipfile
import ctypes, sys
import logging
from pyuac import main_requires_admin


class Utils():
    def __init__(self):
        # logging config
        logging.basicConfig(filename='organize_kits.log', filemode='w', level=logging.DEBUG, format='%(asctime)s ; %(levelname)s ; %(message)s')
        # paths
        self.download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    def print_files_in_folder(ext, path):  # debug function
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith(ext):
                    print(name)  # printing file name

class AutoDrumkit():
    def __init__(self):
        pass

    def organize_kits(self, path):
        logging.debug("Started organizing kits")
        for filename in os.listdir(path):
            src = path + "/" + filename # Original zip file path

            if "kit" in filename.lower() and filename.endswith(".zip"):
                try:
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
                    print("Will even this print?")

                    # unzip
                    with zipfile.ZipFile(zip_destination, "r") as zip_ref:
                        zip_ref.extractall(new_folder_path)

                    # delete original zip file
                    os.remove(zip_destination)
                    logging.debug(f"Extracted and deleted zip: {zip_destination}")
                except Exception as e:
                    logging.error(f"Error organizing kit {filename}: {e}")

        logging.debug("Finished organizing kits")
        print("Will this print?")

    @main_requires_admin
    def main(self):
        utils = Utils()
        logging.debug("Starting the script with admin rights")
        print("This prints")
        self.organize_kits(utils.download_path)


if __name__ == '__main__':
    auto_drumkit = AutoDrumkit()
    auto_drumkit.main()