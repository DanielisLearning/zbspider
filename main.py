from zbspider import ZBSpider
from config import Config


def main():
    zbs = ZBSpider(Config)
    zbs.run()


if __name__ == '__main__':
    main()