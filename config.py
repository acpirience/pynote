import glob
import tomllib

from loguru import logger


class Config:
    def __init__(self) -> None:
        self.toml: dict
        self.student_list: list[str]
        self.get_toml_config()

    def get_toml_config(self) -> None:
        logger.info("Loading config")
        with open("config.toml") as fileObj:
            content = fileObj.read()
            self.toml = tomllib.loads(content)

        logger.info("Loading datafile list")
        datafile_list: list[str] = glob.glob(
            f"{self.toml["data"]["notes_dir"]}"
            f"{self.toml["data"]["datafile_prefix"]}"
            f"*{self.toml["data"]["datafile_suffix"]}"
        )

        self.student_list = [
            x.removeprefix(self.toml["data"]["notes_dir"])
            .removeprefix(self.toml["data"]["datafile_prefix"])
            .removesuffix(self.toml["data"]["datafile_suffix"])
            for x in datafile_list
        ]
