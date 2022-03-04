import PIL.Image as Image

from nsfw import classify

image = Image.open("/path/to/image.jpg")
sfw, nsfw = classify(image)

print("SFW Probability: {}".format(sfw))
print("NSFW Probability: {}".format(nsfw))