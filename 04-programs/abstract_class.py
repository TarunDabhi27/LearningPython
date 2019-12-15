from abc import ABC, abstractmethod
#ABC = Abstract Base Class

class DocumentWriter(ABC):
    
    def __init__(self, document_path):
        self.document_path = document_path
        
    @abstractmethod
    def print_document(self):
        pass
#         raise NotImplementedError("Sub class must implement this method")

    def save_document(self):
        print("Saving Document")
        
class SimpleDocumentWriter(DocumentWriter):
    def __init__(self,document_path):
        DocumentWriter.__init__(self, document_path=document_path)
        
    def print_document(self):
        print("Printing document")
        
if __name__ == '__main__':
    o = DocumentWriter("d")
    obj = SimpleDocumentWriter("D:\input.txt")
    obj.print_document()