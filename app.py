import PIL.Image as Image
import imageio

from nsfw import classify

image = imageio.imread("images/image.jpg", pilmode="RGB")
sfw, nsfw = classify(image)

print("SFW Probability: {}".format(sfw))
print("NSFW Probability: {}".format(nsfw))
