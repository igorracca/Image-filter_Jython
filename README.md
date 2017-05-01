# Image-filter_Jython

The user enters a series of pictures and the program filters out the unwanted content.

The program was created using the python programming language and [JES](https://github.com/gatech-csl/jes)(Jython Environment for Students) . The filters in the program were designed by obtaining the pixel values of the image then modifying them accordingly with the algorithms implemented within the program.
You can choose to apply an Average or Median filter and see which result will be better.

# Installation 

- The easiest way to run this program is installing JES in a downloadable package, which you can find at https://github.com/gatech-csl/jes/releases. Each of them includes its own JESReadme.txt with instructions.

- Download the repository

# Running the Program

- Run JES 

- Go to `File > Open Program` and browse for `proj1.py`

- Click in `Load Program`

- Type the path of the folder that contains the png images in `Project1Images`

- Type an option `1 for Average filter` or `2 for Median filter`

- It can take a while but it will display the result

# Important

The program reads 10 images with .png extension, named from (1.pgn to 10.png).   
If you want to try another pictures, you have to change the number of picures (line 17) and the extension (line 19) whitin `proj1.py`
