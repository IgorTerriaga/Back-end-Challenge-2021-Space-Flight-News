import getpass
from crontab import CronTab

username = getpass.getuser()
cron = CronTab(user=f'{username}')

job = cron.new(
    command=f"python3 /home/{username}/Documents/projetos/BackEndChallengeSpaceFlight/populate.py",
    comment="Esse CRON tem por objetivo sincronização das base de dados",
)


job.setall('0 9 * * *')
cron.write()
job.enable()