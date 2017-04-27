class Vmotion:
    def vmotion(self):
    '''This method will performs the host vmotion.We need to send the paramaters as targetted host'''
    vm_name = "fancy"
    esx_host = "192.168.50.16"

    # Finding source VM
    vm = self.__get_vm_by_name(vm_name)
    # Finding Targeted Host
    host = self.__get_host_by_name(esx_host)
    if(vm and host):
        # relocate spec, to migrate to another host
        # this can do other things, like storage and resource pool
        # migrations
        relocate_spec = vim.vm.RelocateSpec(host=host)
        try:
            # does the actual migration to host
            task = vm.Relocate(relocate_spec)
            while task.info.state not in [vim.TaskInfo.State.success, vim.TaskInfo.State.error]:
                time.sleep(1)
            ststus = task.info.state
            if status == "success":
                print "Vm Migrated Successfully"
                logging.info("Vm Migrated Successfully")
                return status
            elif status == "error":
                print "failed to migrate the VM"
                logging.info("failed to migrate the VM")
                return status

        except Exception as err:
            logging.info(err.message)
            #print "Vm Migration is Not Successful , Something went wrong"
            print None
    else:
        #raise VmotionException("Vm or Host Not found Error")
        logging.info("The given vm or Host not found")
        print "The given vm or Host not found"

obj = Vmotion()
