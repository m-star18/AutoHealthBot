import time

import schedule

from src.const import JOB_TIME
from src.job import AutoHealthJob


def main():
    job = AutoHealthJob()
    schedule.every().day.at(JOB_TIME).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
