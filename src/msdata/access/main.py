import kagglehub
import polars as pl
from dataframely import LazyFrame, DataFrame
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


def filter_to_areas(df: LazyFrame[MSDSchema]) -> LazyFrame[MSDSchema]:
    res = df.filter(pl.col("entity_type") == "area")
    return MSDSchema.cast(res)


def access_one_sample_dataset(unit_id: float, areas_only: bool) -> DataFrame[MSDSchema]:
    print(f"Sampled ID: {unit_id}")
    # TODO: check that id is in valid ids..
    if areas_only:
        res = (
            access_dataset().pipe(filter_to_areas).filter(pl.col("unit_id") == unit_id)
        )
    else:
        res = access_dataset().filter(pl.col("unit_id") == unit_id)
    return MSDSchema.cast(res).collect()
