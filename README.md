# msdata

- The unit ids of the ~5000 valid cases can be found in [static/\_04_temp/msd_stats/valid_ids.csv](https://github.com/juliet29/msdata/blob/main/static/_04_temp/msd_stats/valid_ids.csv).

- Results from "processing" the first 50 valid cases are in [static/\_04_temp/snakemake/0_50](https://github.com/juliet29/msdata/tree/main/static/_04_temp/snakemake/0_50).
- The folder name is the unit id. Each folder contains results for each step of the process. The folder structure and order is given below.
  <unit_id>/
  ├── layout/
  │ └── out.json
  ├── rotate/
  │ ├── out.json
  │ ├── in.png
  │ └── out.png
  ├── ortho/
  │ ├── out.json
  │ └── out.png
  ├── simplify /
  │ ├── out.json
  │ └── out.png
  ├── xplan /
  │ ├── out.json
  │ └── out.png
  ├── xmove /
  │ ├── out.json
  │ └── out.png
  ├── yplan /
  │ ├── out.json
  │ └── out.png
  └── ymove/
  ├── out.json
  └── out.png
