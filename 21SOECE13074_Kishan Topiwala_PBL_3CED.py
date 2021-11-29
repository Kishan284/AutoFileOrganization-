from tkinter import filedialog
from tkinter import *
import os
import shutil
root = Tk()
root.withdraw()
source = filedialog.askdirectory()

video = [".mp4", ".mkv"]
compress = [".7z", ".arj", ".deb ", ".pkg", ".rar", ".rpm ", ".tar", ".gz", ".z ", ".zip"]
image = [".png", ".svg", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff"]
document = [".pdf", ".xlsx", ".txt", ".ppt", ".pptx", ".docx", ".doc"]
exe = [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", ".wsf"]
program = [".c", ".C++", ".cgi ", ".pl", ".class", ".cpp", ".cs", ".h ", ".java", ".php", ".py", ".ipynb", ".sh",
           ".swift", ".vb"]

for file_name in os.listdir(source):
    data = os.path.splitext(file_name)
    only_name = data[0]
    extension = data[1]
    extension = extension.lower()
    so = source + "/"+file_name
    if os.path.isfile(so):
        if extension in image:
            ImageFolderPath = os.path.join(source, 'Image')
            if not os.path.exists(ImageFolderPath+"/"+str(extension).replace(".", "")):
                os.makedirs(ImageFolderPath+"/"+str(extension).replace(".", ""))
            FolderPath = ImageFolderPath+"/"+str(extension).replace(".", "")
            if os.path.exists(FolderPath + "/" + file_name):
                print(file_name + 'already exist')
                continue
            shutil.move(so, FolderPath)
            print('Moved:', file_name)
        elif extension in document:
            DocumentFolderPath = os.path.join(source, 'Document')
            if not os.path.exists(DocumentFolderPath+"/"+str(extension).replace(".", "")):
                os.makedirs(DocumentFolderPath+"/"+str(extension).replace(".", ""))
            FolderPath = DocumentFolderPath+"/"+str(extension).replace(".", "")

            if os.path.exists(FolderPath + "/" + file_name):
                print(file_name+'already exist')
                continue
            shutil.move(so, FolderPath)
            print('Moved:', file_name)
        elif extension in video:
            VideoFolderPath = os.path.join(source, 'Video')
            if not os.path.exists(VideoFolderPath + "/" + str(extension).replace(".", "")):
                os.makedirs(VideoFolderPath + "/" + str(extension).replace(".", ""))
            FolderPath = VideoFolderPath+"/"+str(extension).replace(".", "")
            if os.path.exists(FolderPath + "/" + file_name):
                print(file_name + 'already exist')
                continue
            shutil.move(so, FolderPath)
            print('Moved:', file_name)
        elif extension in compress:
            CompressFolderPath = os.path.join(source, 'Compress')
            if not os.path.exists(CompressFolderPath + "/" + str(extension).replace(".", "")):
                os.makedirs(CompressFolderPath + "/" + str(extension).replace(".", ""))
            FolderPath = CompressFolderPath+"/"+str(extension).replace(".", "")
            if os.path.exists(FolderPath + "/" + file_name):
                print(file_name + 'already exist')
                continue
            shutil.move(so, FolderPath)
            print('Moved:', file_name)
        elif extension in exe:
            ExeFolderPath = os.path.join(source, 'Executable_files')
            if not os.path.exists(ExeFolderPath + "/" + str(extension).replace(".", "")):
                os.makedirs(ExeFolderPath + "/" + str(extension).replace(".", ""))
            FolderPath = ExeFolderPath+"/"+str(extension).replace(".", "")
            if os.path.exists(FolderPath + "/" + file_name):
                print(file_name + 'already exist')
                continue
            shutil.move(so, FolderPath)
            print('Moved:', file_name)
        elif extension in program:
            ProgramFolderPath = os.path.join(source, 'Program')
            if not os.path.exists(ProgramFolderPath + "/" + str(extension).replace(".", "")):
                os.makedirs(ProgramFolderPath + "/" + str(extension).replace(".", ""))
            FolderPath = ProgramFolderPath+"/"+str(extension).replace(".", "")
            if os.path.exists(FolderPath + "/" + file_name):
                print(file_name + 'already exist')
                continue
            shutil.move(so, FolderPath)
            print('Moved:', file_name)
        else:
            print('file not moved')
