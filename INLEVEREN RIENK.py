import mysql.connector
import smtplib
from tkinter import *

#TODO we can still do a lot better
#
# _____________________________________________________________________________________________
# makes connection, exception for connection fail and grabs and sets variable for the data
try:
    soda_machine_db_connection = mysql.connector.connect(
                              host='84.85.94.66',
                              port=3306,
                              user='root',
                              password='MySQLPassword',
                              database='smart_soda_machine',) # frisdrank_automaat

    if soda_machine_db_connection.is_connected():
        sodamachine_db_info = soda_machine_db_connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", sodamachine_db_info, "\n")

except NameError:
    print("Error while connecting to MySQL")


cursor = soda_machine_db_connection.cursor()
select_data_from_table = "SELECT * FROM  soda_stock"
cursor.execute(select_data_from_table)  # frisdrank_voorraad
print(select_data_from_table, "has been executed")


all_sodas_string = "Fanta, Water, Cola, Sprite, Ice-Tea, Dr.Pepper, Pepsi, Fernandes"

# ____________________________________________________________________________________________
# copies all content from database, adds soda names to the top and prints if it has succeeded
with open("sodamachine_db_text.txt", "w") as textfileoutput:
    textfileoutput.write(all_sodas_string)
    for lastrow_in_all_data in cursor:
        data_in_listformat = list(lastrow_in_all_data)
        data_in_stringformat = str(data_in_listformat)
        data_in_stringformat.replace("[", "").replace("]", "")
        textfileoutput.write("\n" + data_in_stringformat)
print("The file's contents have been copied", "\n")

# __________________________________________
# Return name of soda function for each soda

# Variables
with open("sodamachine_db_text.txt", "r") as textfileoutput_read:  # TODO: LOOK AT THIS!! Can simplify words & lines
    for data in textfileoutput_read:
        lines_raw = textfileoutput_read.read().splitlines()
        last_line = [int(characters) for characters in lines_raw[-1].replace("[", "").replace("]", "").split(",")]
        words = lines_raw[0].split(", ")  # TODO: LOOK AT

#  Soda Names

def soda_name_fanta():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split(", ")
        name_fanta = words[0]
        return name_fanta


def soda_name_water():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split(", ")
        name_water = words[1]
        return name_water


def soda_name_cola():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split(", ")
        name_cola = words[2]
        return name_cola


def soda_name_sprite():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split(", ")
        name_sprite = words[3]
        return name_sprite


def soda_name_icetea():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split(", ")
        name_icetea = words[4]
        return name_icetea


def soda_name_drpepper():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split(", ")
        name_drpepper = words[5]
        return name_drpepper


def soda_name_pepsi():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split(", ")
        name_pepsi = words[6]
        return name_pepsi


def soda_name_fernandes():
    with open('sodamachine_db_text.txt', 'r') as textfileoutput:
        words = textfileoutput.read().split()
        name_fernandes = words[7]
        return name_fernandes


# __________________________________________
# Return stock amount function for each soda

last_fanta_stock = lastrow_in_all_data[0]

last_water_stock = lastrow_in_all_data[1]

last_cola_stock = lastrow_in_all_data[2]

last_sprite_stock = lastrow_in_all_data[3]

last_icetea_stock = lastrow_in_all_data[4]

last_drpepper_stock = lastrow_in_all_data[5]

last_pepsi_stock = last_line[6]

last_fernandes_stock = last_line[7]


# ________________________________
# ........NOTIFICATIONS...........

stock_is_low = False


def restock_notifications():
    global stock_is_low
    if last_fanta_stock <= 4:
        stock_is_low = True
        return "Fanta"
    if last_water_stock <= 4:
        stock_is_low = True
        return "Water"
    if last_cola_stock <= 4:
        stock_is_low = True
        return "Cola"
    if last_sprite_stock <= 4:
        stock_is_low = True
        return "Sprite"
    if last_icetea_stock <= 4:
        stock_is_low = True
        return"Ice-Tea"
    if last_drpepper_stock <= 4:
        stock_is_low = True
        return "Dr.Pepper"
    if last_pepsi_stock <= 4:
        stock_is_low = True
        return "Pepsi"
    if last_fernandes_stock <= 4:
        stock_is_low = True
        return "Fernandes"
    if stock_is_low == True:
        return restock_notifications()


