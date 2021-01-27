# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------#

import requests, sys
import os.path
import yaml
DOCUMENTATION = """ 
    1. Create a virtualenv. # virtualenv .env -p python3
    2. Activate that virtualenv. # source .env/bin/activate 
    3. Install requirements. # pip3 install -r requirements.txt

"""
# ------------------------------------------------------------------------------#
def get_properties_from_dg(url):
    """ Function: obtain properties in json format from url
        @param url: url to connect with
        @return: json format returned by the url
    """
    try:
        r = requests.get(url, verify=False)
        if r.status_code != 200:
            return None
        else:
            return r.json()
    except:
        print("Ha fallado la conexión con la url {}".url)

# ------------------------------------------------------------------------------#
def to_yaml(data):
    """ Function: parse dictionary to yaml
        @param data: dictionary
        @return: yaml format
    """
    return yaml.safe_dump(data)

# Method to create a uniq dictionary containing deleting duplicated keys and values
# ------------------------------------------------------------------------------#
def create_uniq(orig,new,server):
    """ Function: combine two different dictionaries. If a key with a different value is found that key is stored in a different global dictionary
        @param orig: dictionary to be compared with
        @param new: dictionary to compare
        @param server: only used if duplicated keys found with different value to identify servers
        @return my_dic: combined dictionary with new properties added
    """
    my_dic = orig.copy()

    for key, value in new.items():
        if key not in orig.keys():
            my_dic[key] = value
        # Key con valor diferente
        elif value != orig[key]:
            custom_name = server+"_"+key
            global duplicated_properties
            duplicated_properties[custom_name] = value

    return my_dic

# ------------------------------------------------------------------------------#
def obtain_servers(inventory_file, dg_name):
    """ Function: obtain servers from an inventory file. This function is addapted to our inventories format, _lr or _cr for production, etc
        @param inventory_file: ansible dg inventory
        @param dg_name: dg_assisted, dg_genoma, etc the name as it is found in the groups of our inventories
        @return servers: list of servers
    """

    with open(inventory_file,"rt",encoding="utf-8") as f:
        inventory = f.read()
        inventory = inventory.strip()
        lines=inventory.splitlines()
        inventory = [ a for a in lines if a != "" ]

        lr = dg_name+"_lr"
        cr = dg_name+"_cr"
        servers = list()

        # check if inventory is divided in lr and cr
        if lr in inventory:
            pos_lr = inventory.index("["+lr+"]")
            pos_cr = inventory.index("["+cr+"]")
            pos_last = inventory.index("["+dg_name+":children]")

            if pos_lr < pos_cr:
                servers = inventory[pos_lr+1:pos_cr]
                servers = servers + inventory[pos_cr+1:pos_last]
            else:
                servers = inventory[pos_cr+1:pos_lr]
                servers = servers + inventory[pos_lr+1:pos_last]
        # If not extract directly the servers
        elif "["+dg_name+"]" in inventory:
            pos_dg = inventory.index("["+dg_name+"]")

            while not inventory[pos_dg+1].startswith("["):
                servers.append(inventory[pos_dg+1])
                pos_dg += 1
        else:
            print("El DG solicitado no está en el inventario facilitado")

        # check if server has an alias and we keep the host name deleting the alias. if servers to check that list is not empty
        if servers and "ansible_host" in servers[0]:
            servers = [ a.split("ansible_host=")[1] for a in servers]
        
        return servers

# ------------------------------------------------------------------------------#
def obtain_servers_from_imput():
    """ Function: ask the user from manual imput of servers if they haven't been found in inventory file
    """
    servers = input("The request dg haven't been found in the provided inventory, please introduce list of servers separated by , :")
    servers = servers.replace(" ","")
    servers = servers.split(",")
    return servers

# ------------------------------------------------------------------------------#
def show_usage():
    print("""Usage: 
    This script admits different parameters. It can take an inventory file as argument (thinked to be used with new DGs in jboss7 using their ansible inventories)
        python3 {0} <dg_name> <protocol(http or https)> <inventory_file>
    Ej: python3 {0} assisted https pro_green_jboss_instances_dg
    Or you can pass directly the servers you want to connect with
        python3 {0} <dg_name> <protocol(http or https)> server1 server2 server3
    Ej: python3 {0} assisted http projboss10 projboss11 projboss12 bcpjboss10 bcpjboss11 bcpjboss12
    """.format(sys.argv[0]))

# ------------------------------------------------------------------------------#
def validate_args():
    """ Function to validate the provided args
        argv[1] - DG name (without dg_)
        argv[2] - http or https protocol to connect with
        argv[3] - inventory_file or first server to connect with
        ...
        argv[n] - n server to connect with
    """
    if len(sys.argv) >= 3:
        dg = sys.argv[1]
        protocol = sys.argv[2]
        if os.path.exists(sys.argv[3]) and os.path.isfile(sys.argv[3]):
            provided_file = sys.argv[3]
            return [dg, protocol, provided_file]
        # if argv[3] is not an existing file we assume that it is a server to connect with
        else:
            servers = sys.argv[3:]
            return [dg, protocol, servers]
    else:
        show_usage()
        sys.exit()

# ------------------------------------------------------------------------------#
def obtain_properties(servers, port, protocol):
    """ Function: given a list of servers and their port return an uniq dictionary with their combined properties
        @param servers: list of servers to connect with
        @param port: port in what DGs are listening
        @param protocol: http or https protocol to connect with
        @return mydic: uniq dictionary with combined properties
    """
    mydic = {}
    for server in servers:
        URL = protocol+"://"+server+":"+port+"/IDEsWeb/properties"
        data = get_properties_from_dg(URL)
        if data != None:
           mydic = create_uniq(mydic,data,server)
    return mydic

# ------------------------------------------------------------------------------#
def create_file(dg_name, yaml_dic):
    """ Function: create a file dg_name_application.properties with the yaml_dic
        @param dg_name: name of the dg to give the name to the file
        @param yaml_dic: properties to be written
    """
    with open(dg_name+"_application.properties","wt",encoding="utf-8") as f:
        f.write(yaml_dic)
        print("Result can be found at {}_application.properties file".format(dg_name))

# ------------------------------------------------------------------------------#
# global dictionary to control duplicated properties
duplicated_properties = {}
if __name__ == "__main__":
    ports = {"genoma":"9107","debitcard":"9097","metascan":"9104","statusline":"9092","IDEsBMB":"9087","renta4":"9103","SMEs":"9102","SMEsBATCH":"9105","SMEsINT":"9080","IDEsBPM":"9083","IDEsINT":"9186","IDEs":"9081","databus_client":"9111","IDEsATM":"9106","IDEsBATCH":"9082","IDEsMR2_PAF":"9116","Mailroom1":"9089","assisted":"9113","chat_proactivo":"9115","minreg":"9093"}
    # validate_args returns the inventory_file or a list of servers
    dg_name, protocol, inventory_or_server = validate_args()
    port = ports[dg_name]
    if isinstance(inventory_or_server, str): # is a string so we have the inventory file
        servers = obtain_servers(inventory_or_server, "dg_"+dg_name)
        if not servers: # If dg is not found in inventory file we ask the user for a list of servers
            servers=obtain_servers_from_imput()
    else: # Servers have been passed as argument
        servers = inventory_or_server

    dic = obtain_properties(servers, port, protocol)
    yaml_properties = to_yaml(dic)
    print()
    create_file(dg_name, yaml_properties)
    print()

    if duplicated_properties:
        print("WARNING: the following properties have different value between different servers, only one of them was added")
        print(to_yaml(duplicated_properties))
