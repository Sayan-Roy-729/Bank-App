from tkinter import *
from dbhelper import DBHelper
from PIL import Image, ImageTk
from tkinter import messagebox
import qrcode
from datetime import date


class Bank():

    def __init__(self):
        

        # Connect to the database
        self.db = DBHelper()

        self.load_login_window()

    def load_login_window(self):

        self._root = Tk()

        self._root.minsize(450, 600)
        self._root.maxsize(450, 600)
        self._root.config(background="#630db8")


        # This is for the icon in the main window
        self._root.wm_iconbitmap('icon1.ico')


        # This will create style object 
        # self._style = Style() 
        # This will be adding style, and  
        # naming that style variable as  
        # W.Tbutton (TButton is used for ttk.Button). 
        # self._style.configure('W.TButton', font = ('calibri', 20), foreground = '#1239bb',background='#080698', border=5)

        self._root.title("deskBANK")

        self._label1 = Label(self._root, text="WELCOME deskBANK", foreground="#E9E612", background="#630db8")
        self._label1.config(font=("Chalet-LondonNineteenSeventy", 25))
        self._label1.pack(pady=(30, 0))



        # Display the app image in login page
        imageUrl = "icon1.ico"
        load = Image.open(imageUrl)
        load = load.resize((50, 50), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack(pady=(2,2))



        # Login Button Label
        self._label2 = Label(self._root, text="Already a member? Log-in here", foreground="#E9E612", background="#630db8")
        self._label2.config(font=(30))
        self._label2.pack(pady=(50, 5))


        # Login Button
        self._login = Button(self._root, text="Login", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.login_handler())
        self._login.pack()



        # Forgot Password Label
        self._label2 = Label(self._root, text="Forgot password?", foreground="#E9E612", background="#630db8")
        self._label2.config(font=(30))
        self._label2.pack(pady=(50, 5))


        # Reset Password Button
        self._login = Button(self._root,text="Reset Password",bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.reset_password_page())
        self._login.pack()


        # Register Button Label
        self._label3 = Label(self._root, text="Not a member? Register here", foreground="#E9E612", background="#630db8")
        self._label3.config(font=(30))
        self._label3.pack(pady=(50, 5))

        # Register Button
        self._register = Button(self._root,  text="Register", bg='#556ce9',fg='white', width=20, height = "1", font= 20, command=lambda: self.regWindow1())
        self._register.pack()


        self.current_date_time()
                            
        self._root.mainloop()

    def reset_password_page(self):

        self.clear()

        self._warning_label = Label(self._root, text="Email & Acc No should be matched.", foreground="#E9E612", background="#630db8")
        self._warning_label.config(font=(16))
        self._warning_label.pack(pady=(30, 30))

        # email label
        self._email = Label(self._root, text="Email", foreground="#E9E612", background="#630db8")
        self._email.config(font=(16))
        self._email.pack(pady=(50,5))

        # email input
        self._emailInput = Entry(self._root, width=50)
        self._emailInput.pack(pady=(5,10), ipady=10, ipadx=30)

        # acc_no_ label
        self._acc_no_ = Label(self._root, text="Account No.(5 - digit):", foreground="#E9E612", background="#630db8")
        self._acc_no_.config(font=(16))
        self._acc_no_.pack(pady=(20,5))

        # acc_no input
        self._acc_no_Input = Entry(self._root, width=50)
        self._acc_no_Input.pack(pady=(5,10), ipady=10, ipadx=30)

        # password label
        self._password = Label(self._root, text="New password", foreground="#E9E612", background="#630db8")
        self._password.config(font=(16))
        self._password.pack(pady=(10, 5))

        # password input
        self._passwordInput = Entry(self._root, width=50)
        self._passwordInput.pack(pady=(5, 10), ipady=10, ipadx=30)



        # Reset Password Button
        self._login = Button(self._root,text="Reset Password",bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.reset_password(self._emailInput.get(), self._acc_no_Input.get(), self._passwordInput.get()))
        self._login.pack(pady=(90, 10))

        self.current_date_time()


    def reset_password(self, emailInput, acc_no_Input, passwordInput):

        data = self.db.reset_password(emailInput, acc_no_Input, passwordInput)
        
        if data == 1:
            messagebox.showinfo("Success", "Your password was successfully changed. Now login and enjoy!!!")
            self.login_handler()

        elif data == 0:
            messagebox.showerror("Error", "Your email or account number was not matched. Try again!!!")
            self.reset_password_page()

        elif data == 2:
            messagebox.showerror("Error", "Some error occured!! Try again")
            self.reset_password_page()

        else:
            messagebox.showerror("Error", "Some error occured!! Try again")
            self.reset_password_page()
            

    def regWindow1(self):
        
        self.clear()

        # name label
        self._name = Label(self._root, text="Name", foreground="#E9E612", background="#630db8")
        self._name.config(font=(16))
        self._name.pack(pady=(20,5))

        # Name input
        self._nameInput = Entry(self._root, width=50)
        self._nameInput.pack(pady=(5,10), ipady=10, ipadx=30)



        # email label
        self._email = Label(self._root, text="Email", foreground="#E9E612", background="#630db8")
        self._email.config(font=(16))
        self._email.pack(pady=(10,5))

        # email input
        self._emailInput = Entry(self._root, width=50)
        self._emailInput.pack(pady=(5,10), ipady=10, ipadx=30)

        # password label
        self._password = Label(self._root, text="Password", foreground="#E9E612", background="#630db8")
        self._password.config(font=(16))
        self._password.pack(pady=(10, 5))

        # password input
        self._passwordInput = Entry(self._root, width=50)
        self._passwordInput.pack(pady=(5, 10), ipady=10, ipadx=30)

        # age label
        self._age = Label(self._root, text="age", foreground="#E9E612", background="#630db8")
        self._age.config(font=(16))
        self._age.pack(pady=(10, 5))

        # age input
        self._ageInput = Entry(self._root, width=50)
        self._ageInput.pack(pady=(5, 10), ipady=10, ipadx=30)

        # address label
        self._address = Label(self._root, text="address", foreground="#E9E612", background="#630db8")
        self._address.config(font=(16))
        self._address.pack(pady=(10, 5))

        # address input
        self._addressInput = Entry(self._root, width=50)
        self._addressInput.pack(pady=(5, 10), ipady=10, ipadx=30)

        self._next1_button = Button(self._root, text="Next", bg='#556ce9',fg='white', width=20, height = "1", font= 20, command=lambda: self.regWindow2(self._nameInput.get(), self._emailInput.get(), self._passwordInput.get(), self._ageInput.get(), self._addressInput.get()))
        self._next1_button.pack(pady=(10,10))

        self.current_date_time()


    def regWindow2(self, nameInput, emailInput, passwordInput, ageInput, addressInput):
        
        self.clear()

        # Bank name label
        self._bank_name = Label(self._root, text="Bank Name:", foreground="#E9E612", background="#630db8")
        self._bank_name.config(font=(16))
        self._bank_name.pack(pady=(20,5))

        # Bank name input
        self._bank_nameInput = Entry(self._root, width=50)
        self._bank_nameInput.pack(pady=(5,10), ipady=10, ipadx=30)


        # acc_no_ label
        self._acc_no_ = Label(self._root, text="Account No.(5 - digit):", foreground="#E9E612", background="#630db8")
        self._acc_no_.config(font=(16))
        self._acc_no_.pack(pady=(20,5))

        

        # acc_no input
        self._acc_no_Input = Entry(self._root, width=50)
        self._acc_no_Input.pack(pady=(5,10), ipady=10, ipadx=30)

        # Bank pin label
        self._bank_pin = Label(self._root, text="Pin(4 - digit)", foreground="#E9E612", background="#630db8")
        self._bank_pin.config(font=(16))
        self._bank_pin.pack(pady=(20,5))

        # Bank pin input
        self._bank_pin_Input = Entry(self._root, width=50)
        self._bank_pin_Input.pack(pady=(5,10), ipady=10, ipadx=30)

        # Bank balance label
        self._bank_balance = Label(self._root, text="Bank balance(minimum balance Rs. 3000):", foreground="#E9E612", background="#630db8")
        self._bank_balance.config(font=(16))
        self._bank_balance.pack(pady=(20,5))

        # Bank balance input
        self._bank_balanceInput = Entry(self._root, width=50)
        self._bank_balanceInput.pack(pady=(5,10), ipady=10, ipadx=30)

        self._register_button = Button(self._root, text="Register", bg='#556ce9',fg='white', width=20, height = "1", font= 20, command=lambda: self.register(nameInput, emailInput, passwordInput, ageInput, addressInput, self._bank_nameInput.get(), self._acc_no_Input.get(), self._bank_pin_Input.get(), self._bank_balanceInput.get()))
        self._register_button.pack(pady=(10,10))

        self.current_date_time()


    def register(self, nameInput, emailInput, passwordInput, ageInput, addressInput, bank_nameInput, acc_no_Input, bank_pin_Input, bank_balanceInput):

        if int(acc_no_Input) >= 10000 and int(acc_no_Input) <= 99999 and int(bank_pin_Input) >= 1000 and int(bank_pin_Input) <= 9999 and int(bank_balanceInput) >= 3000:

            data = self.db.register(nameInput, emailInput, passwordInput, ageInput, addressInput, bank_nameInput, acc_no_Input, bank_pin_Input, bank_balanceInput)

            if data == 1:
                messagebox.showinfo("Successful", "Successful! You was registered. Enjoy!!")

                data = self.db.check_login(nameInput, emailInput,  passwordInput)
                user_id = data[0][0]

                self.mainWindow(user_id, nameInput, emailInput)

            elif data == 0:
                messagebox.showerror("Error", "You was not registered successfully!! Try again.")
                self.regWindow1()

            elif data == 2:
                messagebox.showerror("Error", "Account number already exits!!! Login Now")
                self.login_handler()

            else:
                messagebox.showerror("Error", "Some error occured. Try again")
                self.regWindow1()

        else:
            messagebox.showerror("Error", "Your account number or pin number or minimum balance can not full-fill the conditions. Try again")
            self.regWindow1()


            



    def login_handler(self):

        self.clear()
        

        # name label
        self._name = Label(self._root, text="Name", foreground="#E9E612", background="#630db8")
        self._name.config(font=(16))
        self._name.pack(pady=(100,10))

        # Name input
        self._nameInput = Entry(self._root, width=50)
        self._nameInput.pack(pady=(5,25), ipady=10, ipadx=30)



        # email label
        self._email = Label(self._root, text="Email", foreground="#E9E612", background="#630db8")
        self._email.config(font=(16))
        self._email.pack(pady=(10,10))

        # email input
        self._emailInput = Entry(self._root, width=50)
        self._emailInput.pack(pady=(5,25), ipady=10, ipadx=30)

        # password label
        self._password = Label(self._root, text="Password", foreground="#E9E612", background="#630db8")
        self._password.config(font=(16))
        self._password.pack(pady=(10, 10))

        # password input
        self._passwordInput = Entry(self._root, width=50)
        self._passwordInput.pack(pady=(5, 25), ipady=10, ipadx=30)

        # Creating the button for Login
        self._login = Button(self._root, text="Login", bg='#556ce9',fg='white', width=20, height = "1", font= 20, command=lambda:self.check_login())
        self._login.pack(pady=(30, 10))

        self.current_date_time()
        

    def check_login(self):

        name = self._nameInput.get()
        email = self._emailInput.get()
        password = self._passwordInput.get()

        data = self.db.check_login(name, email, password)

        if len(data)== 0:

            messagebox.showerror("Error", "User Not Found!")
            self._root.destroy()
            self.load_login_window()
            

        else:
            self._user_id = data[0][0]
            self._name1 = data[0][1]
            self._email1 = data[0][2]
            self._age1 = data[0][4]
            self._address1 = data[0][5]
            self._acc_no1 = data[0][7]

            self.mainWindow(self._user_id, self._name1, self._email1)
            
            

    def mainWindow(self, user_id, name, email):

        self.clear()

        self.headerMenu()

        self._nameLabel = Label(self._root, text="Name:", fg="#E9E612", bg="#630db8")
        self._nameLabel.config(font=10)
        self._nameLabel.pack(pady=(20,10))

        self._name = Label(self._root, text=name, fg="white", bg="#630db8",font=10)
        self._name.pack()


        self._emailLabel = Label(self._root, text="Email:", fg="#E9E612", bg="#630db8", font=50)
        self._emailLabel.pack(pady=(20,10))

        self._email = Label(self._root, text=email, fg="white", bg="#630db8", font=20)
        self._email.pack()

        self._balance_button = Button(self._root, text="Balance", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.check_balance(user_id, name, email))
        self._balance_button.pack(pady=(80, 3))

        self._credit_button = Button(self._root, text="Credit", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command = lambda: self.credit_money(user_id, name, email))
        self._credit_button.pack(pady=(3,3))

        self._debit_button = Button(self._root, text="Debit / UPI Pay", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command = lambda: self.debit_money(user_id, name, email))
        self._debit_button.pack(pady=(3,3))

        self.current_date_time()


    def debit_money(self, user_id, name, email):

        self.clear()
        self.headerMenu()

        self._nameLabel = Label(self._root, text="Name:", fg="#E9E612", bg="#630db8")
        self._nameLabel.config(font=10)
        self._nameLabel.pack(pady=(20,10))

        self._name = Label(self._root, text=name, fg="white", bg="#630db8",font=10)
        self._name.pack()


        self._emailLabel = Label(self._root, text="Email:", fg="#E9E612", bg="#630db8", font=50)
        self._emailLabel.pack(pady=(20,10))

        self._email = Label(self._root, text=email, fg="white", bg="#630db8", font=20)
        self._email.pack()


        self._horizontal_line = Label(self._root, text="--------------------------------------------------------------------------------------------------------------------",fg="white", bg="#630db8")
        self._horizontal_line.pack(pady=(30, 30))

        self._upi_button = Button(self._root, text = "UPI Pay", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda:self.upi_pay_input(user_id, name, email))
        self._upi_button.pack(pady=(100, 5))


        self._debit_button = Button(self._root, text = "Debit", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.debit_pay_input(user_id, name, email))
        self._debit_button.pack(pady=(30, 5))


        self.current_date_time()



    def debit_pay_input(self, user_id, name, email):

        self.clear()
        self.headerMenu()

        self._debit_debit_amount = Label(self._root, text="Enter amount:", fg="#E9E612", bg="#630db8", font=(35))
        self._debit_debit_amount.pack(pady=(40, 10))

        self._debit_debit_amount_Input = Entry(self._root, width=50)
        self._debit_debit_amount_Input.pack(pady=(5,25), ipady=10, ipadx=30)


        self._debit_debit_amount_pin = Label(self._root, text="Enter 4 digit pin:", fg="#E9E612", bg="#630db8", font=(35))
        self._debit_debit_amount_pin.pack(pady=(30, 10))

        self._debit_debit_amount_pin_Input = Entry(self._root, width=50)
        self._debit_debit_amount_pin_Input.pack(pady=(5,25), ipady=10, ipadx=30)

        self._debit_debit_button = Button(self._root, text = "Debit",bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.check_debit(user_id, name, email,self._debit_debit_amount_Input.get(),self._debit_debit_amount_pin_Input.get()))
        self._debit_debit_button.pack(pady=(80, 20))


        self.current_date_time()


    def check_debit(self, user_id, name, email, debit_debit_amount_Input,debit_debit_amount_pin_Input):
        
        data = self.db.debit_money(user_id, debit_debit_amount_Input, debit_debit_amount_pin_Input)

        if data == 1:
            messagebox.showinfo("Success", "Your transaction was successful")
            self.mainWindow(user_id, name, email)
            

        elif data == 2:
            messagebox.showerror("Error", "Pin did not matched. Try Again")

        elif data == 0:
            messagebox.showerror("Error", "Did not debited. Try again")
        else:

            messagebox.showerror("Error", "Some error occured")



    def upi_pay_input(self, user_id, name, email):

        self.clear()
        self.headerMenu()

        self._debit_upi_amount = Label(self._root, text="Enter amount:", fg="#E9E612", bg="#630db8", font=(35))
        self._debit_upi_amount.pack(pady=(40, 10))

        self._debit_upi_amount_Input = Entry(self._root, width=50)
        self._debit_upi_amount_Input.pack(pady=(5,25), ipady=10, ipadx=30)


        self._debit_upi_amount_pin = Label(self._root, text="Enter 4 digit pin:", fg="#E9E612", bg="#630db8", font=(35))
        self._debit_upi_amount_pin.pack(pady=(30, 10))

        self._debit_upi_amount_pin_Input = Entry(self._root, width=50)
        self._debit_upi_amount_pin_Input.pack(pady=(5,25), ipady=10, ipadx=30)

        self._debit_upi_button = Button(self._root, text = "GET UPI CODE",bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda:self.qrCode(user_id, name, email, self._debit_upi_amount_Input.get(), self._debit_upi_amount_pin_Input.get()))
        self._debit_upi_button.pack(pady=(80, 20))

        self.current_date_time()




    def qrCode(self, user_id, name, email, debit_upi_amount_Input, debit_upi_amount_pin_Input):

        data = self.db.debit_money(user_id, debit_upi_amount_Input, debit_upi_amount_pin_Input)

        if data == 1:

            self.clear()
            self.headerMenu()
            
            QR = Label(self._root, image="", bg='#556ce9')
            QR.pack(pady=(30,20))

            data = [debit_upi_amount_Input, self.d1, self._email1, self._acc_no1]
            

            fileName = str(user_id) + str(debit_upi_amount_Input) + '.jpg'

            img = qrcode.make(data)
            img.save(fileName)
            self._root.photo = PhotoImage(file = fileName)
            QR.config(image=self._root.photo, text="QR Code Generating Successfully!", fg="white", compound=TOP, width=350, height=450, font=(20))

            self._go_home_button = Button(self._root, text="Go main page", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.mainWindow(user_id, name, email))
            self._go_home_button.pack(pady=(15, 10))

            self.current_date_time()

        elif data == 2:
            messagebox.showerror("Error", "Pin did not matched. Try Again")

        elif data == 0:
            messagebox.showerror("Error", "Did not debited. Try again")
        else:

            messagebox.showerror("Error", "Some error occured")

        

    

    def credit_money(self, user_id, name, email):

        self.clear()

        self.headerMenu()

        self._credit_label = Label(self._root, text="Credit", fg="#E9E612", bg="#630db8", font=("50"))
        self._credit_label.pack(pady=(20, 10))


        self._credit_amount = Label(self._root, text="Enter amount:", fg="#E9E612", bg="#630db8", font=(35))
        self._credit_amount.pack(pady=(40, 10))

        self._credit_amount_Input = Entry(self._root, width=50)
        self._credit_amount_Input.pack(pady=(5,25), ipady=10, ipadx=30)


        self._credit_amount_pin = Label(self._root, text="Enter 4 digit pin:", fg="#E9E612", bg="#630db8", font=(35))
        self._credit_amount_pin.pack(pady=(30, 10))

        self._credit_amount_pin_Input = Entry(self._root, width=50)
        self._credit_amount_pin_Input.pack(pady=(5,25), ipady=10, ipadx=30)

        self._credit_button = Button(self._root, text="Credit", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.check_credit(user_id,name, email,self._credit_amount_Input.get(), self._credit_amount_pin_Input.get() ))
        self._credit_button.pack(pady=(50,3))


        self.current_date_time()

        


    def check_credit(self, user_id,name, email,credit_amount_Input, credit_amount_pin_Input):

        
        data = self.db.check_credit(user_id,credit_amount_Input,credit_amount_pin_Input)

        if data == 1:
            messagebox.showinfo("Success", "Your transaction was successful")
        
        elif data == 0:

            messagebox.showerror("Error", "Your transaction was failed!! Try again.")

        elif data == 2:

            messagebox.showerror("Error", "Pin not matched")

        else:

            messagebox.showerror("Error", "Some error occured")

        self.mainWindow(user_id, name, email)

        

    def check_balance(self, user_id, name, email):

        self.clear()

        self._data = self.db.fetch_user(user_id)

        self._balance = self._data[0][9]

        self._nameLabel = Label(self._root, text="Name:", fg="#E9E612", bg="#630db8")
        self._nameLabel.config(font=10)
        self._nameLabel.pack(pady=(20,10))

        self._name = Label(self._root, text=name, fg="white", bg="#630db8",font=10)
        self._name.pack()


        self._emailLabel = Label(self._root, text="Email:", fg="#E9E612", bg="#630db8", font=50)
        self._emailLabel.pack(pady=(20,10))

        self._email = Label(self._root, text=email, fg="white", bg="#630db8", font=20)
        self._email.pack()

        self._horizontal_line = Label(self._root, text="--------------------------------------------------------------------------------------------------------------------",fg="white", bg="#630db8")
        self._horizontal_line.pack(pady=(30, 30))


        self._check_balance = Label(self._root, text="Balance:", fg="#E9E612", bg="#630db8", font=50)
        self._check_balance.pack(pady=(20,10))

        self._balance = Label(self._root, text=self._balance, fg="white", bg="#630db8", font=20)
        self._balance.pack()



        self._credit_button = Button(self._root, text="Credit", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command = lambda: self.credit_money(user_id, name, email))
        self._credit_button.pack(pady=(50,3))

        self._debit_button = Button(self._root, text="Debit", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command = lambda: self.debit_money(user_id, name, email))
        self._debit_button.pack(pady=(3,3))

        self.current_date_time()


        





    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()




    def headerMenu(self):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Profile", menu=filemenu)
        filemenu.add_command(label="Home", command=lambda: self.menu_home())
        filemenu.add_command(label="Edit", command=lambda: self.menu_edit())
        filemenu.add_command(label="Change Password", command=lambda: self.reset_password_page())
        

        helpmenu = Menu(menu)
        menu.add_cascade(label="Banking", menu=helpmenu)
        helpmenu.add_command(label="Balance", command=lambda: self.menu_balance())
        helpmenu.add_command(label="Credit", command=lambda: self.menu_credit())
        helpmenu.add_command(label="Debit", command=lambda: self.menu_debit())
        helpmenu.add_command(label="Change PIN", command=lambda: self.menu_pin_change())

    def menu_pin_change(self):

        self.clear()

        self._age = Label(self._root, text="Change PIN", foreground="#E9E612", background="#630db8")
        self._age.config(font=(16))
        self._age.pack(pady=(15, 5))

        # acc_no label
        self._acc_no = Label(self._root, text="Account No.", foreground="#E9E612", background="#630db8")
        self._acc_no.config(font=(16))
        self._acc_no.pack(pady=(30, 5))

        # acc_no input
        self._acc_no_Input = Entry(self._root, width=50)
        self._acc_no_Input.pack(pady=(5, 10), ipady=10, ipadx=30)

        # password label
        self._password = Label(self._root, text="Password:", foreground="#E9E612", background="#630db8")
        self._password.config(font=(16))
        self._password.pack(pady=(30, 5))

        # password input
        self._password_Input = Entry(self._root, width=50)
        self._password_Input.pack(pady=(5, 10), ipady=10, ipadx=30)

        # pin label
        self._pin = Label(self._root, text="pin(new):", foreground="#E9E612", background="#630db8")
        self._pin.config(font=(16))
        self._pin.pack(pady=(30, 5))

        # pin input
        self._pin_Input = Entry(self._root, width=50)
        self._pin_Input.pack(pady=(5, 10), ipady=10, ipadx=30)



        self._pin_button = Button(self._root, text="Edit", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.edit_pin(self._acc_no_Input.get(), self._password_Input.get(), self._pin_Input.get()))
        self._pin_button.pack(pady=(30, 20))

        self.current_date_time()


    def edit_pin(self, acc_no_Input, password_Input, pin_Input):

        user_id = self._user_id
        name = self._name1
        email = self._email1

        data = self.db.edit_pin( acc_no_Input, password_Input, pin_Input)

        if data == 0:
            messagebox.showerror("Error", "Pin must have only 4 digits. Try again")
            self.menu_pin_change()

        elif data == 1:
            messagebox.showinfo("Success", "Your new pin was created. Enjoy now!!!")
            self.mainWindow(user_id, name, email)

        elif data == 2:
            messagebox.showerror("Error", "Some error occured. Try again")
            self.menu_pin_change()

        elif data == 3:
            messagebox.showerror("Error", "Some error occured. Try again")
            self.menu_pin_change()

        else:
            messagebox.showerror("Error", "Some error occured. Try again")
            self.menu_pin_change()




    def menu_edit(self):

        self.clear()

        self._age = Label(self._root, text="You can only edit your age & address", foreground="#E9E612", background="#630db8")
        self._age.config(font=(16))
        self._age.pack(pady=(15, 5))

        # age label
        self._age = Label(self._root, text="age", foreground="#E9E612", background="#630db8")
        self._age.config(font=(16))
        self._age.pack(pady=(70, 5))

        # age input
        self._ageInput = Entry(self._root, width=50)
        self._ageInput.pack(pady=(5, 10), ipady=10, ipadx=30)

        # address label
        self._address = Label(self._root, text="address", foreground="#E9E612", background="#630db8")
        self._address.config(font=(16))
        self._address.pack(pady=(70, 5))

        # address input
        self._addressInput = Entry(self._root, width=50)
        self._addressInput.pack(pady=(5, 10), ipady=10, ipadx=30)


        self._edit_button = Button(self._root, text="Edit", bg='#556ce9',fg='white', width=20, height ="1", font= 20, command=lambda: self.edit_profile(self._ageInput.get(), self._addressInput.get()))
        self._edit_button.pack(pady=(50, 20))

        self.current_date_time()




    def edit_profile(self, ageInput, addressInput):

        user_id = self._user_id
        name = self._name1
        email = self._email1
        age = ageInput
        address = addressInput

        data = self.db.edit_profile(user_id, email, age, address)

        if data == 1:
            messagebox.showinfo("Successful", "Your profile are edited successfully")
            self.mainWindow(user_id, name, email)

        elif data == 0:
            messagebox.showerror("Error", "Some error occured. Try again")
            self.menu_edit()

        elif data == 2:
            messagebox.showerror("Error", "Some error occured. Try again")
            self.menu_edit()

        else:
            messagebox.showerror("Error", "Some error occured. Try again")
            self.menu_edit()
        




    def menu_home(self):

        user_id = self._user_id
        name = self._name1
        email = self._email1

        self.mainWindow(user_id, name, email)


    def menu_debit(self):

        user_id = self._user_id
        name = self._name1
        email = self._email1

        self.debit_money(user_id, name, email)


    def menu_credit(self):

        user_id = self._user_id
        name = self._name1
        email = self._email1

        self.credit_money(user_id, name, email)



    def menu_balance(self):

        user_id = self._user_id
        name = self._name1
        email = self._email1

        self.check_balance(user_id, name, email)

    def current_date_time(self):

        today = date.today()

        self.d1 = today.strftime("%d/%m/%Y")

        self._current_date_time_label = Label(self._root, text=f"Date = {self.d1}", foreground="#E9E612", background="#630db8")
        self._current_date_time_label.pack(side = BOTTOM)




obj = Bank()