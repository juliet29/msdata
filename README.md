# msdata

## Installing

This repo can be cloned. Packaging is handled with the [uv](https://docs.astral.sh/uv/) package manager. Assuming uv is installed, running `uv sync` will create a local virtual environment with the dependencies needed to execute the code in this repo.

## Process results

The unit ids of the ~5000 valid cases can be found in [static/\_04_temp/msd_stats/valid_ids.csv](https://github.com/juliet29/msdata/blob/main/static/_04_temp/msd_stats/valid_ids.csv).

Results from "processing" the first 50 valid cases are in [static/\_04_temp/snakemake/0_50](https://github.com/juliet29/msdata/tree/main/static/_04_temp/snakemake/0_50).

The folder name is the unit id for a plan. Each folder contains results for each step of the process. The order of operations is:

1. layout: the original floorplan
2. rotate: the first step in the modification process - this folder contains images of the floorplan before and after rotation
3. ortho: after orthogonalizing - essentially, trying to create polygons with only right angles - this is the stage at which many plans fail
4. simplify: removing extraneous geometry and small bends that make it harder to adjust the plan
5. xplan: plan moves in the x-direction
6. xmove: perform the move in the x-direction
7. yplan: plan moves in the y-direction
8. ymove: perform the move in the y-direction - this is the final transformation

## Summaries

Condensed versions of the process data for each plan is available in [static/\_04_temp/summary/0_50](https://github.com/juliet29/msdata/tree/main/static/_04_temp/summary/0_50). The geometry is stored using Shapely's [well-known text format](https://shapely.readthedocs.io/en/2.1.2/reference/shapely.to_wkt.html). The data can be read in as a Python object using the function `read_summary` located in the [summary/main.py](https://github.com/juliet29/msdata/blob/main/src/msdata/summary/main.py).

## Helper functions

Other helper functions are available in [cli/main.py](https://github.com/juliet29/msdata/blob/main/src/msdata/cli/main.py), and can be run from the command line by calling `uv run msdata <name-of-function>` (underscores become hyphens).

Importantly, the original data from the MSD dataframe can be accessed by calling `uv run msdata access-unit <unit-id-number>`.
