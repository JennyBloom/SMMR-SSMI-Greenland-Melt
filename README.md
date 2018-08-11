# Counting Melted pixels in Greenland for 2007
This project analyzed imagery of Greenlandic melt, where the TIF images have had the XPGR ratio applied allowing quantification of Greenland’s 2007 melted area. This data is used by climate scientists in quantifying melt and predicting sea level rise in response to anthropogenic climate change. 

Pre-processing raw satellite imagery in ASCII format and converting into TIF files was done prior to this project. Images are from the Scanning Multi-channel Microwave Radiometer (SMMR) and the Special Sensor Microwave/Imager (SSM/I) instruments onboard a defense meteorological satellite, DMSR mission. Pre-processing combined these two microwave images with differing polarities of each day. The XPGR ratio was then applied to each combined image. The XPGR ratio acts as a binary indicator of the state of melt found within each pixel on each observed day, by creating a threshold that is a proxy indicator of snow wetness. If a pixel’s XPGR-corrected brightness value is above the threshold, the pixel has released energy as the ice in the image changes state from solid to liquid. Each pixel represents an area of 25 km<sup>2</sup>. Each of the 365 TIF images are `60x109` pixels in size.

## Project Focus:
This was the final python project of the course. The requisites for the project were to include at least:
* 1 main function
* 3 additional functions
* 2 loops (either while or for, or one of each)
* 3 if/elif/else blocks
* 3 numerical variables
* 3 strings
* File I/O and whatever data processing is needed (this is both file input and file output)

## Project Method:
The project folder contains python code, output text, imagery needed for the project, and the whitepaper folder includes screenshots of progress, requirements text of modules needed, and this paper. A dictionary, months, is set up that will be populated with pixels above a threshold value of `-0.0158`. Pixels with values greater than this are considered to be melting, pixels under this value are not counted. Overall, the code only counts pixels that have melted, and only counts them once. These are stored into a dictionary where each month (Jan, Feb, etc) is a key that calls forth a summed count of pixels for each of the daily TIF images. These are totaled, producing all pixels showing ice melt in Greenland for 2007. The area is determined. User prompts allow the user to explore these values within the CLI. When running through the 365 files, a progress bar was created to show the user the code is processing the files.

## Running the Program:
### Requisites:
Pillow==3.0.0
progress==1.2

To get into the VM, within Terminal, include:
```console
pip3 install pillow
pip3 install progress
apt-get install libjpeg-dev
```
Check `pip3` list to see if they are included, and if so,
you're good to run the code.

## Additional Details:
For further reading, please check out the whitepaper on [project description.](https://github.com/JennyBloom/SMMR-SSMI-Greenland-Melt/blob/master/whitepaper/Bloom_Project1.pdf)
