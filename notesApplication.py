#Programming logic assignment: notes taking app

class NotesApplication(object):
	def __init__(self,author):
		self.author=author
		notes=[]
		self.notes=notes

	def getAuthor(self):
		return self.author

	def getNotes(self):
		return self.notes

	def create(self,note_content):
		self.notes.append(note_content)

	def list(self): #Using function name myList, since list is key word
		for i in self.notes:
			print("Note ID: {0} \n {1}\n".format(self.notes.index(i),i))
			print("By Author {0} \n".format(self.author))

	def get(self,note_id):
		return self.notes[note_id]

	def search(self,search_text):
		for x in notes:
			if search_text in x:
				print("Note ID: {0}\n{1}\n".format(self.notes.index(x),x))
				print("By Author {0}".format(self.author))


	def edit(self,note_id,new_content):
		self.notes[note_id]=new_content

note1=NotesApplication("Banks")
note2=NotesApplication("Bonny")
for i in range(3): #create notes for each author
	note1.create("Text "+str(i))
	note2.create("Some text "+str(i))

note1.list()
note2.list()