def send_email_notification():
    sender_email = "smartsodamachine@gmail.com"
    receiver_email = "smartsodamachine.manager@gmail.com"
    password_sender_email = "SmartSodaMachineEmail"

    email_subject = "LOW STOCK NOTIFICATION"
    email_message = "The following soda's are low on stock (less than 4 cans):"

    full_message = f'Subject: {email_subject}\n\n{email_message}\n {restock_notifications()}'

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(sender_email, password_sender_email)
    print("Logged into smartsodamachine@gmail.com succesfully!")
    server.sendmail(sender_email, receiver_email, full_message)
    print("Email has been sent to smartsodamachine.manager@gmail.com succesfully!")


# _______________
# Call functions:

# restock_notification = email.get()  #TODO: EMAIL NOTIFCAITON TOGGLE

restock_notifications()
notifications = "ON"
if notifications == "ON":
    if stock_is_low == True:
        send_email_notification()


fanta_manual_restockbutton = True


input_manual_restockamount = int() #  INVUL VAKJE ACHRAF


# _____________________________________________________________________________________________
# ........................................GUI..................................................

# makes connection, exception for connection fail and grabs and sets variable for the data

main_screen = Tk()
main_screen.title('Main menu')
main_screen.geometry('300x479')
sodamachine_image = PhotoImage(file="SodaMachineFINAL.png")
photolabel = Label(main_screen, image=sodamachine_image)
photolabel.place(x=0, y=0)

small_font = "segoe ui semibold", "10"
close_windows_button = Button(master=main_screen, text='Close window(s)', font=small_font, command=main_screen.destroy)
close_windows_button.place(x=185, y=443)
menu_button = Menubutton(main_screen, text='Menu', bg="red", fg="white", font=("segoe ui bold", "15"))
menu_button.menu = Menu(menu_button)
menu_button.place(x=3, y=3)
menu_button['menu'] = menu_button.menu


def database_connection():

    # _____________________________________________________________________________________________
    # makes connection, exception for connection fail and grabs and sets variable for the data
    try:
        soda_machine_db_connection = mysql.connector.connect(
            host='84.85.94.66',
            port=3306,
            user='root',
            password='MySQLPassword',
            database='smart_soda_machine', )

        if soda_machine_db_connection.is_connected():
            top = Toplevel()
            my_connection_label = Label(master=top, text="Connected to MySQL database... MySQL Server version on " )
            my_connection_label.pack(pady=10, padx=10)

    except NameError:
        top = Toplevel()
        my_connection_label = Label(master=top, text="Error while connecting to MySQL ")
        my_connection_label.pack(pady=10, padx=10)



def get_temperature():
    cursor2 = soda_machine_db_connection.cursor()
    select_data_from_table2 = "SELECT * FROM  dev_temp"
    cursor2.execute(select_data_from_table2)  # frisdrank_voorraad
    print(select_data_from_table2, "has been executed")

    with open("dev_temp_table.txt", "w+") as textfileoutput2:
        for row_in_all_data in cursor2:
            data_in_listformat2 = list(row_in_all_data)
            data_in_stringformat2 = str(data_in_listformat2)
            neededtemp = (data_in_listformat2[1])
            textfileoutput2.write("\n" + data_in_stringformat2)

        return neededtemp
    print("The file's contents have been copied", "\n")




#TODO: Niet goed genoeg!!!!!
def open_logs():
    top = Toplevel()
    top.geometry('350x350')
    text_block = Text(master=top, width=20, height=12)
    text_block.place(x=150, y=100)
    text_block.insert(END, "Temp = " + get_temperature())
    temp_button = Button(master=top, text='Get temperature', command=get_temperature)
    temp_button.place(x=20, y=150)
    status_button = Button(master=top, text='Machine status')
    status_button.place(x=20, y=190)
    top.title('Logs')



def var_checked():
    global output_of_restockbutton
    output_of_restockbutton = [fanta_checked.get(), water_checked.get(), coca_cola_checked.get(),
                               sprite_checked.get(),ice_tea_checked.get(), drpepper_checked.get(),
                               pepsi_checked.get(), fernandes_checked.get()]
    return output_of_restockbutton


