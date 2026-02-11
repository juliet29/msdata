import kagglehub
import polars as pl
from dataframely import LazyFrame
from kagglehub import KaggleDatasetAdapter

from msdata.access.interfaces import MSDSchema


SEED = 1023454


def access_dataset() -> LazyFrame[MSDSchema]:
    file_path = "mds_V2_5.372k.csv"

    lf = kagglehub.dataset_load(
        KaggleDatasetAdapter.POLARS,
        "caspervanengelenburg/modified-swiss-dwellings",
        file_path,
    )

    return MSDSchema.cast(lf)


def access_one_sample_dataset(unit_id: float) -> LazyFrame[MSDSchema]:
    print(f"Sampled ID: {unit_id}")
    # TODO: check that id is in valid ids..
    res = access_dataset().filter(pl.col("unit_id") == unit_id)
    return MSDSchema.cast(res)
