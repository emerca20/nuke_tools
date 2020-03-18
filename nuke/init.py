#----------------------------------------
import nuke
def myTracker():
	n = nuke.thisNode()
	int_k = nuke.Int_Knob('timeOffset_val', '')
	txt_k = nuke.Text_Knob('timeOffset', '')
	txt_k.setLabel('Time Offset')
	pyBtn_k = nuke.PyScript_Knob('timeOffset_btn', 'apply Time offset')
	pyBtn_k.clearFlag(nuke.STARTLINE)
	pyBtn_k.setCommand("if(nuke.thisNode().knob('tracks').value() != 0.0):\n\tnuke.thisNode().knob('tracks').setExpression(\"curve(frame+(this.timeOffset_val)*-1)\")\nelse:\n\tnuke.message('No tracks found on this tracker node!')")

	if not n.knob(int_k.name()) and not n.knob(txt_k.name()):
		n.addKnob(txt_k)
		n.addKnob(int_k)
		n.knob(int_k.name()).setValue(1)
		n.addKnob(pyBtn_k)

		#'Tracker4' custom default knob values
		#----------------------------------------
		n.knob('pretrack_filter').setValue('none')
		n.knob('max_error').setValue(0.1)
		n.knob('warp').setValue('srt')
		n.knob('label').setValue("reference_frame==[format %03d [value this.knob.reference_frame]]")


nuke.addOnCreate(myTracker, nodeClass="Tracker4")
nuke.removeOnCreate(myTracker)
