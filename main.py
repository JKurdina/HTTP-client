import logging
import toml
from parse import parse_args
from send_sms import send_sms

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="sms_client.log",
    filemode="a",
)

logger = logging.getLogger(__name__)


def main():

    with open("config.toml", "r") as f:
        config = toml.load(f)

    args = parse_args()
    logger.info(f"Переданные аргументы: {args}")

    send_sms(config, args.fr, args.t, args.text)


if __name__ == "__main__":
    main()
