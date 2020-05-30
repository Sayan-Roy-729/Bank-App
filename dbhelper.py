import mysql.connector


class DBHelper:

    def __init__(self):
        #connect to database

        try:
            self._conn = mysql.connector.connect(host="127.0.0.1", user="root", password="", database="BankApp")
            self._mycursor = self._conn.cursor()
        except:
            print("Can't connect to Database")
            exit()


    def fetch_user(self, user_id):

        self._mycursor.execute(f"SELECT * FROM users WHERE user_id LIKE {user_id}")
        data = self._mycursor.fetchall()

        return data
    


    def check_login(self, name, email, password):

        # perform login
        self._mycursor.execute(f"SELECT * FROM users WHERE name LIKE '{name}' AND email LIKE '{email}' AND password LIKE '{password}' ")
        data = self._mycursor.fetchall()

        return data


    def check_credit(self, user_id, credit_amount_Input, credit_amount_pin_Input):

        try:
            self._data = self.fetch_user(user_id)
            self._pin = self._data[0][8]
            self._balance = self._data[0][9]

            if self._pin == int(credit_amount_pin_Input):

                total_balance = int(self._balance) + int(credit_amount_Input)
                self._mycursor.execute(f"UPDATE `users` SET `balance` = '{total_balance}' WHERE `users`.`user_id` = {user_id}")
                self._conn.commit()

                return 1
            else:
                return 2
            
        except:
            return 0
            


    def debit_money(self, user_id, debit_upi_amount_Input, debit_upi_amount_pin_Input):

        try:
            self._data = self.fetch_user(user_id)
            self._pin = self._data[0][8]
            self._balance = self._data[0][9]

            if self._pin == int(debit_upi_amount_pin_Input):

                total_balance = int(self._balance) - int(debit_upi_amount_Input)
                self._mycursor.execute(f"UPDATE `users` SET `balance` = '{total_balance}' WHERE `users`.`user_id` = {user_id}")
                self._conn.commit()

                return 1
            else:
                return 2
            
        except:
            return 0


    def register(self, nameInput, emailInput, passwordInput, ageInput, addressInput, bank_nameInput, acc_no_Input, bank_pin_Input, bank_balanceInput):

        ageInput = int(ageInput)
        acc_no_Input = int(acc_no_Input)
        bank_pin_Input = int(bank_pin_Input)
        bank_balanceInput = int(bank_balanceInput)

        try:
            self._mycursor.execute(f"SELECT * FROM users WHERE acc_no LIKE {acc_no_Input}")
            data = self._mycursor.fetchall()

            if len(data) == 0:

                self._mycursor.execute(f"INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `age`, `address`, `bank_name`, `acc_no`, `pin`, `balance`) VALUES (NULL, '{nameInput}', '{emailInput}', '{passwordInput}', '{ageInput}', '{addressInput}', '{bank_nameInput}', '{acc_no_Input}', '{bank_pin_Input}', '{bank_balanceInput}')")

                self._conn.commit()

                return 1
            else:
                return 2
        
        except:
            return 0


    def reset_password(self, emailInput, acc_no_Input, passwordInput):

        acc_no_Input = int(acc_no_Input)

        try:

            self._mycursor.execute(f'SELECT * FROM users WHERE `acc_no` LIKE "{acc_no_Input}" AND `email` LIKE "{emailInput}"')
            data = self._mycursor.fetchall()
            
            if len(data) == 1:
                self._mycursor.execute(f"UPDATE `users` SET `password` = '{passwordInput}' WHERE `users`.`email` = '{emailInput}'")
                self._conn.commit()

                return 1
            else:
                return 0
            
        except:
            return 2
            

    def edit_profile(self, user_id, email, age, address):

        age = int(age)

        try:
            self._mycursor.execute(f'SELECT * FROM `users` WHERE `user_id` LIKE "{user_id}" AND `email` LIKE "{email}"')
            data = self._mycursor.fetchall()
            

            if len(data) == 1:
                self._mycursor.execute(f"UPDATE users SET age = '{age}', address = '{address}' WHERE email = '{email}'")
                self._conn.commit()

                return 1

            else:
                return 0
        except:
            # return 2
            print("Error")

    def edit_pin(self, acc_no_Input, password_Input, pin_Input):

        acc_no_Input = int(acc_no_Input)
        pin_Input = int(pin_Input)

        try:

            if pin_Input < 1000 and pin_Input > 9999:
                return 0

            else:
                self._mycursor.execute(f'SELECT * FROM `users` WHERE `acc_no` LIKE "{acc_no_Input}" AND `password` LIKE "{password_Input}"')
                data = self._mycursor.fetchall()

                if len(data) == 1:
                    self._mycursor.execute(f"UPDATE users SET pin = '{pin_Input}' WHERE `acc_no` LIKE '{acc_no_Input}'")
                    self._conn.commit()

                    return 1

                else:

                    return 2
                

        except:

            return 3




# obj = DBHelper()

# obj.check_credit(user_id = 1, credit_amount_Input = 500, credit_amount_pin_Input=1234)