import streamlit as st
#from rembg import remove
from PIL import Image
from io import BytesIO
import base64
from streamlit_image_coordinates import streamlit_image_coordinates


st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Test StreamApp")
st.write(
    ":dog: Try uploading an image"
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Download the fixed image

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    value = streamlit_image_coordinates(image)

    st.write(value)


    # Size of the image in pixels (size of original image)
    # (This is not mandatory)
    width, height = image.size

    st.write('The image size is w and h ', width, height)
    xresize = st.sidebar.slider("crop x", min_value=0, max_value=int(width/2))
    yresize = st.sidebar.slider("crop y", min_value=0, max_value=int(height / 2))
    # Setting the points for cropped image
    #left = 5
    #top = height / 4
    #right = 164
    #bottom = 3 * height / 4

    # Cropped image of above dimension
    # (It will not change original image)
    fixed = image.crop((xresize, yresize, width-xresize, height-yresize))

    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

number = st.sidebar.number_input('Insert a number')

st.write('The current number is ', number)

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./zebra.jpg")