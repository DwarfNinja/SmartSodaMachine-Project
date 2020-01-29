import mysql.connector
import smtplib

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
select_data_from_table="SELECT * FROM  soda_stock"  #TODO: RIENK
cursor.execute(select_data_from_table)  # frisdrank_voorraad
print (select_data_from_table, "has been executed")


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


# ____________________________________
# user_input and answers of user_input

print("Choose out of the following soda's:" "\n", all_sodas_string, "\n")

user_input = input("From which soda do you want information?")

if user_input.lower() == "fanta":
    print(soda_name_fanta() + " has a stock of: " + str(last_fanta_stock))
elif user_input.lower() == "water":
    print(soda_name_water() + " has a stock of: " + str(last_water_stock))
elif user_input.lower() == "cola":
    print(soda_name_cola() + " has a stock of: " + str(last_cola_stock))
elif user_input.lower() == "sprite":
    print(soda_name_sprite() + " has a stock of: " + str(last_sprite_stock))
elif user_input.lower() == "icetea":
    print(soda_name_icetea() + " has a stock of: " + str(last_icetea_stock))
elif user_input.lower() == "drpepper":
    print(soda_name_drpepper() + " has a stock of: " + str(last_drpepper_stock))
elif user_input.lower() == "pepsi":
    print(soda_name_pepsi() + " has a stock of: " + str(last_pepsi_stock))
elif user_input.lower() == "fernandes":
    print(soda_name_fernandes() + " has a stock of: " + str(last_fernandes_stock))


print("Test Check sheet is: ", last_line)


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

restock_notification = "OFF"
while restock_notifications == "ON":
    restock_notifications()

if stock_is_low == True:
    send_email_notification()


fanta_manual_restockbutton = True


input_manual_restockamount = int() #  INVUL VAKJE ACHRAF



if manual_restockbutton == geklicked: # KNOP OM TE RESTOCKEN
    newrow_in_table = []

    if indexering_van_welke_soda[1] == True: # VINKJE VAN FANTA
            add_to_fantastock = last_fanta_stock + input_manual_restockamount  #  OR 5
            newrow_in_table.append(add_to_fantastock)
    else:
        newrow_in_table.append(last_fanta_stock)

    if water_manual_restockbutton == True: # VINKJE VAN WATER
            add_to_waterstock = last_water_stock + input_manual_restockamount
            newrow_in_table.append(add_to_waterstock)
    else:
        newrow_in_table.append(last_water_stock)

    if cola_manual_restockbutton == True: # VINKJE VAN COLA
            add_to_colastock = last_cola_stock + input_manual_restockamount
            newrow_in_table.append(add_to_colastock)
    else:
        newrow_in_table.append(last_cola_stock)

    if sprite_manual_restockbutton == True: # VINKJE VAN SPRITE
            add_to_spritestock = last_sprite_stock + input_manual_restockamount
            newrow_in_table.append(add_to_spritestock)
    else:
        newrow_in_table.append(last_sprite_stock)

    if icetea_manual_restockbutton == True: # VINKJE VAN
            add_to_iceteastock = last_icetea_stock + input_manual_restockamount
            newrow_in_table.append(add_to_iceteastock)
    else:
        newrow_in_table.append(last_iceatea_stock)

    if drpepper_manual_restockbutton == True: # VINKJE VAN DRPEPPER
            add_to_drpepperstock = last_drpepper_stock + input_manual_restockamount
            newrow_in_table.append(add_to_drpepperstock)
    else:
        newrow_in_table.append(last_drpepper_stock)

    if pepsi_manual_restockbutton == True: # VINKJE VAN PEPSI
            add_to_pepsistock = last_pepsi_stock + input_manual_restockamount
            newrow_in_table.append(add_to_pepsistock)
    else:
        newrow_in_table.append(last_pepsi_stock)

    if fernandes_manual_restockbutton == True: # VINKJE VAN PEPSI
            add_to_fernandesstock = last_fernandes_stock + input_manual_restockamount
            newrow_in_table.append(add_to_fernandesstock)
    else:
        newrow_in_table.append(last_fernandes_stock)


