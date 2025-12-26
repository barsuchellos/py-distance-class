from typing import Self


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Self | int | float) -> Self:
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: Self | int | float) -> Self:
        if isinstance(other, (int, float)):
            self.km += other
            return self

        self.km += other.km
        return self

    def __mul__(self, other: int | float | Self) -> Self:
        if isinstance(other, (int, float)):
            self.km *= other
            return self

        self.km *= other
        return self

    def __truediv__(self, other: int | float | Self) -> Self:
        if isinstance(other, (int, float)):
            self.km = round(self.km / other, 2)
            return self

        self.km = round(self.km / other, 2)
        return self

    def __lt__(self, other: Self | int | float) -> bool:
        if isinstance(other, (int, float)):
            return True if self.km < other else False
        return True if self.km < other.km else False

    def __gt__(self, other: Self) -> bool:
        if isinstance(other, (int, float)):
            return True if self.km > other else False
        return True if self.km > other.km else False

    def __eq__(self, other: Self) -> bool:
        if isinstance(other, (int, float)):
            return True if self.km == other else False
        return True if self.km == other.km else False

    def __le__(self, other: Self) -> bool:
        if isinstance(other, (int, float)):
            return True if self.km <= other else False
        return True if self.km <= other.km else False

    def __ge__(self, other: Self) -> bool:
        if isinstance(other, (int, float)):
            return True if self.km >= other else False
        return True if self.km >= other.km else False
