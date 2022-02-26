import os
import shutil
from api.HelperFunctions import _make_textfile, _make_zipfile

def create_cutTool(bookmarks) : 
    _make_textfile(bookmarks)
    os.system("python ./api/download_logic/setup.py build")
    _make_zipfile()

def delete_cutTool() : 
    shutil.rmtree(r"./build")
    os.remove('./HIGHLIGHTING.zip')