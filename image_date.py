from PIL import Image


def extract_image_date(directory, file):
    im = Image.open(directory + "/" + file)
    st = im._getexif()[36867]
    st = st.split(" ")
    st = str(st[0]).replace(":", "/") + " " + str(st[1])
    return str(st)

