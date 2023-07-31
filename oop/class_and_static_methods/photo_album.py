import itertools
from math import ceil
from collections import deque


class PhotoAlbum:
    photos_per_page = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = PhotoAlbum.get_album_layout(pages)
        self.pictures_queue = deque(itertools.product(range(self.pages), range(PhotoAlbum.photos_per_page)))

    @staticmethod
    def get_album_layout(pages):
        return [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photo_count: int):
        pages = ceil(photo_count / cls.photos_per_page)
        return cls(pages)

    def add_photo(self, picture):
        if self.pictures_queue:
            page_index, picture_index = self.pictures_queue.popleft()
            self.photos[page_index].append(picture)
            return f"{picture} photo added successfully on page {page_index + 1} slot {picture_index + 1}"
        else:
            return "No more free slots"

    def display(self):
        display_info = ""
        for page in self.photos:
            picture_representation = " ".join("[ ]" for _ in page)
            display_info += f"{picture_representation}\n" + "-" * 11 + "\n"
        return display_info
