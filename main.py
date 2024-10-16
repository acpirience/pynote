from loguru import logger

from config import Config


def main() -> None:
    logger.info("Starting Pynote")
    myconfig = Config()

    logger.info(myconfig.toml)
    logger.info(myconfig.student_list)


if __name__ == "__main__":
    main()
