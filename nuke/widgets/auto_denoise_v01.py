import nuke
import os
def auto_denoise():
	#check to make sure only 1 node is selected, and that it is a 'Read' node
	if (len(nuke.selectedNodes()) == 1) and (nuke.selectedNode().Class() == 'Read'):
	        read = nuke.selectedNode()
	
			#attaches a 'Shuffle' node with the 'alpha' knob set to 'white'
			#'Reduce Noise v4' expects a solid alpha channel
        	shuffle = nuke.createNode("Shuffle")
	        shuffle.knob('red').setValue('red')
	        shuffle.knob('green').setValue('green')
        	shuffle.knob('blue').setValue('blue')
        	shuffle.knob('alpha').setValue('white')

			#attaches a 'Reduce Noise v4' node
        	reduce_noise_v4 = nuke.createNode("Reduce Noise v4")
        	#reduce_noise_v4.knob('Prepare_Profile...').execute()

			#captures the value of the 'Read' node's 'file' knob and alters it to point to the current shot's 'CMP' directory
        	read_dir = os.path.split(read.knob('file').getValue())
        	footage_dir = os.path.split(read_dir[0])
        	plates_dir = os.path.split(footage_dir[0])
        	cmp_dir = os.path.split(plates_dir[0])[0]
        
        	fileName = str(os.path.splitext(os.path.splitext(read_dir[1])[0])[0]) + '_denoise'
        	fileName = os.path.join(cmp_dir, 'Precomps', 'denoise', str(fileName), str(fileName) + '.%04d.exr')

			#attaches a 'Write' node
        	write = nuke.createNode("Write")
        	write.knob('file').setValue(fileName)
        	write.knob('colorspace').setValue('linear')
        	write.knob('file_type').setValue('exr')
        	write.knob('compression').setValue('PIZ Wavelet (32 scanlines)')
        	write.knob('create_directories').setValue(1)
#toolbar = nuke.menu("Nodes")
#toolbar.addCommand('auto_denoise', 'auto_denoise_v01.auto_denoise()', icon='')
#nuke.menu('Nuke').addCommand('auto_denoise','auto_denoise_v01.auto_denoise()', icon='')
#import auto_denoise_v01