import datetime

#Store Next avilable id for all new notes
last_id = 0

class Note:
    '''
    Initialize `Note`(Class)
    
    '''
    def __init__(self, memo, tags=''):
        '''

        parameter
        ---------
        
        memo : str
            the string for note.
        tags : str
            for quick query in memo.
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today
        global last_id
        last_id += 1
        self.id =last_id
    
    def get_match(self,filter):
        '''
        To get match in memo and tags of Note.
        '''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''
    represent collection of notes that can 
    be tagged and modified and searched.
    '''
    def __init__(self):
        '''
        initialize NoteBook with notes
        '''
        self.notes = []
        
    def new_note(self,memo,tags=''):
        self.notes.append(Note(memo,tags))
    
    def modify_memo(self,note_id,memo):
        for note in self.notes:
            if note.id == note_id:
                note.memo =  memo
                break

    def _find_note(self,note_id):
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_tags(self,note_id,tags):
        self._find_note(note_id).tags = tags

    def search(self,filter):
        return [
            note for note in self.notes if note.get_match(filter)
        ]

