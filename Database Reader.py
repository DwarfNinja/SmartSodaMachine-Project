import mysql.connector

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
        soda_machine_db_info = soda_machine_db_connection.get_server_info()
        print("Connected to MySQL database... MySQL Server version on ", soda_machine_db_info, "\n")

except NameError:
    print("Error while connecting to MySQL")


cursor = soda_machine_db_connection.cursor()

cursor.execute("SELECT * FROM  soda_stock")  # frisdrank_voorraad


all_sodas_string = "Fanta, Water, Cola, Sprite, Ice-Tea, Dr.Pepper, Pepsi, Fernandes"

# ____________________________________________________________________________________________
# copies all content from database, adds soda names to the top and prints if it has succeeded
with open("sodamachine_db_text.txt", "w") as textfileoutput:
    textfileoutput.write(all_sodas_string)
    for lastrow_in_all_data in cursor:
        data_in_stringformat = str(lastrow_in_all_data)
        textfileoutput.write("\n" + data_in_stringformat)

print("The file's contents have been copied", "\n")

# __________________________________________
# Return name of soda function for each soda

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

def last_fanta_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_fanta_supply = lastrow_in_all_data[0]
        return last_fanta_supply


def last_water_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_water_stock = lastrow_in_all_data[1]
        return last_water_stock


def last_cola_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_cola_stock = lastrow_in_all_data[2]
        return last_cola_stock


def last_sprite_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_sprite_stock = lastrow_in_all_data[3]
        return last_sprite_stock


def last_icetea_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_icetea_stock = lastrow_in_all_data[4]
        return last_icetea_stock


def last_drpepper_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_drpepper_stock = lastrow_in_all_data[5]
        return last_drpepper_stock


def last_pepsi_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_pepsi_stock = lastrow_in_all_data[6]
        return last_pepsi_stock


def last_fernandes_stock():
    with open('sodamachine_db_text.txt', 'r'):
        last_fernandes_stock = lastrow_in_all_data[7]
        return last_fernandes_stock


# ____________________________________
# user_input and answers of user_input

print("Choose out of the following soda's:" "\n", all_sodas_string, "\n")

user_input = input("From which soda do you want information?")

if user_input.lower() == "fanta":
    print(soda_name_fanta() + " has a stock of: " + str(last_fanta_stock()))
elif user_input.lower() == "water":
    print(soda_name_water() + " has a stock of: " + str(last_water_stock()))
elif user_input.lower() == "cola":
    print(soda_name_cola() + " has a stock of: " + str(last_cola_stock()))
elif user_input.lower() == "sprite":
    print(soda_name_sprite() + " has a stock of: " + str(last_sprite_stock()))
elif user_input.lower() == "icetea":
    print(soda_name_icetea() + " has a stock of: " + str(last_icetea_stock()))
elif user_input.lower() == "drpepper":
    print(soda_name_drpepper() + " has a stock of: " + str(last_drpepper_stock()))
elif user_input.lower() == "pepsi":
    print(soda_name_pepsi() + " has a stock of: " + str(last_pepsi_stock()))
elif user_input.lower() == "fernandes":
    print(soda_name_fernandes() + " has a stock of: " + str(last_fernandes_stock()))

# To manually check if the correct values have been given, can be removed in final
print("Test Check sheet is: ", data_in_stringformat)
