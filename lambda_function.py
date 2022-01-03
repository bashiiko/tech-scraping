import scraping_hatena as sc_hatena
import scraping_tech_blog as sc_tech_blog
import os
from slackweb import slackweb

def lambda_handler(event, context):
    results_hatena = sc_hatena.scraping()
    results_blog = sc_tech_blog.scraping()
    notify_slack(results_hatena, os.environ['WEBHOOKURL_HATENA'])
    notify_slack(results_blog, os.environ['WEBHOOKURL_BLOG'])
    
def notify_slack(results, webhook_url):
    slack = slackweb.Slack(url=webhook_url)
    content = "\n".join(results)
    slack.notify(text=content)