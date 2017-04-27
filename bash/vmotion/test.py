import atexit
import argparse
import sys
import time
import requests, ssl
from pyVmomi import vim, vmodl
from pyVim import connect
from pyVim.connect import Disconnect
from pyVim.connect import SmartConnect, Disconnect



inputs = {'vcenter_ip': "183.82.41.58",
          'vcenter_password': 'Nexii@123',
          'vcenter_user': 'root',
          'vm_name': 'fancy',
          'destination_host': '192.168.50.16',
          'destination_datastore': "shared_DS_100G"
          }


def get_obj(content, vimtype, name):
    """
     Get the vsphere object associated with a given text name
    """
    obj = None
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        if c.name == name:
            obj = c
            break
    return obj


def wait_for_task(task, actionName='job', hideResult=False):
    """
    Waits and provides updates on a vSphere task
    """
    while task.info.state == vim.TaskInfo.State.running:
        time.sleep(2)
    if task.info.state == vim.TaskInfo.State.success:
        if task.info.result is not None and not hideResult:
            out = '%s completed successfully, result: %s' % (actionName, task.info.result)
            print out
        else:
            out = '%s completed successfully.' % actionName
            print out
    else:
        out = '%s did not complete successfully: %s' % (actionName, task.info.error)
        raise task.info.error
        print out

    return task.info.result


def main():
    # Disabling urllib3 ssl warnings
    #requests.packages.urllib3.disable_warnings()

    # Disabling SSL certificate verification
    #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    #context.verify_mode = ssl.CERT_NONE
    try:
        si = None
        si = SmartConnect(host=vcenter_ip, user=vcenter_user, pwd=vcenter_password, port=443)


        print "Connected to VCENTER SERVER !"

        content = si.RetrieveContent()

        vm = get_obj(content, [vim.VirtualMachine], inputs['vm_name'])
        destination_host = get_obj(content, [vim.HostSystem], inputs['destination_host'])

        destination_datastore = get_obj(content,[vim.Datastore],
                destination_datastore)
        resource_pool = vm.resourcePool

        migrate_priority = vim.VirtualMachine.MovePriority.defaultPriority

        print "Migrating %s to destination host %s" % (inputs['vm_name'], inputs['destination_host'])
        relocate_spec = vim.vm.RelocateSpec(datastore= destination_datastore, host=destination_host)
        task = vm.Relocate(relocate_spec)
        wait_for_task(task, si)

    except vmodl.MethodFault, e:
        print "Caught vmodl fault: %s" % e.msg
        return 1
    except Exception, e:
        print "Caught exception: %s" % str(e)
        return 1

# Start program
if __name__ == "__main__":
    main()