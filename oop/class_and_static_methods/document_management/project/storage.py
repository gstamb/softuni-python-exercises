from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []
        self.category_lookup = {}
        self.topic_lookup = {}
        self.document_lookup = {}

    def add_category(self, category: Category):
        if category.id not in self.category_lookup:
            self.category_lookup[category.id] = len(self.categories)
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic.id not in self.topic_lookup:
            self.topic_lookup[topic.id] = len(self.topics)
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document.id not in self.document_lookup:
            self.document_lookup[document.id] = len(self.documents)
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        if category_id in self.category_lookup:
            category = self.categories[self.category_lookup[category_id]]
            category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        if topic_id in self.topic_lookup:
            topic = self.topics[self.topic_lookup[topic_id]]
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        if document_id in self.document_lookup:
            document = self.documents[self.document_lookup[document_id]]
            document.file_name = new_file_name

    def delete_category(self, category_id):
        if category_id in self.category_lookup:
            self.categories.pop(self.category_lookup[category_id])
            del self.category_lookup[category_id]

    def delete_topic(self, topic_id):
        if topic_id in self.topic_lookup:
            self.topics.pop(self.topic_lookup[topic_id])
            del self.topic_lookup[topic_id]

    def delete_document(self, document_id):
        if document_id in self.document_lookup:
            self.documents.pop(self.document_lookup[document_id])
            del self.document_lookup[document_id]

    def get_document(self, document_id):
        if document_id in self.document_lookup:
            return self.documents[self.document_lookup[document_id]]

    def __repr__(self):
        return "\n".join([str(document) for document in self.documents])
