# #from Chrome_Actions import *
# from Content_Downloader import *
# from GUI import GUI

# #callback function passing to GUI
# def initRepost(options):
#     print(options)
#     downloader = Content_Downloader(options)
#     downloader.downloadAllAccounts()

#     if options['autoupload']:
#         loginInstagram()
#         uploadMedia()

# gui = GUI(initRepost)


#from Chrome_Actions import *
from downloaderV2 import *
from GUI import GUI

#callback function passing to GUI
def initRepost(options):
    print(options)
    downloaderInit(options)
    downloadAllAccounts()

    # if options['autoupload']:
    #     loginInstagram()
    #     uploadMedia()

gui = GUI(initRepost)
