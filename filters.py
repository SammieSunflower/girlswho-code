from PIL import Image
sun = Image
# Rename this file to be "filters.py"
# Add commands to import modules here.
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(sun):
    im = Image.open(sun)
    return im

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(sun):
    sun.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(sun, sunflower):
    sun.save(sunflower)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.


im = load_img("sun.jpg")
show_img(im)
save_img(im, "sunflower.jpg")
def obamicon(sun):
    pixels = sun.getdata()
    darkblue = (0, 51, 76)
    red = (217, 26, 33)
    lightblue = (112, 150, 158)
    yellow = (252, 227, 166)
    newim = []
    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 182:
            newim.append(darkblue)
        elif intensity >= 182 and intensity < 364:
            newim.append(red)
        elif intensity >= 364 and intensity < 546:
            newim.append(lightblue)
        elif intensity >= 546:
            newim.append(yellow)
    sunny = Image.new("RGB", (775, 515))
    sunny.putdata(newim)
    sunny.show()
obamicon(im)
#save_img(sunny, "sunny.jpg")
#sun.size
