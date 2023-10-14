from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import re
import smtplib
ram = Tk()


def abc():
    # Viit canteen bill
    import time
    import random
    # price1,price2,price3,price4,price5,price6,price7,price8

    def price():
        roo = Tk()
        roo.geometry("350x280")
        roo.title("Price List")
        # roo.iconbitmap('C:\PE PBL\\viit-logo-01.ico')
        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
        lblinfo.grid(row=0, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="___", fg="white", anchor=W)
        lblinfo.grid(row=0, column=2)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="black", anchor=W)
        lblinfo.grid(row=0, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="icecream", fg="#ED420B", anchor=W)
        lblinfo.grid(row=1, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="#ED420B", anchor=W)
        lblinfo.grid(row=1, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Aloo Paratha", fg="#ED420B", anchor=W)
        lblinfo.grid(row=2, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="#ED420B", anchor=W)
        lblinfo.grid(row=2, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Poha", fg="#ED420B", anchor=W)
        lblinfo.grid(row=3, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="20", fg="#ED420B", anchor=W)
        lblinfo.grid(row=3, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Upama", fg="#ED420B", anchor=W)
        lblinfo.grid(row=4, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="35", fg="#ED420B", anchor=W)
        lblinfo.grid(row=4, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="vadapav", fg="#ED420B", anchor=W)
        lblinfo.grid(row=5, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W)
        lblinfo.grid(row=5, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text=" Special Thali", fg="#ED420B", anchor=W)
        lblinfo.grid(row=6, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="70", fg="#ED420B", anchor=W)
        lblinfo.grid(row=6, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W)
        lblinfo.grid(row=7, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Coffee", fg="#ED420B", anchor=W)
        lblinfo.grid(row=7, column=0)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="10", fg="#ED420B", anchor=W)
        lblinfo.grid(row=8, column=3)

        lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Tea", fg="#ED420B", anchor=W)
        lblinfo.grid(row=8, column=0)

        roo.mainloop()

    def quit_fun():
        root.destroy()

    def total():
        price1 = int(dringE.get())
        price2 = int(AlooparathaE.get())
        price3 = int(Poha.get())
        price4 = int(upama.get())
        price5 = int(vadapav.get())
        price6 = int(Thali.get())
        price7 = int(Coffee.get())
        price8 = int(tea.get())
        # p1,p2,p3 etc means Price Per Person
        p1 = price1 * 25
        p2 = price2 * 25
        p3 = price3 * 20
        p4 = price4 * 35
        p5 = price5 * 10
        p6 = price6 * 70
        p7 = price7 * 10
        p8 = price8 * 10
        # Cost
        print(p1)
        cost = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
        display = cost
        p1_label["text"] = display
        # Service Tax
        service_charge = cost / 50
        service_display = service_charge
        p2_label["text"] = service_display
        # Tax
        tax_charge = int(cost / 100)
        tax_display = tax_charge
        p3_label["text"] = tax_display
        # Sub Total
        sub_total = p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8
        sub_display = sub_total
        p4_label["text"] = sub_display
        # Total
        total = int(display + service_charge + tax_charge)
        total_display = total
        p5_label["text"] = total_display

        # Order Number
        num = random.randint(1, 1000)
        order_label["text"] = num

    def reset():
        dringE.delete(0, END)
        AlooparathaE.delete(0, END)
        Poha.delete(0, END)
        upama.delete(0, END)
        vadapav.delete(0, END)
        Thali.delete(0, END)
        Coffee.delete(0, END)
        tea.delete(0, END)
        stu_naE.delete(0, END)
        stu_idE.delete(0, END)
        bill_noE.delete(0, END)
        p1_label["text"] = ""
        p2_label["text"] = ""
        p3_label["text"] = ""
        p4_label["text"] = ""
        p5_label["text"] = ""
        order_label["text"] = ""
        random_num = random.randint(1000, 9999)

        # Insert the random number into the bill_noE widget
        bill_noE.insert(0, str(random_num))

    def clock():
        current = time.strftime("%H:%M:%S")
        label1["text"] = current
        root.after(1000, clock)

    def onsubmit():
        name_label = Label(frame4, text=stu_naE.get(), font="arial 15 bold", bg="#96C3EB")
        name_label.place(x=150, y=73)

        id_label = Label(frame4, text=stu_idE.get(), font="arial 15 bold", bg="#96C3EB")
        id_label.place(x=150, y=97)

        billno_label = Label(frame4, text=bill_noE.get(), font="arial 15 bold", bg="#96C3EB")
        billno_label.place(x=150, y=127)

        for i in range(1, 9):
            j = 25 * i
            Table_content = Label(frame4, text=i, bg="#96C3EB", font="arial 12")
            Table_content.place(x=25, y=220 + j)
            menulist = ["Ice-Cream", "Aloo Paratha", "Poha", "Upama", "VadaPav", "Special Thali", "Coffee", "Tea"]
            Table_menu = Label(frame4, text=menulist[i - 1], bg="#96C3EB", font="arial 12")
            Table_menu.place(x=65, y=220 + j)
            Quantitylist = [dringE.get(), AlooparathaE.get(), Poha.get(), upama.get(), vadapav.get(), Thali.get(),
                            Coffee.get(), tea.get()]
            Table_Quantity = Label(frame4, text=Quantitylist[i - 1], bg="#96C3EB", font="arial 12")
            Table_Quantity.place(x=245, y=220 + j)
            price1 = int(dringE.get())
            price2 = int(AlooparathaE.get())
            price3 = int(Poha.get())
            price4 = int(upama.get())
            price5 = int(vadapav.get())
            price6 = int(Thali.get())
            price7 = int(Coffee.get())
            price8 = int(tea.get())
            # p1,p2,p3 etc means Price Per Person
            p1 = price1 * 25
            p2 = price2 * 25
            p3 = price3 * 20
            p4 = price4 * 35
            p5 = price5 * 10
            p6 = price6 * 70
            p7 = price7 * 10
            p8 = price8 * 10
            pricelist_l = [p1, p2, p3, p4, p5, p6, p7, p8]
            Table_price = Label(frame4, text=pricelist_l[i - 1], bg="#96C3EB", font="arial 12")
            Table_price.place(x=415, y=220 + j)
            Total = int(p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8)
            subtotal = int((103 / 100) * Total)
            nettotal = Label(frame4,
                             text=f"Net Total {subtotal}\n\n\n Sir Please Pay ₹{subtotal}\n\n\n Thank you for Visiting"f"\n\nVisit again!!!",
                             font="arial 12 bold", bg="#96C3EB", fg="blue")
            nettotal.place(x=525, y=220)

    def save_bill():
        import smtplib
        import os
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from PIL import ImageGrab

        # Take a screenshot using Pillow
        screenshot = ImageGrab.grab()

        # Save the screenshot to a file on your system
        screenshot.save('screenshot.png')

        # Get the file size in bytes
        file_size = os.path.getsize('screenshot.png')

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = 'rambojadhavabhi@gmail.com'
        msg['To'] = 'kushal.22110853@viit.ac.in'
        msg['Subject'] = 'Screenshot'

        # Add the image as an attachment to the email message
        with open('screenshot.png', 'rb') as fp:
            img = MIMEImage(fp.read(), _subtype='png')
            img.add_header('Content-Disposition', 'attachment', filename='screenshot.png')
            msg.attach(img)

        # Add a text message to the email
        body = MIMEText(f'Screenshot attached. File size: {file_size} bytes.')
        msg.attach(body)

        # Connect to the SMTP server and send the email
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'rambojadhavabhi@gmail.com'
        smtp_password = 'aoieopztlvnroiub'
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(msg['From'], msg['To'], msg.as_string())

    root = Tk()
    root.geometry("1500x800")
    # root.iconbitmap('C:\PE PBL\\viit-logo-01.ico')
    heading1 = Label(root, text="VIIT Canteen", font="Italic 48 bold", fg="red")
    heading2 = Label(root, text="Vishwakarma Institutes ", font="arial 18 bold", fg="blue")
    frame1 = Frame(root, height="460", width="330", bd=10, bg="#ffcccb", highlightthickness=1, relief=SUNKEN)
    frame1.place(x=40, y=230)

    frame2 = Frame(root, height="460", width="500", bd=10, bg="#CCCCCC", highlightthickness=1, relief=SUNKEN)
    frame2.place(x=380, y=230)
    # Button Frame
    frame3 = Frame(root, height="100", width="1455", bd=10, bg="#696969", highlightthickness=1, relief=SUNKEN)
    frame3.place(x=40, y=685)
    # bill frame
    frame4 = Frame(root, height="460", width="800", bd=10, bg="#96C3EB", highlightthickness=1, relief=SUNKEN)
    frame4.place(x=700, y=230)
    # customer frame
    frame5 = Frame(root, height="100", width="1455", bd=10, bg="#FF6633", highlightthickness=1, relief=SUNKEN)
    frame5.place(x=40, y=125)
    frame_time = Frame(root, height="200", width="200", bd=10, highlightthickness=1, relief=SUNKEN)
    frame_time.place(x=100, y=50)
    # Price Frame
    p1_label = Label(frame2, font="arial 14 bold ", bg="#CCCCCC")
    p1_label.place(x=200, y=80)
    p2_label = Label(frame2, font="arial 14 bold ", bg="#CCCCCC")
    p2_label.place(x=200, y=120)
    p3_label = Label(frame2, font="arial 14 bold ", bg="#CCCCCC")
    p3_label.place(x=200, y=160)
    p4_label = Label(frame2, font="arial 14 bold ", bg="#CCCCCC")
    p4_label.place(x=200, y=200)
    p5_label = Label(frame2, font="arial 14 bold ", bg="#CCCCCC")
    p5_label.place(x=200, y=240)
    order_label = Label(frame2, font="arial 14 bold ", bg="#CCCCCC")
    order_label.place(x=200, y=40)

    # Time
    label1 = Label(frame_time, font="article 30", bg="black", fg="#ED420B")
    label1.grid(row=0, column=0)
    clock()
    # Buttons

    # Frame 3
    new_window = Button(frame3, text="  Menu Price  ", command=price, font="arial 15 bold", bd=8)
    new_window.place(x=80, y=10)
    total_btn = Button(frame3, text="  Calculate Bill  ", command=total, font="arial 15 bold", bd=8)
    total_btn.place(x=280, y=10)
    reset_btn = Button(frame3, text="  Reset  ", command=reset, font="arial 15 bold", bd=8)
    reset_btn.place(x=500, y=10)
    quit_btn = Button(frame3, text="  Exit  ", command=quit_fun, font="arial 15 bold", bd=8)
    quit_btn.place(x=650, y=10)
    View_bill = Button(frame3, text="  View Bill  ", command=onsubmit, font="arial 15 bold", bd=8)
    View_bill.place(x=800, y=10)
    Save_bill = Button(frame3, text="  Save Bill  ", command=save_bill, font="arial 15 bold", bd=8)
    Save_bill.place(x=1000, y=10)

    # Frame_2 Labelling
    order_number = Label(frame2, text="Order Number", font="arial 12 bold", bg="#CCCCCC")
    cost_label = Label(frame2, text="Cost", font="arial 12 bold ", bg="#CCCCCC")
    service_tax = Label(frame2, text="Service Cost", font="arial 12 bold", bg="#CCCCCC")
    tax = Label(frame2, text="Tax", font="arial 12 bold ", bg="#CCCCCC")
    sub_total = Label(frame2, text="Sub Total", font="arial 12 bold", bg="#CCCCCC")
    total = Label(frame2, text="You Have To Pay", font="arial 12 bold ", bg="#CCCCCC")
    # Frame_2 Label position
    order_number.place(x=10, y=40)
    cost_label.place(x=10, y=80)
    service_tax.place(x=10, y=120)
    tax.place(x=10, y=160)
    sub_total.place(x=10, y=200)
    total.place(x=10, y=240)

    # Frame 1 Entry
    dringE = Entry(frame1, bd="3")
    dringE.insert(0,"0")
    AlooparathaE = Entry(frame1, bd="5")
    AlooparathaE.insert(0,"0")
    Poha = Entry(frame1, bd="5")
    Poha.insert(0,"0")
    upama = Entry(frame1, bd="5")
    vadapav = Entry(frame1, bd="5")
    Thali = Entry(frame1, bd="5")
    Coffee = Entry(frame1, bd="5")
    tea = Entry(frame1, bd="5")

    # Frame 4 Labelling.
    billp = Label(frame4, text="Student Name:", bg="#96C3EB", font="arial 12 bold")
    mo_number = Label(frame4, text="Student Id:", bg="#96C3EB", font="arial 12 bold")
    ono_label = Label(frame4, text="Bill No:", bg="#96C3EB", font="arial 12 bold ")
    gstn_tax = Label(frame4, text="GSTIN : 22AAAAA000A1Z5", bg="#96C3EB", font="arial 12 bold")
    headl = Label(frame4, text="VIIT Canteen", bg="#96C3EB", font="arial 12 bold ")
    meal_total = Label(frame4, text="Meal Details:", bg="#96C3EB", font="arial 12 bold")
    line_total = Label(frame4, text="________", bg="#96C3EB", font="arial 12 bold")
    linet_total = Label(frame4, text="________", bg="#96C3EB", font="arial 12 bold")
    srno_label = Label(frame4, text="Sr.No", bg="#96C3EB", font="arial 12 bold")
    a_label = Label(frame4, text="Item", bg="#96C3EB", font="arial 12 bold")
    b_label = Label(frame4, text="Quantity", bg="#96C3EB", font="arial 12 bold")
    c_label = Label(frame4, text="Total", bg="#96C3EB", font="arial 12 bold")
    d_label = Label(frame4, text="", bg="#96C3EB", font="arial 12 bold")
    e_label = Label(frame4, text="Sr.No", bg="#96C3EB", font="arial 12 bold")
    f_label = Label(frame4, text="Sr.No", bg="#96C3EB", font="arial 12 bold")

    # Frame 4 Position..
    billp.place(x=5, y=70)
    mo_number.place(x=5, y=100)
    ono_label.place(x=5, y=130)
    gstn_tax.place(x=550, y=40)
    headl.place(x=300, y=15)
    meal_total.place(x=5, y=180)
    line_total.place(x=5, y=35)
    linet_total.place(x=5, y=155)
    srno_label.place(x=5, y=210)
    a_label.place(x=75, y=210)
    b_label.place(x=225, y=210)
    c_label.place(x=355, y=210)

    # frame5 Labelling
    stu_na = Label(frame5, text="Student Name:", font="arial 12 bold", bg="#696969")
    stu_id = Label(frame5, text="Student ID:", font="arial 12 bold", bg="#696969")
    bill_no = Label(frame5, text="Bill Number:", font="arial 12 bold", bg="#696969")
    stu_naE = Entry(frame5, bd="5")
    stu_naE.place(x=5, y=40)
    stu_idE = Entry(frame5, bd="5")
    stu_idE.place(x=525, y=40)
    bill_noE = Entry(frame5, bd="5")
    bill_noE.place(x=1025, y=40)
    random_num = random.randint(1000, 9999)

    # Insert the random number into the bill_noE widget
    bill_noE.insert(0, str(random_num))

    # Frame5 Position
    stu_na.place(x=5, y=10)
    stu_id.place(x=525, y=10)
    bill_no.place(x=1025, y=10)
    Submission = Button(frame5, text=" Proceed For bill  ", command=onsubmit, font="arial 10 bold", bd=1)
    Submission.place(x=1230, y=40)

    # Frame1_objects Entry
    dringE = Entry(frame1, bd="3")
    dringE.insert(0,"0")
    AlooparathaE = Entry(frame1, bd="5")
    AlooparathaE.insert(0,"0")
    Poha = Entry(frame1, bd="5")
    Poha.insert(0,"0")
    upama = Entry(frame1, bd="5")
    upama.insert(0,"0")
    vadapav = Entry(frame1, bd="5")
    vadapav.insert(0,"0")
    Thali = Entry(frame1, bd="5")
    Thali.insert(0,"0")
    Coffee = Entry(frame1, bd="5")
    Coffee.insert(0,"0")
    tea = Entry(frame1, bd="5")
    tea.insert(0,"0")

    # Frame_1_objects
    dringE.place(x=140, y=35)
    AlooparathaE.place(x=140, y=80)
    Poha.place(x=140, y=125)
    upama.place(x=140, y=170)
    vadapav.place(x=140, y=215)
    Thali.place(x=140, y=260)
    Coffee.place(x=140, y=305)
    tea.place(x=140, y=350)

    # Frame1_objects
    icecream_label = Label(frame1, text="Icecream", font="arial 15 bold ", bg="#ffcccb")
    Alooparatha_label = Label(frame1, text="Aloo Paratha", font="arial 15 bold", bg="#ffcccb")
    Poha_label = Label(frame1, text="Poha", font="arial 15 bold", bg="#ffcccb")
    upama_label = Label(frame1, text="Upama", font="arial 15 bold", bg="#ffcccb")
    vadapav_label = Label(frame1, text="Vada pav", font="arial 15 bold ", bg="#ffcccb")
    Thali_label = Label(frame1, text="Special Thali", font="arial 15 bold", bg="#ffcccb")
    Coffee_label = Label(frame1, text="Coffee", font="arial 15 bold ", bg="#ffcccb")
    tea_label = Label(frame1, text="Tea", font="arial 15 bold ", bg="#ffcccb")

    # Frame 1 Object position
    icecream_label.place(x=10, y=35)
    Alooparatha_label.place(x=10, y=80)
    Poha_label.place(x=10, y=125)
    upama_label.place(x=10, y=175)
    vadapav_label.place(x=10, y=215)
    Thali_label.place(x=10, y=260)
    Coffee_label.place(x=10, y=305)
    tea_label.place(x=10, y=350)
    heading1.place(x=600, y=10)
    heading2.place(x=650, y=80)

    root.title("VIIT Canteen Bill counter")
    # root.iconbitmap('C:\PE PBL\\viit-logo-01.ico')
    root.mainloop()


heading3 = Label(ram, text="Vishwakarma Institutes", font="Italic 18 bold", fg="red")
heading4 = Label(ram, text="VIIT Canteen", font="arial 48 bold", fg="blue")
heading5 = Label(ram, text='''Welcome to VIIT canteen. Please follow Covid Rules and Regulations
, Maintain Social Distancing ,All tables are sanitized. So Enjoy Food delightfully.
 Access this application to see menu and download bill.
''', font="arial 20 bold", fg="black")
heading3.place(x=600, y=30)
heading4.place(x=550, y=80)
heading5.place(x=250, y=250)


def admin():
    admin123 = Tk()
    admin123.title("Admin Login")
    admin_frame = Frame(admin123, height="350", width="500", bd=10, bg="#696969", highlightthickness=1, relief=SUNKEN)
    admin_frame.place(x=70, y=75)
    general = Label(admin_frame, text="Please login by Correct Credentials", font="arial 15 bold ", bg="#ffcccb")
    general.place(x=20, y=10)
    user_label = Label(admin_frame, text="Username", font="arial 15 bold ", bg="#696969")
    user_label.place(x=45, y=55)
    user_labelE = Entry(admin_frame, bd=5)
    user_labelE.place(x=150, y=55)
    email = Label(admin_frame, text="Email", font="arial 15 bold ", bg="#696969")
    email.place(x=45, y=95)
    email_labelE = Entry(admin_frame, bd=5)
    email_labelE.place(x=150, y=95)

    def z():
        admin123.destroy()

    def all_nvalid():
        regex = re.compile(r"^[a-z]+\.\d{8}@viit\.ac\.in$")

        if(re.fullmatch(regex,email_labelE.get())):
        # if email_labelE.get() =="0000" and  user_labelE.get() == "VIIT123":
            z()
            abc()
        else:
            text1_label = Label(admin_frame, text="Email or Username is Invalid !!!!!", font="arial 15 bold ",
                                bg="#696969")
            text1_label.place(x=90, y=260)

    Submit123 = Button(admin123, text="Login", command=all_nvalid, bg="green", font="arial 18 bold", bd=10)
    Submit123.place(x=150, y=250)
    admin123.minsize(600, 600)
    ram.destroy()
    admin123.mainloop()


# By Pressing Keyboard Buttons
def key_press(e):
    admin()


def key_released(e):
    return


# admin login
Admin = Button(text="Admin Login", command=admin, bg="green", font="arial 18 bold", bd=15)
Admin.place(x=650, y=400)
ram.minsize(1500, 1000)
ram.title("VIIT Canteen Management")

ram.bind('<KeyPress>', key_press)
ram.bind('<KeyRelease>', key_released)
ram.mainloop()
