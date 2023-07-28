from album import Album
from song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = {}

    def add_album(self, album: Album):
        if album.name in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums[album.name] = album
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name in self.albums:
            if self.albums[album_name].published:
                return "Album has been published. It cannot be removed."
            else:
                del self.albums[album_name]
                return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        details_info = f"Band {self.name}\n"
        for _, album in self.albums.items():
            details_info += f"{album.details()}\n"
        return details_info


if __name__ == "__main__":
    pass