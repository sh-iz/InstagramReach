# with open("captions.py",'r',encoding="utf-8") as r:
#     lines = r.readlines()
#     with open('usedCaptions.py','w',encoding="utf-8") as w:
#         w.write("captions = [");
#         for l in lines:
#             t= "\""+l+"\","
#             w.write(t)
import os, random,calendar
from instabot import Bot
from hashtags import hts
from creds import id,pw
from captions import caps,usedCaps
from datetime import date


# Choose a random image from the images directory
def chooseImage():
    return random.choice(os.listdir("K:\\Projects\\Auto Download Unsplash\\Images\\Motivational")) 

# moving the used picture from the images directory to a new directory
def moveUsedImg(sourcePath,img):
    try:
        targetPath = "K:\\Projects\\Auto Download Unsplash\\Used\\Motivational\\"+img
        os.rename(sourcePath,targetPath)
        return "Successfully moved ther image to Used directory!"
    except:
        return (f"Oops! Couldn't move the file to used directory. \n Please move {img} manually")

def main():
    imageName = chooseImage()  #chooses a random image from directory
    imgPath = "K:\\Projects\\Auto Download Unsplash\\Images\\Motivational\\" + imageName

    status = moveUsedImg(imgPath,imageName)
    print(status)

if __name__=="__main__":
    main()
