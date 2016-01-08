import dialogs

protocolFname = "../resources/protocols.txt" # path to the protocols file
storageFname = "../resources/storageDevices.txt" # path to the storage devices file

def getProtocols(fname):
    """get the protocols from the text file and return them as a list"""
    protocols = []

    f = open(fname, "r")
    protos = f.readlines()
    f.close()

    for protocol in protos:
        protocols.append(protocol[:-1]) # remove trailing \n

    return protocols

def getStorage(fname):
    """get the storage devices from the text file and return them as a list"""
    storage = []

    f = open(fname, "r")
    storeDevs = f.readlines()
    f.close()


    for storeDev in storeDevs:
        storage.append(storeDev[:-1]) # remove trailing \n

    return storage

protocols = getProtocols(protocolFname)
storage = getStorage(storageFname)

def getRemoveProtocol():
    """creates a graphical dialog to remove a protocol"""
    proto = protocols # get the current protocols
    res, ok = dialogs.RemoveProtocol.getDataDialog() # creates graphical dialog
    if ok:
        try:
            proto.remove(res) # remove the selected protocol
            rewriteResource(proto, protocolFname) # rewrite the protocols text file
        except ValueError:
            return

def getAddProtocol():
    """creates a graphical dialog to add a protocol"""
    proto = protocols
    res, ok = dialogs.AddProtocol.getDataDialog()
    if ok:
        proto.append(res) # add the new protocol 
        rewriteResource(proto, protocolFname) # rewrite the protocols text file

def getRemoveStorage():
    """creates a graphical dialog to remove a storage device"""
    store = storage
    res, ok = dialogs.RemoveStorage.getDataDialog()
    if ok:
        try:
            store.remove(res)
            rewriteResource(store, storageFname)
        except ValueError:
            return

def getAddStorage():
    """creates a graphical dialog to add a storage device"""
    store = storage
    res, ok = dialogs.AddStorage.getDataDialog()
    if ok:
        store.append(res)
        rewriteResource(store, storageFname)



def rewriteResource(resource, fname):
    """rewrite the given text file with the new resources"""
    f = open(fname, "w")

    for item in resource:
        f.write(item + "\n") # delimit each entry with a \n

    f.close()


