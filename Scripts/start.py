
# GUI first page
# Driver and emergency contact details before starting driving


# import packages
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from PIL import Image
import re

# import scripts
import fatigue_backend

# regular expression for validating an email
REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def is_valid_email(email):
    return re.fullmatch(REGEX, email)


class InfoPage:

    def __init__(self, root):

        # root
        self.root = root
        self.root.title("RoadGuardian")
        self.root.geometry("800x420+100+50")
        self.root.resizable(False, False)  # disable resizing

        # bg_image
        background = PhotoImage(file="../Data/bg_img (2).png")
        Label(self.root, image=background).place(x=250, y=0)

        # info_page
        info_page = Frame(root, bg="white")
        info_page.place(x=0, y=0, height=1000, width=500)

        #logo
        logo_frame = Frame(info_page, width=200, height=100)  #create a frame
        logo_frame.place(anchor='se', relx=0.75, rely=0.12)
        logo_image = ImageTk.PhotoImage(Image.open("../Data/logo_final.png"))  # create an ImageTk object
        Label(logo_frame, image=logo_image, background="white").pack()  # create a label widget to display the image

        # note label
        Label(info_page, text="Welcome! Please enter your name.The emergency\n number shall be contacted in case of repeated fatigue alarms.", font=("Helvetica", 11, "bold italic"), fg="#3a65ab", bg="white").place(x=20, y=110)
        # driver name label and text box
        Label(info_page, text="Name", font=("Helvetica", 12, "bold italic"), fg="#B80008", bg="white").place(x=30, y=150)
        self.txt_driver_name = Entry(info_page, font=("times new roman", 15), bg="white")
        self.txt_driver_name.place(x=35, y=180, width=350, height=25)


        # contact name label and text box
        Label(info_page, text="Name of Emergency Contact", font=("Helvetica", 12, "bold italic"), fg="#B80008", bg="white").place(x=30, y=210)
        self.txt_name_contact = Entry(info_page, font=("times new roman", 15), bg="white")
        self.txt_name_contact.place(x=35, y=240, width=350, height=25)

        # contact email label and text box
        Label(info_page, text="Emergency Email", font=("Helvetica", 12, "bold italic"), fg="#B80008", bg="white").place(x=30, y=270)
        self.txt_email_contact = Entry(info_page, font=("times new roman", 15), bg="white")
        self.txt_email_contact.place(x=35, y=300, width=350, height=25)

        # start button
        Button(self.root, command=self.start_function, text="Start Driving", bg="#3a65ab", font=("times new roman", 12, "bold italic"), fg ="white").place(x=150, y=350, width=100, height=30)

        # infinite loop waiting for an event to occur and process the event as long as the window is not closed
        root.mainloop()

    def start_function(self):
        """This function checks the correctness of the input and starts the system, in case of missing or incorrect details messagebox will appear"""

        # if there is an empty field, show an error message
        if self.txt_email_contact.get() == "" or self.txt_driver_name.get() == "" or self.txt_name_contact.get() == "":
            messagebox.showerror("Error", "All fields are required.", parent=self.root)

        # if the email address is invalid, show an error message
        elif not is_valid_email(self.txt_email_contact.get()):
            messagebox.showerror("Error", "Invalid email address.", parent=self.root)

        # otherwise, show a success message, close the window and start driving
        else:
            messagebox.showinfo("Start Driving", f"{self.txt_driver_name.get()}, have a pleasant journey! \nYour emergency contact is {self.txt_name_contact.get()}. \n\nPlease wait a few seconds...", parent=self.root)
            username, contact_name, contact_email = self.txt_driver_name.get(), self.txt_name_contact.get(), self.txt_email_contact.get()  # these will be deleted when the root is destroyed
            self.root.destroy()
            fatigue_backend.start_driving(username, contact_name, contact_email)


def main():
    InfoPage(Tk())


if __name__ == '__main__':
    main()
