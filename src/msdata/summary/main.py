from attr import dataclass
from polyfix.geometry.layout import Layout
from polyfix.geometry.ortho import FancyOrthoDomain
import shapely as sp

from polyfix.pydantic_models import read_layout_from_path
from pathlib import Path
from pydantic import BaseModel
from utils4plans.io import read_json, write_json


class SimpleRoom(BaseModel):
    name: str
    shapely_wkt: str

    @classmethod
    def from_polyfix_domain(cls, domain: FancyOrthoDomain):
        return cls(name=domain.name, shapely_wkt=sp.to_wkt(domain.polygon))


class SimpleLayout(BaseModel):
    rooms: list[SimpleRoom]

    @classmethod
    def from_polyfix_layout(cls, layout: Layout):
        return cls(rooms=[SimpleRoom.from_polyfix_domain(i) for i in layout.domains])


def read_layout_to_simple_layout(path: Path):
    # TODO: handle path doesnt exist..
    if not path.exists():
        return SimpleLayout(rooms=[])
    res = read_layout_from_path(path)
    return SimpleLayout.from_polyfix_layout(res)


class CaseSummary(BaseModel):
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
            unit_id=self.unit_id,
            original=self.get_original(),
            rotate=self.get_rotate(),
            ortho=self.get_ortho(),
            simplify=self.get_simplify(),
            xmove=self.get_xmove(),
            ymove=self.get_ymove(),
        )


def create_summaries(root_path: Path):
    ids = [i.name for i in root_path.iterdir() if i.is_dir()]
    summaries = [CaseReader(id, root_path).get_summary() for id in ids]
    return summaries


def write_summaries(root_path: Path, out_path: Path):
    summaries = create_summaries(root_path)
    for summary in summaries:
        write_json(
            summary.model_dump(),
            out_path / f"{str(summary.unit_id)}.json",
            OVERWRITE=True,
        )


def read_summary(path: Path):
    data = read_json(path)
    res = CaseSummary(**data)
    return res
