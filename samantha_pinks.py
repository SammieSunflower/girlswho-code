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

im = load_img("dev.jpg")
show_img(im)
save_img(im, "devarshi.jpg")
def obamicon(sun):
    pixels = sun.getdata()
    white = (250, 250, 250)
    pink = (230, 67, 145)
    brightpink = (255, 0, 123)
    darkpink = (148, 0, 71)
    black = (41, 20, 30)
    anotherpink = (255, 77, 162)
    newim = []
    width, height = sun.size
    for p in pixels:
        intensity = p[0] + p[1] + p[2]

        if intensity < 170:
            newim.append(darkpink)
        elif intensity >= 170 and intensity < 364:
            newim.append(white)
        elif intensity >= 364 and intensity < 400:
            newim.append(pink)
        elif intensity >= 400 and intensity < 450:
            newim.append(brightpink)
        elif intensity >= 450:
            newim.append(anotherpink)
    sunny = Image.new("RGB", (width, height))
    sunny.putdata(newim)
    sunny.show()
obamicon(im)
