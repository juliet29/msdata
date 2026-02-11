from attr import dataclass
import polars as pl
from polyfix.geometry.layout import Layout
from typing import NamedTuple
from polyfix.geometry.ortho import FancyOrthoDomain
import shapely as sp

from polyfix.pydantic_models import read_layout_from_path
from pathlib import Path


class SimpleRoom(NamedTuple):
    name: str
    geometry: sp.Polygon

    @classmethod
    def from_polyfix_domain(cls, domain: FancyOrthoDomain):
        return cls(name=domain.name, geometry=domain.polygon)


class SimpleLayout(NamedTuple):
    rooms: list[SimpleRoom]

    @classmethod
    def from_polyfix_layout(cls, layout: Layout):
        return cls([SimpleRoom.from_polyfix_domain(i) for i in layout.domains])


def read_layout_to_simple_layout(path: Path):
    # TODO: handle path doesnt exist..
    if not path.exists():
        return SimpleLayout([])
    res = read_layout_from_path(path)
    return SimpleLayout.from_polyfix_layout(res)


class CaseSummary(NamedTuple):
    unit_id: str | int
    original: SimpleLayout
    rotate: SimpleLayout | None
    ortho: SimpleLayout | None
    simplify: SimpleLayout | None
    xmove: SimpleLayout | None
    ymove: SimpleLayout | None


@dataclass
class CaseReader:
    unit_id: str | int
    root_path: Path

    @property
    def path(self):
        return self.root_path / str(self.unit_id)

    def get(self, name: str):
        return read_layout_to_simple_layout(self.path / name / "out.json")

    def get_original(self):
        return self.get("layout")

    def get_rotate(self):
        return self.get("rotate")

    def get_ortho(self):
        return self.get("ortho")

    def get_simplify(self):
        return self.get("simplify")

    def get_xmove(self):
        return self.get("xmove")

    def get_ymove(self):
        return self.get("ymove")

    def get_summary(self):
        return CaseSummary(
            self.unit_id,
            self.get_original(),
            self.get_rotate(),
            self.get_ortho(),
            self.get_simplify(),
            self.get_xmove(),
            self.get_ymove(),
        )


def create_dataframe(root_path: Path):
    ids = [i.name for i in root_path.iterdir() if i.is_dir()][1:10]
    summaries = [CaseReader(id, root_path).get_summary() for id in ids]
    res = pl.DataFrame(summaries)
    return res

    pass
