*** Settings ***
Library           ../bash/avinash/Vmware_Operations.py

*** Test Cases ***
disk_space_increase
    Connect    183.82.41.58    root    Nexii@123
    Disk Space Increase    avinash    11    Nexiilabs
    Disconnect
    [Teardown]

reboot_esxi_host
    Connect    183.82.41.58    root    Nexii@123
    Reboot Host    192.168.50.22
    Disconnect

Enter_maintanencemode_esxi_host
    [Template]
    Connect    183.82.41.58    root    Nexii@123
    Enter Maintanence Mode    192.168.50.22    3000
    Disconnect

exit_maintanencemode_esxi_host
    Connect    183.82.41.58    root    Nexii@123
    Exit Maintanence Mode    192.168.50.22    30000
    Disconnect

power_on_vm
    Connect    183.82.41.58    root    Nexii@123
    Power On Vm    fancy
    Disconnect

power_off_vm
    Connect    183.82.41.58    root    Nexii@123
    Power Off Vm    avinash
    Disconnect

get_vm_power_status
    [Setup]
    Connect    183.82.41.58    root    Nexii@123
    Power State Vm    avinash
    Disconnect

group
    Connect    183.82.41.58    root    Nexii@123
    Disk Space Increase    avinash    10    Nexiilabs
    Reboot Host    192.168.50.22
    Enter Maintanence Mode    192.168.50.22    3000
    Exit Maintanence Mode    192.168.50.22    3000
    Power On Vm    avinash
    Power Off Vm    avinash
    Power State Vm    avinash
    Migration    fancy    192.168.50.14    pool-14
    Disconnect

migration
    Connect    183.82.41.58    root    Nexii@123
    Migration    fancy    192.168.50.14    pool-14
    Disconnect
