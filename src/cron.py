import getpass
from crontab import CronTab
from pathlib import Path


def start_cron():

    username = getpass.getuser()
    print(username)
    print(Path('populate.py').absolute())
    cron = CronTab(user=f"{username}")

    job = cron.new(
        command=f"python3 {Path('populate.py').absolute()}",
        comment="Esse CRON tem por objetivo sincronização das base de dados",
    )

    job.setall("0 9 * * *")
    cron.write()
    job.enable()
