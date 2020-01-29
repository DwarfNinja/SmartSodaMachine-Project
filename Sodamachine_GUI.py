from tkinter import *
import mysql.connector


main_screen = Tk()
main_screen.title('Main menu')
main_screen.geometry('300x300')


def database_connection():

    # _____________________________________________________________________________________________
    # makes connection, exception for connection fail and grabs and sets variable for the data
    try:
        soda_machine_db_connection = mysql.connector.connect(
            host='84.85.94.66',
            port=3306,
            user='root',
            password='MySQLPassword',
            database='smart_soda_machine', )  # frisdrank_automaat

        if soda_machine_db_connection.is_connected():
            sodamachine_db_info = soda_machine_db_connection.get_server_info()
            top = Toplevel()
            my_connection_label = Label(master=top, text="Connected to MySQL database... MySQL Server version on " )
            my_connection_label.pack(pady=10, padx=10)
            print("Connected to MySQL database... MySQL Server version on ", sodamachine_db_info, "\n")

    except NameError:
        print("Error while connecting to MySQL")
        top = Toplevel()
        my_connection_label = Label(master=top, text="Error while connecting to MySQL ")
        my_connection_label.pack(pady=10, padx=10)


def open_restock():
    my_entry = StringVar()
    fanta_checked = IntVar()
    sprite_checked = IntVar()
    coca_cola_checked = IntVar()
    drpepper_checked = IntVar()
    water_checked = IntVar()

    def var_checked():
        print(fanta_checked.get(), sprite_checked.get(), coca_cola_checked.get(), drpepper_checked.get(), water_checked.get())

    top = Toplevel()
    fanta_check_button = Checkbutton(master=top, text='Fanta', variable=fanta_checked)
    fanta_check_button.pack(pady=10, padx=10)
    cola_check_button = Checkbutton(master=top, text='Coca Cola', variable=coca_cola_checked)
    cola_check_button.pack(pady=10, padx=10)
    drpepper_check_button = Checkbutton(master=top, text='Dr.Pepper', variable=drpepper_checked)
    drpepper_check_button.pack(pady=10, padx=10)
    water_check_button = Checkbutton(master=top, text='Water', variable=water_checked)
    water_check_button.pack(pady=10, padx=10)
    sprite_check_button = Checkbutton(master=top, text='Sprite', variable=sprite_checked)
    sprite_check_button.pack(pady=10, padx=10)
    amount_restocked_label = Label(master=top, text='When you press the button, every checked \ndrink will be updated with + 5')
    amount_restocked_label.pack(pady=10, padx=10)
    amount_resctock_confirm = Button(master=top, text='Confirm restock', command=var_checked)
    amount_resctock_confirm.pack(pady=10, padx=10)
    amount_restock_email = Checkbutton(master=top, text='Receive E-Mail notifications.')
    amount_restock_email.pack(pady=10, padx=10)
    button = Button(master=top, text='Check database connection', command=database_connection)
    button.pack(pady=20, padx=20)
    print(fanta_checked)
    top.title('Restock')



def open_error_logs():
    top = Toplevel()
    button = Button(master=top, text='Logs')
    button.pack(pady=50, padx=50)
    top.title('Error logs')


def open_stock():
    top = Toplevel()
    top.geometry('500x500')
    stock_label = Label(master=top, text='Welcome to a overview of the current stock')
    stock_label.pack(pady=10, padx=10)
    text_blok = Text(master=top)
    text_blok.place(x=100, y=50, height=300, width=300)
    get_stock_button1 = Button(master=top, text='Fanta')
    get_stock_button1.place(x=120, y=360)
    get_stock_button2 = Button(master=top, text='Coca cola')
    get_stock_button2.place(x=160, y=360)
    get_stock_button3 = Button(master=top, text='Water')
    get_stock_button3.place(x=220, y=360)
    get_stock_button4 = Button(master=top, text='Sprite')
    get_stock_button4.place(x=260, y=360)
    get_stock_button5 = Button(master=top, text='Dr.Pepper')
    get_stock_button5.place(x=300, y=360)
    get_stock_button6 = Button(master=top, text='Ice Tea')
    get_stock_button6.place(x=160, y=390)
    get_stock_button7 = Button(master=top, text='Fernandes')
    get_stock_button7.place(x=205, y=390)
    get_stock_button8 = Button(master=top, text='Pepsi')
    get_stock_button8.place(x=240, y=390)
    top.title('Stock')


def old_stock():
    top = Toplevel()
    top.geometry('500x500')
    text_blok = Text(master=top)
    text_blok.place(x=100, y=50, height=300, width=300)
    open_old_stock_button = Button(master=top, text='Get all stock')
    open_old_stock_button.pack(pady=10, padx=10)







close_windows_button = Button(master=main_screen, text='Close window(s)', command=main_screen.destroy)
close_windows_button.pack(pady=30, padx=30)
menu_button = Menubutton(main_screen, text='Main menu', font='arial')
menu_button.menu = Menu(menu_button)
menu_button['menu'] = menu_button.menu


menu_button.menu.add_command(label='Error Logs', command=open_error_logs)
menu_button.menu.add_command(label='Restock', command=open_restock)
menu_button.menu.add_command(label='Current Stock', command=open_stock)  # Cendur verandert
menu_button.menu.add_command(label='Average Stock', command=old_stock)  # Cendur verandert


menu_button.pack()


main_screen.mainloop()
