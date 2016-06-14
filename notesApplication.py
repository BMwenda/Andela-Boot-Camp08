#Notes taking app assignment

class NotesApplication(object):
	def __init__(self,author,notes):
		self.author=author
		self.notes=notes

	def getAuthor(self):
		return self.author

	def getNotes(self):
		return self.notes

	def create(self,note_content):
		self.notes=self.notes.append(note_content)

	def myList(self):
		print(self.notes)

	def get(self,note_id):
		print(self.notes[note_id])

	#def search(self,search_text):

	#def edit(self,note_id,new_content):

note1=NotesApplication("Banks","kisa")
print(note1.getAuthor())
print(note1.getNotes())