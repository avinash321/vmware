'''
This will put the given Esxi Host into maintanence mode
'''
from vmware import VmwareLib
import logging

logging.basicConfig(filename="log_Esxi_maintanence_mode.txt",level=logging.DEBUG,
format = "%(asctime)s-->%(levelname)s-->%(message)s")

class VMMaintenceException(Exception):
    pass

def maintanencemode(si, host_name, obj):
    host = obj.get_host_by_name(si, host_name)
    # This will put the given Esxi host in maintanence mode
    if host:
        timeout = 3000   # 3000 secends
        obj.exit_maintanence_mode(host, timeout)
    else:
        raise VMMaintenceException("Host Not Found")


def main():
    # Creating Object for VMwareLib Class
    logging.info("Program Started")
    obj = VmwareLib()
    logging.info("Object created for VmwareLib")
    logging.debug(obj)
    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)
    if si:
        logging.info("connection object created")
        logging.debug(si)
        #Reboot operation
        host_name = "192.168.50.22"
        try:
            maintanencemode(si, host_name, obj)
        except VMMaintenceException as vmerror:
            logging.exception(vmerror.message)
            logging.info("VMMaintenence exception")

        # Disconnecting to Vcenter
        obj.disconnect(si)
    logging.info("Program Ended")


if __name__ == "__main__":
    main()


