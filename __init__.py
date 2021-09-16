# mandatory file

# code for testing

DEBUG = True
from sys import path
sys.path.append('/C:/Python35/Lib/site-packages')
if DEBUG:
    import ptvsd
    print("Waiting for debugger attach")
    # 5678 is the default attach port in the VS Code debug configurations
    #ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    ptvsd.enable_attach(address=('localhost', 5678))
    ptvsd.wait_for_attach()
    # my stuff
    print("1st breakpoint")
