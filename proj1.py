"""
Author: Igor Racca
Brief: This program performs a median or an average filter (depending on the user's choice) on a series of images in order to remove a person from a scenario.
GitHub Repositoy: https://github.com/igorracca/project01
"""

#folder = "Project1Images/"
folder = requestString("Please type path of the folder that contains the images: ")

# get user option 1-Average 2-Median
option = requestNumber("Enter an option:\n1)Average\n2)Median\n")

# list to store pictures
pictures = []

# get pictures
for x in range(1,10):
  #converts x in string
  image = folder + "\\" + str(x) + ".png"
  image = makePicture(image)
  pictures.append(image)
  
width = getWidth(pictures[0])
height = getHeight(pictures[0])

canvas = makeEmptyPicture(width,height)

for x in range(0, width):
  for y in range(0, height):
    # Clear our red, green, blue value lists
    redPixelList = []
    greenPixelList = []
    bluePixelList = []

    # we have 9 images
    for imageNumber in range(0,9):
      """
      JES getPixel function takes as input
      a picture object and coordinate pair
      """
      pixel = getPixel(pictures[imageNumber], x, y)

      red = getRed(pixel)
      green = getGreen(pixel)
      blue = getBlue(pixel)

      redPixelList.append(red)
      greenPixelList.append(green)
      bluePixelList.append(blue)

    if option == 1:
      # Do average calculations
      newRed = sum(redPixelList) / len(redPixelList)
      newGreen = sum(greenPixelList) / len(greenPixelList)
      newBlue = sum(bluePixelList) / len(bluePixelList)   
      
    elif option == 2:
      # Do median calculations
      medianIndex = (len(redPixelList) + 1) / 2
      
      redPixelList = sorted(redPixelList)
      greenPixelList = sorted(greenPixelList)
      bluePixelList = sorted(bluePixelList)
        
      newRed = redPixelList[medianIndex] 
      newGreen = greenPixelList[medianIndex]
      newBlue = bluePixelList[medianIndex]
      
    color = makeColor(newRed, newGreen, newBlue)   
    # Set red, green blue values for the pixel for the output image
    setColor(getPixel(canvas,x,y), color)

show(canvas)