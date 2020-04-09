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

people = [("Bucky Roberts", 67, "Exotic Dancer"),
          ("Jenny Blue", 21, "Shepherd"),
          ("John Smith", 55, "Programmer"),
          ("Emma Anderson", 43, "Nurse"),
          ("Emily Wilson", 28, "Teacher")]



class Handler:
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		pass

	def print_aqui  (self, widget):
		""" Function doc """
		print('aqui')



class MopacObject:
    """ Class doc """

    def __init__ (self):
	""" Class initialiser """
	#pass
	self.mopacPath = '/opt/mopac/MOPAC2016.exe'
	
	self.parameters = {}
	
	self.atoms = []
	self.fixed = []
	self.fixed_idx = []
	self.coords = []
	
    
    
    def load_mop (self, inputfile):
	""" Function doc """
	mopfile = open(inputfile, 'r')
	for line in mopfile:
	    print line
	
	
	

class MopacProject:
    """ Class doc """

    def __init__ (self):
	""" Class initialiser """
	pass
	self.counter       = 0
	self.index         = []
	self.atoms         = []
	self.coords        = []
	self.coords_fixed  = []

	
    def energy (self):
	""" Function doc """
	print 'Energy'

		


class pMopacMain:
    """ Class doc """

    def __init__ (self):
	""" Class initialiser """

	self.builder = Gtk.Builder()
	self.builder.add_from_file("Mainwindow.glade")
	self.builder.connect_signals(self)

	#self.toolbar = self.builder.get_object("toolbar")
	#self.win.show_all()
	self.win = self.builder.get_object("window1")
	#self.win.connect("destroy", Gtk.main_quit)
	#self.win.show_all()
	#self.win.add(self.toolbar)

	self.layout = self.builder.get_object("mainlayout")
	
	
	
	
	# convert to liststore
	self.people = Gtk.ListStore(str, int, str)
	for item in people:
		self.people.append(list(item))

	# como acessar a liststore 
	#for row in self.people: 
	#	print (row[:])

	#treeview 
	self.treeview = Gtk.TreeView(self.people)
	#self.treeview.connect("select-cursor-row", self.print_aqui)
	#self.treeview.connect("row-activated", self.print_aqui)
	#self.treeview.connect("cursor-changed", self.print_aqui)

	for i, col_title in enumerate(['name', 'Age', 'prof']):
	    print i, col_title
	    renderer  = Gtk.CellRendererText()
	    renderer.set_property("editable", True)
	    #renderer.connect("edited", self.text_edited)
	    column    = Gtk.TreeViewColumn(col_title, renderer, text = i)
	    self.treeview.append_column(column)
	self.layout.pack_start(self.treeview, True, True, 0)
	
	
	
	
	
	
	
	
	
	
	
	
	self.statusbar = Gtk.Statusbar()
	self.layout.pack_start(self.statusbar, True, True, 0)
	self.statusbar.push(1, "You clicked the button.")


	#self.button = Gtk.Button(label="Click Here")
	#self.button.connect("clicked", self.on_button_clicked)
	#self.win.add(self.button)
	self.win.connect("destroy", Gtk.main_quit)
	self.win.show_all()
	Gtk.main()


    def open_file (self, widget):
	""" Function doc """
	chooser = Gtk.FileChooserDialog("Please choose a file", self.win,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
	#self.add_filters(dialog)
	filter = Gtk.FileFilter()  
	filter.set_name("Mopac input - *.mop")
	#
	filter.add_mime_type("Mopac input files")
	filter.add_pattern("*.mop")
	#
	chooser.add_filter(filter)
	filter = Gtk.FileFilter()
	filter.set_name("Mopac aux - *.aux")
	filter.add_pattern("*.aux")
	#
	#
	chooser.add_filter(filter)
	filter = Gtk.FileFilter()
	filter.set_name("Mopac output  - *.out")
	filter.add_pattern("*.out")
	#
	chooser.add_filter(filter)
	filter = Gtk.FileFilter()
	filter.set_name("Mopac output  - *.out")
	filter.add_pattern("*.out")
	#
	
	chooser.add_filter(filter)
	filter = Gtk.FileFilter()
	filter.set_name("All files")
	filter.add_pattern("*")
	#
	chooser.add_filter(filter)  
	# chooser.set_current_folder(data_path)

	response = chooser.run()
	
	if response == Gtk.ResponseType.OK:
	    #print("Open clicked")
	    #print("File selected: " + chooser.get_filename())
	    selectedFile = chooser.get_filename()
	    what_type = selectedFile.split('.')
	    _type = what_type[-1]
	    if _type in ['mop', 'inp']:
		_buffer = self.load_mop (selectedFile)
		print _buffer
	    
	    
	    
	elif response == Gtk.ResponseType.CANCEL:
	    print("Cancel clicked")
	chooser.destroy()

    
    def on_button_clicked(self, widget):
	print("Hello World")
	pymol.cmd.load('sug1_B3_test.pdb')
	self.statusbar.push(0, "sug1_B3_test.pdb")

    def load_mop (self, inputfile):
	""" Function doc 
	* ===============================
	* Input file for Mopac
	* ===============================
	PM7 XYZ    CHARGE=0 Singlet  BONDS AUX 

	Mopac file generated by Gabedit
	C  0.3500  1 -0.1550  1 -0.2600  1
	C  -0.1410  1 0.9590  1 -1.1410  1
	C  0.4230  1 2.1170  1 -0.8110  1
	"""
	_buffer = []
	mopfile = open(inputfile, 'r')
	
	mopac_project = MopacProject()
	
	lines = mopfile.readlines()
	
	for line in lines:
	    print line
	    
	    line2 = line.split()
	    #print line2
	    
	    try:
		atom    = str  (line2[0])
		x       = float(line2[1])
		x_fixed = int  (line2[2])
		y       = float(line2[3])
		y_fixed = int  (line2[4])
		z       = float(line2[5])
		z_fixed = int  (line2[6])		#pass
		mopac_project.atoms       .append(atom)
		mopac_project.coords      .append([x,y,z])
		mopac_project.coords_fixed.append([x_fixed,y_fixed,z_fixed])
	    
	    except:
		pass

	for i, atom in enumerate(mopac_project.atoms):
	    print i, atom, mopac_project.coords[i]
	
	self.from_mopac2pymol(mopac_project)
	
	

    def load_aux (self, inputfile):
	""" Function doc 
	* ===============================
	* Input file for Mopac
	* ===============================
	PM7 XYZ    CHARGE=0 Singlet  BONDS AUX 

	Mopac file generated by Gabedit
	C  0.3500  1 -0.1550  1 -0.2600  1
	C  -0.1410  1 0.9590  1 -1.1410  1
	C  0.4230  1 2.1170  1 -0.8110  1
	"""
	_buffer = []
	mopfile = open(inputfile, 'r')
	
	mopac_project = MopacProject()
	
	lines = mopfile.readlines()
	
	for line in lines:
	    print line
	    
	    line2 = line.split()
	    #print line2
	    
	    try:
		atom    = str  (line2[0])
		x       = float(line2[1])
		x_fixed = int  (line2[2])
		y       = float(line2[3])
		y_fixed = int  (line2[4])
		z       = float(line2[5])
		z_fixed = int  (line2[6])		#pass
		mopac_project.atoms       .append(atom)
		mopac_project.coords      .append([x,y,z])
		mopac_project.coords_fixed.append([x_fixed,y_fixed,z_fixed])
	    
	    except:
		pass

	for i, atom in enumerate(mopac_project.atoms):
	    print i, atom, mopac_project.coords[i]

    
    def export_xyzfile (self, mopac_project):
	""" Function doc """
	tmpfile = open('/home/fernando/temp.xyz', 'w')
	size = len(mopac_project.atoms)
	text =  '{:<100}\n'.format(size)
	text += '\n'
	for i, atom in enumerate(mopac_project.atoms):
	    coords = mopac_project.coords[i]
	    text   += '{:<2}  {:<10}  {:<10}  {:<10}\n'.format( atom, coords[0],coords[1], coords[2] )
	    print i, atom, mopac_project.coords[i]	
	
	tmpfile.write(text)
	
	    
    
    def from_mopac2pymol (self, obj = None, _type = 'xyz'):
	""" Function doc """
	if _type == 'xyz':
	    fileout = self.export_xyzfile ( obj)
	    pymol.cmd.load('/home/fernando/temp.xyz')
	    
	





#win = FileChooserWindow()
#win.connect("destroy", Gtk.main_quit)
#win.show_all()
#Gtk.main()


























pymol.finish_launching()                                #
#Gtk.gdk.threads_init()

print ("Creating object")
pMopacMain = pMopacMain()
#pMopacMain.PyMOL_initialize()
#EasyHybrid.run()

