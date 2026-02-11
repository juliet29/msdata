from cyclopts import App
from utils4plans import logconfig

from msdata.paths import DynamicPaths

from loguru import logger

from msdata.summary.main import create_dataframe


# from polyfix.cli.studies.main import studies_app

# TODO: clean up imports to clean up project structure

app = App()


@app.command()
def welcome():
    return "Welcome to msdata"


########### --------- BEGIN TESTS ------------


@app.command()
def try_read_plan():
    root_path = DynamicPaths.case_data
    df = create_dataframe(root_path)
    return df
    # cr = CaseReader(6210, root_path)
    # res = cr.get_summary()
    # # res = read_layout_to_simple_layout(path)
    # # res = read_layout_from_path(path)
    logger.debug()
    # logger.debug(res.domains[0].polygon)


######### ----------------- END TESTS -----------


def main():
    logconfig.logset(to_stderr=True)
    app()


if __name__ == "__main__":
    main()
