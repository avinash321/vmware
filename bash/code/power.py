
from vmware import VmwareLib

def get_vm(si,vm_name, obj):

    vm = obj.get_vm_by_name(si,vm_name)
    return vm

def main():
    # Creating Object for VMwareLib Class
    obj = VmwareLib()

    vcenter_ip = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    # Connecting to Vcenter
    si = obj.connect(vcenter_ip, username, password)
    #Getting Vm
    if si:
        vm_name = raw_input("Enter VM name: ")
        vm = get_vm(si, vm_name, obj)
        if vm:
            print "plese select any one of the follwing options"
            n = input("1.Power ON VM    2.Power OFF VM    3.Power state of VM:  ")

            if n==1:
                obj.power_on_vm(vm)

            elif n==2:
                obj.power_off_vm(vm)

            elif n==3:
                obj.power_state_vm(vm)

            else:
                print "please select valid option"

        obj.disconnect(si)

if __name__ == "__main__":
    main()