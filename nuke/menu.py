from widgets import NUKE_pathConverter_v02
from widgets import hub

import nuke

#creates a new 'menu' object, named 'MercadoFX Tools,' and places it within the existing 'Nodes' toolbar
toolbar = nuke.toolbar('Nodes')
mFX_menu = toolbar.addMenu('MercadoFX Tools', icon='./widgets/images/mercadofx-logo-gray-64.png')
hub_menu = toolbar.addMenu('hub')

#uses 'addCommand()' function to create commands, or buttons, within the menu items created previously
mFX_menu.addCommand('Path Converter', 'NUKE_pathConverter_v02.create_pathConverter_window()')
hub_menu.addCommand('Hub', hub.nukeTestWindow().show())

