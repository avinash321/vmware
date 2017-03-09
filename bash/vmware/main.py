import vcenter
# Connect to Vcenter Server
vcenter.connect()
# Get the current Date from the Vcenter server
vcenter.currentDate()
# To get the Vsphere Info
vcenter.vsphere_info()
# To get all the list of datacenters
vcenter.datacenters()
# To get all the list of Vms
vcenter.vmlist()
#Disconnect from Vcenter
vcenter.disConnect()