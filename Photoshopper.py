#Jessica Hoang
#30064517
#A program that takes a set of images and takes the portion where there is nothing to create a new
#image with the things(tourist) that you don't want. So it is left with just the landscape.
from simplegraphic import *

# Part 1
#Takes the input given by the user and stores it into a list. 
#Does not take anything as its parameter
def loadImages():
    #Read the input from the user #Change the variable name!!! 
    abrev_imageSubject = input("Enter the image you want you work with")
    num_image = int(input("Enter the number of images"))
    #Store all the images in a list where it can be loaded
    imageList = [] 
    #Make sure the number of image entered is in the right range
    if 3 <= num_image <= 16:
        #Load the image
        for i in range(1,num_image + 1):
            imageName = abrev_imageSubject + "_" + str(i) + ".png"
            img_num = loadImage(imageName)  
            #constantly add the number of images into the imageList
            imageList.append(img_num)
            
            #Resize the width and height
            width = getWidth(img_num)
            height = getHeight(img_num)
            resize(2 * width, height)
        #Returns(gives us a list of images that we call upon when we want to draw the
        #thumbnail and remove tourist. 
        return imageList 
    #Close the program if it is not
    else:
        print("The number you entered is not in the correct range")
        close()
        quit()

#Part 2
#This function creates an image that is 1/4 of the original width and height so that it can be
#drawn in drawThumbnail properly on the left side of the window. 
#The parameter takes on only ONE image 
def createThumbnail(image):
    #gets the width and height of an image. 
    width = getWidth(image)
    height = getHeight(image)
    #Resize the new image 
    newimage = createImage(width // 4, height // 4)
    #Loop to add every 4th pixel horizontally 
    for x_coord in range(0, width, 4):
    #Loop to add every 4th pixel vertically
        for y_coord in range(0, height, 4):
            r,g,b = getPixel(image,x_coord,y_coord)
            putPixel(newimage,x_coord // 4, y_coord // 4,r,g,b)
    #returns(create) a new image with the new pixels that we have gathered. 
    return newimage

#Draws the images from the list on the left side of the window.
#Parameter takes on a list of imageS 
def drawThumbnails(images):
        #gather the width and height of the resized image to use as x and y coordinates of each image.
        width = getWidth(images[0])
        height = getHeight(images[0])
        WIDTHFACTOR = (width//4)
        HEIGHTFACTOR = (height//4)
    #Initialize position to 0 
        countImage = 0
        #Draw DIFFERENT images that fills up the first row and then continues onto the next
        #Each row should only fill up up to 4 images. 
        for i in images:
            if countImage < 4:
                drawImage(createThumbnail(i),countImage*WIDTHFACTOR, 0)
            elif countImage < 8:
                drawImage(createThumbnail(i),(countImage%4)*WIDTHFACTOR, HEIGHTFACTOR)
            elif countImage < 12:
                drawImage(createThumbnail(i),(countImage%4)*WIDTHFACTOR, HEIGHTFACTOR*2)
            else:
                drawImage(createThumbnail(i),(countImage%4)*WIDTHFACTOR, HEIGHTFACTOR*3)
            #Constantly add to the width so that drawImage isn't in the same spot
            countImage += 1
#This function does not return a value 

#Part 3
#Find the median of a list that contains pixels.
#This parameter takes on a List that we will be using in the remove function.
def Median(pixelList):
    #Sort the list in ascending order 
    pixelList.sort()
    if len(pixelList) % 2 == 0:
        #Compute the avg of the 2 middle element in the list
        median = (pixelList[len(pixelList) // 2 - 1] + pixelList[len(pixelList) // 2]) / 2
    else:
        #Find the middle element
        median = pixelList[len(pixelList) // 2]
    return median 

#Remove the tourist from the landsscape
#This parameter also takes on a list of imageS 
def removeTourists(images):
    #draw an image with half of the windows width and the full height in the second half of the window.
    width = getWidth(images[0])
    height = getHeight(images[0])
    new_Image = createImage(width, height) 
    drawImage(new_Image,width, 0)
    #get pixels from the whole image; from width to height. 
    for x_coord in range(0, width):
        for y_coord in range(0, height):
            #create a list for each colour set. 
            redList = []
            greenList = []
            blueList = []
            #gather the pixels from each image and add them into constantly into their appropriate list.
            for image in images:
                r,g,b = getPixel(image,x_coord,y_coord)
                redList.append(r)
                greenList.append(g)
                blueList.append(b)
            #Put the pixel back so that we can draw the image with using each list's median 
            putPixel(new_Image,x_coord, y_coord,Median(redList),Median(greenList),Median(blueList))
        update()
#this function does not return a value 

def main():
  images = loadImages()
  drawThumbnails(images)
  removeTourists(images)

main()
