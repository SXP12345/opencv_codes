#include <opencv2/core.hpp>         //the basic building blocks of the library
#include <opencv2/imgcodecs.hpp>    //provides functions for reading and writing
#include <opencv2/highgui.hpp>      //contains the functions to show an image in a window
#include <iostream>
using namespace cv;
int main()
{
    /* loads the image using the file path specified by the first argument. 
    The second argument is optional and specifies the format in which we want the image. 
    This may be:
    (1) IMREAD_COLOR loads the image in the BGR 8-bit format. This is the default that is used here.
    (2) IMREAD_UNCHANGED loads the image as is (including the alpha channel if present)
    (3) IMREAD_GRAYSCALE loads the image as an intensity one */
    std::string image_path = samples::findFile("pic.jpg");
    Mat img = imread(image_path, IMREAD_COLOR);
    if(img.empty())
    {
        std::cout << "Could not read the image:" << image_path << std::endl;
        return 1;
    }
    imshow("Display window", img);
    int k = waitKey(0);
    
    if(k == 's')
    {
        imwrite("pic_saved.jpg", img);
    }
    return 0;
}