def open_restock():
    global fanta_checked
    fanta_checked = IntVar()
    global water_checked
    water_checked = IntVar()
    global coca_cola_checked
    coca_cola_checked = IntVar()
    global sprite_checked
    sprite_checked = IntVar()
    global drpepper_checked
    drpepper_checked = IntVar()
    global ice_tea_checked
    ice_tea_checked = IntVar()
    global pepsi_checked
    pepsi_checked = IntVar()
    global fernandes_checked
    fernandes_checked = IntVar()

    top = Toplevel()

    fanta_check_button = Checkbutton(master=top, text='Fanta', variable=fanta_checked)
    fanta_check_button.pack(pady=10, padx=10)

    cola_check_button = Checkbutton(master=top, text='Water', variable=water_checked)
    cola_check_button.pack(pady=10, padx=10)

    drpepper_check_button = Checkbutton(master=top, text='Coca Cola', variable=coca_cola_checked)
    drpepper_check_button.pack(pady=10, padx=10)

    water_check_button = Checkbutton(master=top, text='Sprite', variable=sprite_checked)
    water_check_button.pack(pady=10, padx=10)

    sprite_check_button = Checkbutton(master=top, text='Ice Tea', variable=ice_tea_checked)
    sprite_check_button.pack(pady=10, padx=10)

    drpepper_check_button = Checkbutton(master=top, text='Dr.Pepper', variable=drpepper_checked)
    drpepper_check_button.pack(pady=10, padx=10)

    pepsi_check_button = Checkbutton(master=top, text='Pepsi', variable=pepsi_checked)
    pepsi_check_button.pack(pady=10, padx=10)

    fernandes_check_button = Checkbutton(master=top, text='Fernandes', variable=fernandes_checked)
    fernandes_check_button.pack(pady=10, padx=10)

    amount_restocked_label = Label(master=top, text='When you press the button, every checked \n'
                                                    'drink will be restocked to full capacity')
    amount_restocked_label.pack(pady=10, padx=10)
    amount_restock_confirm = Button(master=top, text='Confirm restock', command=restockbutton_pressed)
    amount_restock_confirm.pack(pady=10, padx=10)
    amount_restock_email = Checkbutton(master=top, text='Receive E-Mail notifications.')
    amount_restock_email.pack(pady=10, padx=10)
    button = Button(master=top, text='Check database connection', command=database_connection)
    button.pack(pady=20, padx=20)
    top.title('Restock')


def restockbutton_pressed():
    var_checked()
    global value_of_restockbutton_pressed
    value_of_restockbutton_pressed = 1

    if value_of_restockbutton_pressed == 1:  # KNOP OM TE RESTOCKEN
        newrow_in_table = []

        if output_of_restockbutton[0] == 1:  # VINKJE VAN FANTA
            add_to_fantastock = last_fanta_stock + (20-last_fanta_stock) # OR 5
            newrow_in_table.append(add_to_fantastock)
        else:
            newrow_in_table.append(last_fanta_stock)

        if output_of_restockbutton[1] == 1:  # VINKJE VAN WATER
            add_to_waterstock = last_water_stock + (20-last_water_stock)
            newrow_in_table.append(add_to_waterstock)
        else:
            newrow_in_table.append(last_water_stock)

        if output_of_restockbutton[2] == 1:  # VINKJE VAN COLA
            add_to_colastock = last_cola_stock + (20-last_cola_stock)
            newrow_in_table.append(add_to_colastock)
        else:
            newrow_in_table.append(last_cola_stock)

        if output_of_restockbutton[3] == 1:  # VINKJE VAN SPRITE
            add_to_spritestock = last_sprite_stock + (20-last_sprite_stock)
            newrow_in_table.append(add_to_spritestock)
        else:
            newrow_in_table.append(last_sprite_stock)

        if output_of_restockbutton[4] == 1:  # VINKJE VAN
            add_to_iceteastock = last_icetea_stock + (20-last_icetea_stock)
            newrow_in_table.append(add_to_iceteastock)
        else:
            newrow_in_table.append(last_icetea_stock)

        if output_of_restockbutton[5] == 1:  # VINKJE VAN DRPEPPER
            add_to_drpepperstock = last_drpepper_stock + (20-last_drpepper_stock)
            newrow_in_table.append(add_to_drpepperstock)
        else:
            newrow_in_table.append(last_drpepper_stock)

        if output_of_restockbutton[6] == 1:  # VINKJE VAN PEPSI
            add_to_pepsistock = last_pepsi_stock + (20-last_pepsi_stock)
            newrow_in_table.append(add_to_pepsistock)
        else:
            newrow_in_table.append(last_pepsi_stock)

        if output_of_restockbutton[7] == 1:  # VINKJE VAN PEPSI
            add_to_fernandesstock = last_fernandes_stock + (20-last_fernandes_stock)
            newrow_in_table.append(add_to_fernandesstock)
        else:
            newrow_in_table.append(last_fernandes_stock)

    with open("sodamachine_db_text.txt", "a") as textfileoutput:
        textfileoutput.write("\n")
        textfileoutput.write(str(newrow_in_table))
        print("Inventory has been restocked succesfully!")


