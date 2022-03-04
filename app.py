import PIL.Image as Image
import imageio 

from nsfw import classify

image = imageio.imread(image, pilmode="RGB")
#with Image.open("images/image.jpg") as image:
sfw, nsfw = classify(image)

print("SFW Probability: {}".format(sfw))
print("NSFW Probability: {}".format(nsfw))
