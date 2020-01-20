from tkinter import *


main_screen = Tk()
main_screen.title('Main menu')
main_screen.geometry('300x300')


def clicked():
    entry = password_entry.get
    label = Label(master=top, text=entry)
    label.pack(CENTER)



def open_stock():
    top = Toplevel()
    password_entry = Entry(master=top, text='Password')
    password_entry.pack(pady=10, padx=10)
    password = password_entry.get
    button = Button(master=top, text='Update stock')
    button.pack(pady=50, padx=50)
    stock_amount = Label(master=top, text=password)
    stock_amount.pack(pady=10, padx=10)
    top.title('Stock')


def open_error_logs():
    top = Toplevel()
    button = Button(master=top, text='Error logs')
    button.pack(pady=50, padx=50)
    top.title('Error logs')


def open_sales():
    top = Toplevel()
    button = Button(master=top, text='Sales')
    button.pack(pady=50, padx=50)
    top.title('Sales')


def open_orders():
    cola = 2.00
    cola_light = 2.50
    fanta = 1.50
    red_bull = 3.00


    top = Toplevel()
    order_label = Label(master=top, text='What would you like to drink?')
    order_label.pack(pady=10, padx=10)
    price_drink = Label(master=top, text='The price of the chosen product is ' + str(cola))
    price_drink.pack(pady=10, padx=10)
    button_7up = Button(master=top, text='7Up')
    button_7up.pack(pady=10, padx=10)
    button_cola_light = Button(master=top, text='Cola Light')
    button_cola_light.pack(pady=10, padx=10)
    button_cola = Button(master=top, text='Cola')
    button_cola.pack(pady=10, padx=10)
    button_fanta = Button(master=top, text='Fanta')
    button_fanta.pack(pady=10, padx=10)

    top.title('Orders')

close_windows_button = Button(master=main_screen, text='Close window(s)', command=main_screen.destroy)
close_windows_button.pack(pady=30, padx=30)
mb = Menubutton(main_screen, text='Main menu', font='arial')
mb.menu = Menu(mb)
mb['menu'] = mb.menu


mb.menu.add_command(label='Orders', command=open_orders)
mb.menu.add_command(label='Sales', command=open_sales)
mb.menu.add_command(label='Error Logs', command=open_error_logs)
mb.menu.add_command(label='Stock', command=open_stock)

mb.pack()


main_screen.mainloop()
