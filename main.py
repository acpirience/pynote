import pprint
import tomllib

from loguru import logger


def main() -> None:
    logger.info("Starting Pynote")
    logger.info("Opening config.toml")
    with open("config.toml") as fileObj:
        content = fileObj.read()
        config = tomllib.loads(content)

    pprint.pprint(config)


if __name__ == "__main__":
    main()
