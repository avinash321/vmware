from vmware import VmwareLib
from pyVmomi import vim

# Creating the object for vmwareLib class
def name(vm_name, obj):
    vm = obj.get_vm_by_name(si,vm_name)
    t = obj.power_on_vm(vm)
    print t.info.state

def main():
    # Creating Object for VMwareLib Class
    obj = VmwareLib()
    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "VMware@123"
    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)
    name("avinash",obj)
    obj.disconnect(si)

if __name__ == "__main__":
    main()