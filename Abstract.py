from abc import ABC, abstractmethod
class Movie(ABC):

    @abstractmethod
    def show_genre(self):
        pass

class Leo(Movie):
    def show_genre(self):
        print("Naan tha da Leo, Leo Das")

class Amaran(Movie):
    def show_genre(self):
        print("Amaran is a SK's movie")

m1 = Leo()
m2 = Amaran()

m1.show_genre()
m2.show_genre()
