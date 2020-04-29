from tkinter import *
from PIL import ImageTk, Image

global x
x = -1

root = Tk()
root.title("Image Viewer")

image1 = ImageTk.PhotoImage(Image.open("1.jpg"))
image2 = ImageTk.PhotoImage(Image.open("2.jpg"))
image3 = ImageTk.PhotoImage(Image.open("3.jpg"))
image4 = ImageTk.PhotoImage(Image.open("4.jpg"))
image5 = ImageTk.PhotoImage(Image.open("5.jpg"))

image1_label = Label(root, image=image1)
image2_label = Label(root, image=image2)
image3_label = Label(root, image=image3)
image4_label = Label(root, image=image4)
image5_label = Label(root, image=image5)

image_list = [image1_label, image2_label, image3_label, image4_label, image5_label]

def pack_img(index):
    image_list[index].grid(row=1, column=0, columnspan=3)


def next_img():
    global x
    if x == len(image_list)-1:   # X has reached it maximum value
        return
    image_list[x].grid_forget()
    x += 1
    pack_img(x)
    return


def prev_img():
    # Takes x value of current image, reduces it by one and packs the image with x-1 value
    global x
    if x == 0:  # If x=0, the current image is the first image, so no previous image
        return
    image_list[x].grid_forget()
    x -= 1
    pack_img(x)
    return


def quit_():
    root.quit()


quit_button = Button(text="Quit", command=quit)
quit_button.grid(row=0, column=1)

prev_button = Button(text="Previous", command=prev_img)
prev_button.grid(row=0, column=0)

next_button = Button(text="Next", command=next_img)
next_button.grid(row=0, column=2)

next_img()


root.mainloop()














