import re
cm=hou.pwd().path()
val=hou.node(cm).parm('vm_picture').eval()
pmap=hou.hscript('pathmap -ct %s'%val)[0]
if pmap:
    sP=re.sub('\n', '',pmap)
    pSplit=sP.split('.')
    pSplit[-2]='%sF'%'$'
    finalPath='.'.join(pSplit)
    hou.node(cm).parm('vm_picture').set(finalPath)