import glob
import tomllib

from loguru import logger


def main() -> None:
    logger.info("Starting Pynote")
    logger.info("Loading config")
    with open("config.toml") as fileObj:
        content = fileObj.read()
        config = tomllib.loads(content)

    logger.info("Loading datafile list")
    datafile_list: list[str] = glob.glob(
        f"{config["data"]["notes_dir"]}"
        f"{config["data"]["datafile_prefix"]}"
        f"*{config["data"]["datafile_suffix"]}"
    )

    student_list = [
        x.removeprefix(config["data"]["notes_dir"])
        .removeprefix(config["data"]["datafile_prefix"])
        .removesuffix(config["data"]["datafile_suffix"])
        for x in datafile_list
    ]
    logger.info(f"Student list:{student_list}")


if __name__ == "__main__":
    main()
