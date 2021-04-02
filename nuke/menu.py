#from widgets import NUKE_pathConverter_v02
from widgets import MFX_evTable_v01
from widgets import hub
import os
import nuke

p = os.path.dirname(os.path.realpath(__file__))

#creates a new 'menu' object, named 'MercadoFX Tools,' and places it within the existing 'Nodes' toolbar
toolbar = nuke.toolbar('Nodes')
mFX_menu = toolbar.addMenu('MercadoFX Tools', icon=p + '/widgets/images/mercadofx-logo-gray-64.png')
hub_menu = toolbar.addMenu('hub')

#uses 'addCommand()' function to create commands, or buttons, within the menu items created previously

img = mFX_menu.addMenu('Image', icon=':qrc/images/ToolbarImage.png')
img.addCommand('Marcie')
img.addCommand('Lena')
img.addCommand('Mandril')

drw = mFX_menu.addMenu('Draw', icon=':qrc/images/ToolbarDraw.png')
drw.addCommand('MFX Grain_v001', "nuke.createNode('mfx_Grain_v001.gizmo')")

clr = mFX_menu.addMenu('Color', icon=':qrc/images/ToolbarColor.png')
mth = clr.addMenu('Math')
mth.addCommand('Additive Inverse', "nuke.createNode('additive_inverse.gizmo')")
mth.addCommand('I\/O Graph', "nuke.createNode('io_graph.gizmo')")
mth.addCommand('Multiplicative Inverse', "nuke.createNode('multiplicative_inverse.gizmo')")
clr.addCommand('Contrast', "nuke.createNode('contrast.gizmo')")
clr.addCommand('MFX Grade', "nuke.createNode('mfx_grade.gizmo')")
clr.addCommand('Saturation', "nuke.createNode('saturation.gizmo')")
clr.addCommand('Toe', "nuke.createNode('toe.gizmo')")

flt = mFX_menu.addMenu('Filter', icon=':qrc/images/ToolbarFilter.png')
flt.addCommand('Chroma Blur', "nuke.createNode('chroma_blur.gizmo')")
flt.addCommand('Color Dilate', "nuke.createNode('color_dilate.gizmo')")
flt.addCommand('Faux Albedo', "nuke.createNode('faux_albedo.gizmo')")

key = mFX_menu.addMenu('Keyer', icon=':qrc/images/ToolbarKeyer.png')
key.addCommand('Additive Keyer', "nuke.createNode('additive_keyer.gizmo')")
key.addCommand('Color Difference Keyer', "nuke.createNode('color_difference_keyer.gizmo')")
key.addCommand('Multiplicative Keyer', "nuke.createNode('multiplicative_keyer.gizmo')")
key.addCommand('MFX IBKColorV3_v001', "nuke.createNode('mfx_ibkColourV3_v001.gizmo')")
key.addCommand('Screen Leveling', "nuke.createNode('screen_leveling.gizmo')")

mrg = mFX_menu.addMenu('Merge', icon=':qrc/images/ToolbarMerge.png')
mrg.addCommand('Advanced Merge', "nuke.createNode('advance_merge.gizmo')")
mrg.addCommand('ID Mattes', "nuke.createNode('mattes_v02.gizmo')")

trn = mFX_menu.addMenu('Transform', icon=':qrc/images/ToolbarTransform.png')
trn.addCommand('MFX CornerPin2D_v001', "nuke.createNode('mfx_CornerPin2D_v001.gizmo')")
trn.addCommand('LensDistortion[L]', "nuke.createNode('LensDistortionL.gizmo')")
trn.addCommand('MFX Tracker_v001', "nuke.createNode('mfx_Tracker_v001.gizmo')")

mFX_menu.addCommand('Path Converter', 'NUKE_pathConverter_v02.create_pathConverter_window()')
mFX_menu.addCommand('EV Table', 'MFX_evTable_v01.create_window()')
#hub_menu.addCommand('Hub', 'hub.create_hub_window()')