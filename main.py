import logging

logging.basicConfig(
    level=logging.INFO,
    format="[ %(asctime)s ] %(message)s",
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    logger.info("welcome to ml project")
