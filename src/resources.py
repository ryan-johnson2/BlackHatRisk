import dialogs

protocolFname = "../resources/protocols.txt"
storageFname = "../resources/storageDevices.txt"

def getProtocols(fname):
    protocols = []

    f = open(fname, "r")
    protos = f.readlines()
    f.close()

    for protocol in protos:
        protocols.append(protocol[:-1])

    return protocols

def getStorage(fname):
    storage = []

    f = open(fname, "r")
    storeDevs = f.readlines()
    f.close()


    for storeDev in storeDevs:
        storage.append(storeDev[:-1])

    return storage

protocols = getProtocols(protocolFname)
storage = getStorage(storageFname)

def getRemoveProtocol():
    proto = protocols
    res, ok = dialogs.RemoveProtocol.getDataDialog()
    if ok:
        try:
            proto.remove(res)
            rewriteResource(proto, protocolFname)
        except ValueError:
            return

def getAddProtocol():
    proto = protocols
    res, ok = dialogs.AddProtocol.getDataDialog()
    if ok:
        proto.append(res)
        rewriteResource(proto, protocolFname)

def getRemoveStorage():
    store = storage
    res, ok = dialogs.RemoveStorage.getDataDialog()
    if ok:
        try:
            store.remove(res)
            rewriteResource(store, storageFname)
        except ValueError:
            return

def getAddStorage():
    store = storage
    res, ok = dialogs.AddStorage.getDataDialog()
    if ok:
        store.append(res)
        rewriteResource(store, storageFname)



def rewriteResource(resource, fname):
    f = open(fname, "w")

    for item in resource:
        f.write(item + "\n")

    f.close()


