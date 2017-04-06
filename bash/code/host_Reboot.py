'''
This will Reboot the given Esxi Host
'''
from vmware import VmwareLib
import logging

logging.basicConfig(filename="log_reboot.txt",level=logging.DEBUG,
format="%(asctime)s-->%(levelname)s-->%(message)s")
class VMRebootException(Exception):
   pass

def VMreboot(si, host_name, obj):
    host = obj.get_host_by_name(si, host_name)
    #This will Reboot the given Esxi Host
    if host:
        force = True
        obj.reboot_host(host, force)
    else:
        raise VMRebootException("Host error")

if __name__ == "__main__":

    # Creating Object for VMwareLib Class
    logging.info("Program Started")
    obj = VmwareLib()
    logging.debug(obj)
    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)
    logging.debug(si)
    if si:
        #Reboot operation
        host_name = "192.168.50.16"
        try:
            VMreboot(si, host_name, obj)
        except VMRebootException as vmerror:
            logging.exception(vmerror)
            print "VMreboot exception"

        # Disconnecting to Vcenter
        obj.disconnect(si)
        logging.info("Program Ended")
