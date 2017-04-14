from pyVmomi import vim
from pyVim.connect import SmartConnect, Disconnect
import time
import ssl

def _get_obj(content, vimtype, name):
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

def _get_all_objs(content, vimtype):
    """
    Get all the vsphere objects associated with a given type
    """
    obj = {}
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for c in container.view:
        obj.update({c: c.name})
    return obj


def login_in_guest(username, password):
    return vim.vm.guest.NamePasswordAuthentication(username=username,password=password)

def start_process(si, vm, auth, program_path, args=None, env=None, cwd=None):
    cmdspec = vim.vm.guest.ProcessManager.ProgramSpec(arguments=args, programPath=program_path, envVariables=env, workingDirectory=cwd)
    cmdpid = si.content.guestOperationsManager.processManager.StartProgramInGuest(vm=vm, auth=auth, spec=cmdspec)
    return cmdpid

def is_ready(vm):

    while True:
        system_ready = vm.guest.guestOperationsReady
        system_state = vm.guest.guestState
        system_uptime = vm.summary.quickStats.uptimeSeconds
        if system_ready and system_state == 'running' and system_uptime > 90:
            break
        time.sleep(10)

def get_vm_by_name(si, name):
    """
    Find a virtual machine by it's name and return it
    """
    return _get_obj(si.RetrieveContent(), [vim.VirtualMachine], name)

def get_host_by_name(si, name):
    """
    Find a virtual machine by it's name and return it
    """
    return _get_obj(si.RetrieveContent(), [vim.HostSystem], name)

def get_resource_pool(si, name):
    """
    Find a virtual machine by it's name and return it
    """
    return _get_obj(si.RetrieveContent(), [vim.ResourcePool], name)

def get_resource_pools(si):
    """
    Returns all resource pools
    """
    return _get_all_objs(si.RetrieveContent(), [vim.ResourcePool])

def get_datastores(si):
    """
    Returns all datastores
    """
    return _get_all_objs(si.RetrieveContent(), [vim.Datastore])

#----------------Changed

def get_datastore(si,name):
    """
    Returns the data store
    """
    return _get_obj(si.RetrieveContent(), [vim.Datastore] , name)

def get_hosts(si):
    """
    Returns all hosts
    """
    return _get_all_objs(si.RetrieveContent(), [vim.HostSystem])

def get_datacenters(si):
    """
    Returns all datacenters
    """
    return _get_all_objs(si.RetrieveContent(), [vim.Datacenter])

def get_registered_vms(si):
    """
    Returns all vms
    """
    return _get_all_objs(si.RetrieveContent(), [vim.VirtualMachine])

def get_templates_vms(si):
    """
    Returns all vms
    """
    return _get_all_objs(si.RetrieveContent(), [vim.VmTemplates])
#----------------------------------------------------------------------------------------

def connect():
    vcenter = "183.82.41.58"
    username = "root"
    password = "Nexii@123"

    si = None
    s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    s.verify_mode = ssl.CERT_NONE

    try:
        si = SmartConnect(host = vcenter, user = username, pwd = password)
        print "Valid certificate"
        return si
    except:
        print "Trying to Connect Vcenter ......"
        si = SmartConnect(host = vcenter, user = username, pwd = password, sslContext = s)
        print "Connected to Vcenter Successfully"
        return si 

def disconnect(si):
    print "Trying to Disconnect Vcenter ......"
    Disconnect(si)
    print "Disconeected to Vcenter Successfully"





