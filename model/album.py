from dataclasses import dataclass
@dataclass
class Album():
    id: int
    title: str
    artist_id: int
    duration: int


    def __str__(self):
        return f"{self.title} by {self.artist_id}"

    def __repr__(self):
        return f"{self.title} by {self.artist_id}"

    def __hash__(self):
        return hash(self.id)

