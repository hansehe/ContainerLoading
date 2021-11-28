from pydantic import BaseModel

class ItemModel(BaseModel):
    x0: int = 0
    y0: int = 0
    z0: int = 0
    length: int
    width: int
    height: int
    weight: int

    @property
    def volume(self) -> int:
        return self.length * self.width * self.height