def open_stock():
    top = Toplevel()
    top.title('Stock')
    top.geometry('400x400')
    Label(master=top, text="Select a soda to show its current stock").place(x=93, y=20)
    Label(master=top, text='Current stock of: ').place(x=207, y=45)
    text_block = Text(master=top)
    text_block.place(x=195, y=75, height=269, width=120)

    FantaButton = Button(master=top, text='Fanta', font=small_font, fg="white", bg="#FC8102",
                         command=lambda: text_block.insert(END, "Fanta = " + str(last_fanta_stock) + "\n"))
    FantaButton.place(x=85, y=75, width=100)

    WaterButton = Button(master=top, text='Water', font=small_font, fg="white", bg="#71BBEC",
                         command=lambda: text_block.insert(END, "Water = " + str(last_water_stock) + "\n"))
    WaterButton.place(x=85, y=109, width=100)

    ColaButton = Button(master=top, text='Cola', font=small_font, fg="white", bg="#FE001A",
                        command=lambda: text_block.insert(END, "Cola =  " + str(last_cola_stock) + "\n"))
    ColaButton.place(x=85, y=143, width=100)

    SpriteButton = Button(master=top, text='Sprite', font=small_font, fg="white", bg="#62B43A",
                          command=lambda: text_block.insert(END, "Sprite =  " + str(last_sprite_stock) + "\n"))
    SpriteButton.place(x=85, y=177, width=100)

    IceteaButton = Button(master=top, text='Ice Tea', font=small_font, fg="white", bg="#FFE105",
                          command=lambda: text_block.insert(END, "Ice-tea =  " + str(last_icetea_stock) + "\n"))
    IceteaButton.place(x=85, y=211, width=100)

    DrpepperButton = Button(master=top, text='Dr.Pepper', font=small_font, fg="white", bg="#890024",
                            command=lambda: text_block.insert(END, "Dr.Pepper = " + str(last_drpepper_stock) + "\n"))
    DrpepperButton.place(x=85, y=245, width=100)

    PepsiButton = Button(master=top, text='Pepsi', font=small_font, fg="white", bg="#1C52A2",
                         command=lambda: text_block.insert(END, "Pepsi = " + str(last_pepsi_stock) + "\n"))
    PepsiButton.place(x=85, y=279, width=100)

    FernandesButton = Button(master=top, text='Fernandes', font=small_font, fg="white", bg="#EA1A5C",
                             command=lambda: text_block.insert(END, "Fernandes = " + str(last_fernandes_stock) + "\n"))
    FernandesButton.place(x=85, y=313, width=100)

def average_stock():
    top = Toplevel()
    top.geometry('400x200')
    global inputfield
    inputfield = Entry(top, width=20)
    inputfield.place(x=190, y=30)
    Label(master=top, text="Enter the amount of days:").place(x=30, y=30)
    Label(master=top, text="The average stock for the requested days is:").place(x=30, y=120)
    Button(master=top, text="Input", command=knop).place(x=50, y=50)
    global output_of_averagecalculation
    output_of_averagecalculation = Text(master=top, height=1, width=20)
    output_of_averagecalculation.place(x=270, y=120)

def knop():
    return_of_inputfield = inputfield.get()
    string_of_inputfield = str(return_of_inputfield)
    global integer_of_inputfield
    integer_of_inputfield = int(string_of_inputfield)
    average_amount_of_soda_calculation()


def average_amount_of_soda_calculation(): # shows the average amount of soda that is left over, for the n amount of days
    # global days
    # days = int(input("For how many days do you want the average?: "))

    requested_range = lines_raw[-(integer_of_inputfield + 1):-1]
    str_requested_range = str(requested_range).replace("[", "").replace("]", "").replace("'", "").replace(" ", "").split(",")
    str_requested_range = [int(i) for i in str_requested_range]     # makes a complete list

    def delete_8th_char():          # deletes 8th character from list

        del str_requested_range[8 - 1::8]
        return str_requested_range

    delete_8th_char()
    total = sum(delete_8th_char())  #total amount of all days
    average = total / integer_of_inputfield     # divides the sum with n days
    output_of_averagecalculation.insert(END, str(average))


menu_button.menu.add_command(label='Error Logs', command=open_logs)
menu_button.menu.add_command(label='Restock', command=open_restock)
menu_button.menu.add_command(label='Current Stock', command=open_stock)
menu_button.menu.add_command(label='Average Stock', command=average_stock)


main_screen.mainloop()