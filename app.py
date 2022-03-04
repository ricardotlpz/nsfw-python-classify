import PIL.Image as Image
import imageio as io
import matplotlib

from nsfw import classify

image = io.imread("images/image.jpg",plugin='matplotlib')
#with Image.open("images/image.jpg") as image:
sfw, nsfw = classify(image)

print("SFW Probability: {}".format(sfw))
print("NSFW Probability: {}".format(nsfw))
