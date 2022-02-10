from crontab import CronTab
cron = CronTab(user=True)

job = cron.new(
    command="py populate.py",
    comment="Esse CRON tem por objetivo sincronização das base de dados",
)


work = job.minute.every(1)
cron.write()
job.enable()
