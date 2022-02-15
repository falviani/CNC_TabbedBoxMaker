'''
Globally available data
'''
boxData = None
theDoc = None
theSketches = {}  # probably need 1 sketch per plate, retrieve by name
aBody = None
bodyName = ""


#accessors
def setDoc(d):
    global theDoc
    theDoc = d

def getDoc():
    global theDoc
    return theDoc

def setBody(b):
    global aBody
    aBody = b

def getBody():
    global aBody
    return aBody

def setBodyName(nm):
    global bodyName
    bodyName = nm

def getBodyName():
    global bodyName
    return bodyName

def setBoxData(bd):
    global boxData
    boxData = bd

def getBoxData():
    global boxData
    return boxData

def addSketch(nm, sk):
    """
    This can replace an existing sketch
    """
    global theSketches
    if nm is not None and sk is not None:
        theDoc[nm] = sk

def getSketch(nm):
    global theSketches
    if nm is not None:
        return theSketches[nm]
    else:
        return None

# miscellaneous
def test1():
    # examine what's actually stored
    bd = boxData
    d = theDoc
    aB = aBody
    bN = bodyName
