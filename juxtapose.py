from PIL import Image
import argparse

p = argparse.ArgumentParser(description="Juxtapose two image to compare them")
p.add_argument("path1", default="1.jpg", help="PATH of the 1 Image")
p.add_argument("path2", default="2.jpg", help="PATH of the 2 Image")
p.add_argument("-m", "--mode", type=int, default=0, help="Mode 1: Put them next to each other. Mode 0: Juxtapose the two half")
args = p.parse_args()


def juxtapose0(im1, im2): #JUXTAPOSE THE TWO HALF
    w1, h1 = im1.size
    w2, h2 = im2.size
    h = min(h1, h2)
    new_w1 = w1 * h / h1
    new_w2 = w2 * h / h2

    im1 = im1.resize((int(new_w1), h), Image.ANTIALIAS)
    im2 = im2.resize((int(new_w2), h), Image.ANTIALIAS)
    back = Image.new('RGBA', (int((new_w1 + new_w2) / 2), h), 0)
    back.paste(im1, (0, 0))
    back.paste(im2.crop((new_w1 / 2, 0, new_w1 + new_w2, h)), (int((new_w1) / 2), 0))
    print("DONE")
    back.save("mode0output.jpg")


def juxtapose1(im1, im2): #JUXTAPOSE FULL IMAGES
    w1, h1 = im1.size
    w2, h2 = im2.size
    h = min(h1, h2)
    new_w1 = w1 * h / h1
    new_w2 = w2 * h / h2

    im1 = im1.resize((int(new_w1), h), Image.ANTIALIAS)
    im2 = im2.resize((int(new_w2), h), Image.ANTIALIAS)
    back = Image.new('RGBA', (int(new_w1 + new_w2), h), 0)
    back.paste(im1, (0, 0))
    back.paste(im2, (int((new_w1)), 0))
    print("DONE")
    back.save("mode1output.jpg")


def main():
    try:
        im1 = Image.open(args.path1)
        im2 = Image.open(args.path2)
    except IOError:
        print ("Error in opening the images files")
        quit()
    if args.mode:
        juxtapose1(im1, im2)
    else:
        juxtapose0(im1, im2)

if __name__ == '__main__':
    main()