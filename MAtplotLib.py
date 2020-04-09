from gi.repository import Gtk

# List of tuples (this is the model, aka the data that will be displayed by the TreeView)
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
		#self.people.append(list(("Emily Wilson", 28, "Teacher")))



class MainWindow(Gtk.Window ):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		Gtk.Window.__init__(self, title = 'people')
		
		self.builder = Gtk.Builder()
		self.builder.add_from_file("Mainwindow.glade")
		self.builder.connect_signals(self)
		
		self.toolbar = self.builder.get_object("toolbar")
		self.layout = Gtk.Box()
		self.button1 = Gtk.Button()
		self.layout.add(self.toolbar)
		self.button2 = Gtk.Button()
		self.layout.add(self.button2)
		self.add(self.layout)
		
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
			renderer.connect("edited", self.text_edited)
			column    = Gtk.TreeViewColumn(col_title, renderer, text = i)
			
			self.treeview.append_column(column)
		
		self.layout.pack_start(self.treeview, True, True, 0)
		
	def print_aqui  (self, widget):
		""" Function doc """
		print('aqui')
		
		self.people.append(list(("Emily Wilson", 28, "Teacher")))

	def text_edited(self, widget, path, text):
		print text
		print self.people[path] 
		self.people[path][0] = text		
        
window =  MainWindow()
window.connect ('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
