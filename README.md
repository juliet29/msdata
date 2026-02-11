# msdata

- The unit ids of the ~5000 valid cases can be found in [static/\_04_temp/msd_stats/valid_ids.csv](https://github.com/juliet29/msdata/blob/main/static/_04_temp/msd_stats/valid_ids.csv).

- Results from "processing" the first 50 valid cases are in [static/\_04_temp/snakemake/0_50](https://github.com/juliet29/msdata/tree/main/static/_04_temp/snakemake/0_50).
- The folder name is the unit id. Each folder contains results for each step of the process. The order of operations is:

1. layout: the original floorplan
2. rotate: the first step in the modificaiton process - this folder contains images of the floorplan before and after rotation
3. ortho: after orthogonalizing - essentially, trying to create polygons with only right angles - this is the stage at which many plans fail
4. simplify: removing extraneous geometry and small bends that make it harder to adjust the plan
5. xplan: plan moves in the x-direction
6. xmove: perform the move in the x-direction
7. yplan: plan moves in the y-direction
8. ymove: perform the move in the y-direction
