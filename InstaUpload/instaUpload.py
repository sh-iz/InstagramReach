import os, shutil, random,calendar
from instabot import Bot
from hashtags import hts
from creds import id,pw
from captions import caps,usedCaps
from datetime import date

bot = Bot()
trials = 0

def resetTrials(t):
    global trials
    if(t==0):
        trials = 0
    else:
        trials += 1


# Choose a random image from the images directory
def chooseImage():
    return random.choice(os.listdir("K:\\Projects\\Auto Download Unsplash\\Images\\Motivational")) 

# generating random hashtags
def generateHashtags():
    my_date = date.today()
    dayOfWeek = calendar.day_name[my_date.weekday()]
    hashtag = f"#{dayOfWeek.lower()}motivation "
    t=random.randint(0,len(hts)-21)
    for i in range( t,t+19 ):
        hashtag += hts[i] + " "
    return hashtag

# generate random motivational captions
def generateCaptions():
    try:
        index = random.randint(0,len(caps))
        caption = caps[index]
        usedCaps.append(caps[index])
        caps.pop(index)
    except:
        generateCaptions()
    return caption

# moving the used picture from the images directory to a new directory
def moveUsedImg(sourcePath,img):
    try:
        targetPath = "K:\\Projects\\Auto Download Unsplash\\Used\\Motivational\\" + img
        os.rename(sourcePath,targetPath)
        return "Successfully moved ther image to Used directory!"
    except:
        try:
            sourcePath +=".REMOVE_ME"
            targetPath = "K:\\Projects\\Auto Download Unsplash\\Used\\Motivational\\" + img
            os.rename(sourcePath,targetPath)
            return "Successfully moved ther image to Used directory!"
        except:
            return (f"Oops! Couldn't move the file to used directory. \n Please move {img} manually")
def generateImgPath(imageName):
    imgPath = "K:\\Projects\\Auto Download Unsplash\\Images\\Motivational\\" + imageName
    return imgPath

def post(cap):
    imageName = chooseImage()
    imgPath  = generateImgPath(imageName)
    try:
        bot.upload_photo(imgPath,caption=cap)
        # print("UPLOAD SUCCESS!")
        status = moveUsedImg(imgPath,imageName)
        print(status)
    except:
        # status = moveUsedImg(imgPath,imageName)
        # print(status + " because of a discrepancy")
        # print("Retrying uploading a different picture")
        # post(cap)
        pass


def login():
    try:
        bot.login(username = id, password = pw)
        resetTrials(0)
        return "Login Successful"
    except:
        resetTrials(1)
        if(trials<5):
            print("Login trials : "+ str(trials))
            login();
        else:
            return "Login Unsuccessful"

        
def main():
    status = login()
    print(status)
    resetTrials(0)
    for _ in range(8):
        caption = generateCaptions() + "\n\n" + generateHashtags() #generated relevant caption and adds hashtag to it
        
        if(status == "Login Successful"):
            post(caption)
        else:
            resetTrials(1)
            if(trials < 5):
                main()

    # Moving the image from source to used folder
    

if __name__=="__main__":
    main()
