import cv2   #importing openCV
from fpdf import FPDF   #importing FPDF fromfpdf
import os   #importing os module used for interacting with operating system
from PIL import Image
import numpy as np
url = "http://192.168.1.3:8080/video"   #write your url here
cap = cv2.VideoCapture(url)
ret = True
f1 = 0
i = 0
while ret:
    ret, frame=cap.read()
    #frame = cv2.resize(frame(1000,500))
    if f1==0:
        print("press 's' to scan the document")
        print("press 'q' to quit the document")
        f1=f1+1
    cv2.imshow("camera feed", frame)
    k= cv2.waitKey(1)  & 0xFF  #waits for input from the keyboard
    if k==ord('s') :
        cv2.destroyWindow("camera feed")
        cv2.imshow("Scanned photo",frame )
        print("press 'u' if unreadable")
        print("press 'b' to convert it into black and white form")
        print("press 'n' to remove the noises from the image")
        print("press 'e' to detect the edges of an image")
        print("press 'x' to crop the image")
        print("press 'c' to find the contours of the image")
        print("press 'r' to resize the image")

        #for scanning an unreadable document using adaptive thresholding

        k1=cv2.waitKey(0)
        if k1== ord('u') :
            cv2.destroyWindow('Scanned photo')
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            new=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,155,1)
            cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg"%i,new)
            i=i+1
            print("press 's' to scan more document")
            print("press 'q' to quit")
            continue

        #for producing the black an white copy of the image

        elif k1== ord('b') :
            cv2.destroyWindow('Scanned photo')
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg"%i,gray)
            i=i+1
            print("print 's' to scan more document")
            print("press 'q' to quit")
            continue

        # for adding gaussian blur to an image

        elif k1 == ord('n') :
            cv2.destroyWindow('Scanned Photo')
            a=int(input("Enter the size of the gaussian kernel"))
            if (a%2):
               denoised_img = cv2.GaussianBlur(frame, (a,a), 0, 0)
               cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg"%i, denoised_img)
               i = i + 1
               print("Press 's' to scan more documents")
               print("Press 'q' to quit ")
               continue

            else:
               print("Only odd values accepted")
               print("Press 's' to scan more documents")
               continue

        # for canny edge detection

        elif k1 == ord('e') :
                cv2.destroyWindow('Scanned photo')
                cannied = cv2.Canny(frame, 100, 200)
                cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg"%i,cannied)
                i = i + 1
                print("Press 's' to scan more documents")
                print("Press 'q' to quit")
                continue

        #for cropping the image

        elif k1 == ord('x') :
            cv2.destroyWindow('Scanned photo')
            sr= int(input("Enter the coordinates of the starting row of the cropped image"))
            er = int(input("Enter the coordinates of the ending row of the cropped image"))
            sc = int(input("Enter the coordinates of the starting column of the cropped image"))
            ec = int(input("Enter the coordinates of the starting column of the cropped image"))
            cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg" % i, frame)
            image = cv2.imread('C://Users//NIKITA//pdf//scanned%d.jpg'%i)
            cropped = image[sr:er, sc:ec]
            cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg" % i, cropped)
            i = i + 1
            print("Press 's' to scan more documents")
            print("Press 'q' to quit")
            continue



        # for finding and drawing contours for the given image
        
        elif k1== ord('c') :

                cv2.destroyWindow('Scanned photo')
                grayscaled = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                cannied_img = cv2.Canny(frame, 100, 200)
                gaussian_blurred = cv2.GaussianBlur(cannied_img, (5, 5), 0, 0)
                countours, hierarchy = cv2.findContours(gaussian_blurred, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
                cv2.drawContours(frame, countours, -1, (0, 255, 0), 2)
                cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg" % i, frame)
                i = i + 1
                print("Press 's' to scan more documents")
                print("Press 'q' to quit")
                continue       

        #for resizing the image

        elif k1 == ord('r') :
            cv2.destroyWindow('Scanned photo')
            w=int(input("Enter the new width of the image"))
            h=int(input("Enter the new height of the image"))
            cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg" % i, frame)
            img = cv2.imread('C://Users//NIKITA//pdf//scanned%d.jpg' % i)
            res = cv2.resize(img, dsize=(w,h), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg" % i,res)
            i = i + 1
            print("Press 's' to scan more documents")
            print("Press 'q' to quit")
            continue

        #for adding text to the image

        elif k1 == ord('t') :
            cv2.destroyWindow('Scanned photo')
            text=input("Enter the text you want to add")
            x=int(input("Enter the x-coordinate of the position of the image"))
            y=int(input("Enter the y-coordinate of the position of the image"))
            fontscale=int(input("Enter the font scale of the image"))
            print("Enter the color in terms of bgr values")
            b=int(input())
            g=int(input())
            r=int(input())
            t=int(input("Enter the thickness of the text"))
            cv2.putText(frame, text, (x,y),  cv2.FONT_HERSHEY_SIMPLEX, fontscale, (b, g, r),t, cv2.LINE_AA)
            cv2.imwrite("C://Users//NIKITA//pdf//scanned%d.jpg" % i, frame)
            i = i + 1
            print("Press 's' to scan more documents")
            print("Press 'q' to quit")
            continue


    elif k==ord('q') & 0xFF:
        ret= False
        break

cv2.destroyAllWindows()

r=0
im=[]
imagelist = os.listdir("C://Users//NIKITA//pdf")
for image in imagelist:
    path="C://Users//NIKITA//pdf//"+image
    im.append(0)
    im[r]=Image.open(path)
    r+=1
imv=im.pop(0)
imv.save(r'C://Users//NIKITA//your_file.pdf',save_all=True, append_images=imagelist)





