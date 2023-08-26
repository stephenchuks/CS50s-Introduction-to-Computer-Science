#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Define the color you want to use for replacement
    RGBTRIPLE newColor;
    newColor.rgbtBlue = 255; // Set the blue component
    newColor.rgbtGreen = 0;  // Set the green component
    newColor.rgbtRed = 0;    // Set the red component

    // Iterate through each pixel in the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Check if the pixel is black (all components are 0)
            if (image[i][j].rgbtBlue == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtRed == 0)
            {
                // Replace the black pixel with the new color
                image[i][j] = newColor;
            }
        }
    }
}
