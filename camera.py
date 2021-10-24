import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    vd = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = vd.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name , frame)
        start_time = time.time
        result = False

    return img_name
    print("snapshot taken")
    vd.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "wWNG17yULusAAAAAAAAAAY8gQsXm3E2JazwrgFBvCN0DqjZugR2tvlz_D134H0ck"
    file = img_name
    file_from = file
    file_to = "/testfolder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")
    
def main():
    while(True):
        if((time.time() - start_time)>= 5):
            name = take_snapshot()
            upload_file(name)
main()

