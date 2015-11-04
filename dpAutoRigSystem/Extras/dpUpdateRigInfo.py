# importing libraries:
import maya.cmds as cmds
import maya.mel as mel

# global variables to this module:    
CLASS_NAME = "UpdateRigInfo"
TITLE = "m057_updateRigInfo"
DESCRIPTION = "m058_updateRigInfoDesc"
ICON = "/Icons/dp_updateRigInfo.png"


class UpdateRigInfo():
    def __init__(self, *args, **kwargs):
        # call main function
        self.dpMain(self)
    
    
    def dpMain(self, *args):
        """ Main function.
            Just call the update function.
        """
        self.updateRigInfoLists()
    

    @staticmethod
    def updateRigInfoLists(*args):
        """
        """
        masterCtrl = None
        masterCtrlAttr = "masterCtrl"
        allList = cmds.ls(selection=False)
        for nodeItem in allList:
            if cmds.objExists(nodeItem+"."+masterCtrlAttr) and \
                (cmds.getAttr(nodeItem+"."+masterCtrlAttr, type=True) == "bool" or \
                cmds.getAttr(nodeItem+"."+masterCtrlAttr, type=True) == "long") and \
                cmds.getAttr(nodeItem+"."+masterCtrlAttr) == 1:
                masterCtrl = nodeItem
        if masterCtrl:
            ctrlList = cmds.ls("*_Ctrl")
            ctrlString = ""
            if ctrlList:
                for i, item in enumerate(ctrlList):
                    ctrlString = ctrlString + str(item)
                    if i < len(ctrlList):
                        ctrlString = ctrlString + ";"
                cmds.setAttr(masterCtrl+".controlList", ctrlString, type="string")
            
            meshList = cmds.ls("*_Mesh")
            meshString = ""
            if meshList:
                for i, item in enumerate(meshList):
                    meshString = meshString + str(item)
                    if i < len(meshList):
                        meshString = meshString + ";"
                cmds.setAttr(masterCtrl+".geometryList", meshString, type="string")
            print "Control List = ", ctrlString
            print "Mesh List    = ", meshString
            print "Updated Rig Info: "+masterCtrl,
