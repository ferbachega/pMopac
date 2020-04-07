#!/usr/bin/env python
text1 = """
#
#
#
#
#
#
#
#                         ---- pMopac %s ----
#
#
#       Copyright 2012 Jose Fernando R Bachega  <ferbachega@gmail.com>
#
#               visit: https://sites.google.com/site/EasyHybrid/
#
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#
#   pMopac team:
#   - Jose Fernando R Bachega   - Universidade Federal de Ciencias da Saude de Porto Alegre - RS, Brazil
#
""" % ('0.1')


#texto_d1 = "\n\n                       -- simple-distance --\n\nFor simple-distance, select two atoms in pymol using the editing mode\nfollowing the diagram:\n\n   R                    R\n    \                  /\n     A1--A2  . . . . A3\n    /                  \ \n   R                    R\n         ^            ^\n         |            |\n        pk1  . . . . pk2\n                d1\n"
#texto_d2d1 = "\n                       -- multiple-distance --\n\nFor multiple-distance, select three atoms in pymol using the editing mode\nfollowing the diagram:\n\n   R                    R\n    \                  /\n     A1--A2  . . . . A3\n    /                  \ \n   R                    R\n     ^   ^            ^\n     |   |            |\n    pk1-pk2  . . . . pk3\n       d1       d2\n"

#
#dialog_text = {
#    'error_topologies/Parameters': "Error: the topology, parameters or coordinates do not match the system type: ",
#    'error_coordiantes': "Error: the coordinates do not match the loaded system.",
#    'error_trajectory': "Error: the trajectory does not match the loaded system.",
#    'delete': "Delete memory system.",
#    'prune': "Warning: this is an irreversible process. Do you want to continue?",
#    'qc_region': "Warning: no quantum region has been defined. Would you like to put all atoms in the quantum region?",
#    'delete2': "Warning: there is a system loaded in memory. Are you sure that you want to delete it?"
#}
##



# System
import datetime
import time
import sys
import glob
import math
import os
import threading
import gi

#-----------------------------------------------------------------------
import pymol
from pymol import *
from pymol.cgo import *
#-----------------------------------------------------------------------

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class pMopacMain:
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		
		self.builder = Gtk.Builder()
		self.builder.add_from_file("Mainwindow.glade")
		#self.builder.connect_signals(Handler())
		
		self.win = self.builder.get_object("window1")
		self.win.show_all()
		#self.win = Gtk.Window()
		#self.win.connect("destroy", Gtk.main_quit)
		#self.win.show_all()

		#self.button = Gtk.Button(label="Click Here")
		#self.button.connect("clicked", self.on_button_clicked)
		#self.win.add(self.button)
		#self.win.connect("destroy", Gtk.main_quit)
		#self.win.show_all()
		Gtk.main()

	def on_button_clicked(self, widget):
		print("Hello World")
		pymol.cmd.load('/home/fernando/QC_atoms.pdb')



pymol.finish_launching()                                #
#Gtk.gdk.threads_init()

print "Creating object"
pMopacMain = pMopacMain()
#pMopacMain.PyMOL_initialize()
#EasyHybrid.run()

