from cyclopts import App
from utils4plans import logconfig

from msdata.access.main import access_one_sample_dataset
from msdata.paths import DynamicPaths


from msdata.summary.main import create_summaries, read_summary, write_summaries


app = App()


@app.command()
def welcome():
    return "Welcome to msdata"


########### --------- BEGIN HELPER FUNCTIONS ------------


@app.command()
def read_all_summaries():
    root_path = DynamicPaths.case_data
    df = create_summaries(root_path)
    return df


@app.command()
def write_all_summaries():
    write_summaries(DynamicPaths.case_data, DynamicPaths.summary_data)


@app.command()
def read_summary_from_json(case: str):
    return read_summary(DynamicPaths.summary_data / f"{case}.json")


@app.command()
def access_unit(case_num: float = 5013, areas_only: bool = True):
    res = access_one_sample_dataset(case_num, areas_only=areas_only)
    return res


######### ----------------- END HELPER FUNCTIONS -----------


def main():
    logconfig.logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()
