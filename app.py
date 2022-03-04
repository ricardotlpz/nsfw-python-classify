import PIL.Image as Image

from nsfw import classify

with Image.open("images/image.jpg") as image:
    sfw, nsfw = classify(image)

print("SFW Probability: {}".format(sfw))
print("NSFW Probability: {}".format(nsfw))
