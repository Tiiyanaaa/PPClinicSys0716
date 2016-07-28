from collective.grok import gs
from PPClinicSys0716.app import MessageFactory as _

@gs.importstep(
    name=u'PPClinicSys0716.app', 
    title=_('PPClinicSys0716.app import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('PPClinicSys0716.app.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
