from song import Song


class Album:
    def __init__(self, name: str, *args):
        self.name = name
        self.published = False
        self.songs = {}

        for arg in args:
            self.songs[arg.username] = arg

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.name in self.songs:
            return "Song is already in the album."
        else:
            self.songs[song.name] = song
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        if song_name in self.songs:
            del self.songs[song_name]
            return f"Removed song {song_name} from album {self.name}."
        else:
            return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        details_info = f"Album {self.name}\n"
        for _, obj in self.songs.items():
            details_info += f"== {obj.get_info()}\n"

        return details_info


if __name__ == "__main__":
    pass