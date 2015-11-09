class Main():
	def __init__ (self):
		self.view = View()
		self.model = Model()
		self.controller = Controller(self.view, self.controller)

		self.view.intialize(self.controller)