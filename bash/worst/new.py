#!/usr/bin/env python
"""
Written by Dann Bohn
Github: https://github.com/whereismyjetpack
Email: dannbohn@gmail.com
Clone a VM from template example
"""
from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import atexit
import argparse
import getpass
import connect


def wait_for_task(task):
    """ wait for a vCenter task to finish """
    task_done = False
    while not task_done:
        if task.info.state == 'success':
            return task.info.result

        if task.info.state == 'error':
            print "there was an error"
            print task.info.result
            task_done = True


def get_obj(content, vimtype, name):
    """
    Return an object by name, if name is None the
    first found object is returned
    """
    obj = None
    container = content.viewManager.CreateContainerView(
        content.rootFolder, vimtype, True)
    for c in container.view:
        if name:
            if c.name == name:
                obj = c
                break
        else:
            obj = c
            break

    return obj


def clone_vm(
        content, template, vm_name, si,
        datacenter_name, vm_folder, datastore_name,
        cluster_name, resource_pool, power_on):
    """
    Clone a VM from a template/VM, datacenter_name, vm_folder, datastore_name
    cluster_name, resource_pool, and power_on are all optional.
    """

    # if none git the first one
    destfolder =None
    datacenter = get_obj(content, [vim.Datacenter], datacenter_name)
    print datacenter.name

    if vm_folder:
        destfolder = get_obj(content, [vim.Folder], vm_folder)
        print "1st" + destfolder.name
    else:
        destfolder = datacenter.vmFolder
        print "2nd" + destfolder

    if datastore_name:
        datastore = get_obj(content, [vim.Datastore], datastore_name)
        print "1st"+datastore.name
    else:
        datastore = get_obj(content, [vim.Datastore], template.datastore[0].info.name)
        print "2nd"+datastore

    # if None, get the first one
    cluster = get_obj(content, [vim.ClusterComputeResource], cluster_name)
    print cluster

    if resource_pool:
        resource_pool = get_obj(content, [vim.ResourcePool], resource_pool)
        print resource_pool
    else:
        resource_pool = cluster.resourcePool
        print "2nd"+resource_pool

    # set relospec
    relospec = vim.vm.RelocateSpec()
    relospec.datastore = datastore
    #relospec.pool = resource_pool



    clonespec = vim.vm.CloneSpec()
    clonespec.location = relospec
    clonespec.powerOn = True
    clonespec.template = True

    print "cloning VM..."
    task = template.Clone(folder=destfolder, name=vm_name, spec=clonespec)
    wait_for_task(task)


def main():
    """
    Let this thing fly
    """

    # connect this thing
    si = connect.connect()
    # disconnect this] thing
    #atexit.register(Disconnect, si)

    content = si.RetrieveContent()
    template = "mytemp"
    template = get_obj(content, [vim.VirtualMachine], template)

    print template

    clone_vm(content, template, "avinash12", si,
            "Nexiilabs", "vm",
            "datastore1 (1)", "namec",
            "DEV", True)

    print "Template Created Successfully"

    connect.disconnect(si)

# start this thing
if __name__ == "__main__":
    main()