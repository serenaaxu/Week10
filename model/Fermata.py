from dataclasses import dataclass


@dataclass # per rappresentare dati
class Fermata():
    _id_fermata : int
    _nome : str

    @property
    def id_fermata(self): # -> int:
        return self._id_fermata

    @property
    def nome(self): # -> str:
        return self._nome

    def __str___(self):
      return f"Fermata: {self._id_fermata} {self.nome}"

    def __hash__(self):
        return hash(self.id_fermata)


