import threading
from queue import Queue
from spider import Spider
from domain import *
from General import *

PROJECT_NAME = 'Arteezy'
HOMEPAGE = 'http://dotamax.com/player/match/86745912/?skill=pro'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + "/queue.txt"
CRAWLED_FILE = PROJECT_NAME + "/crawled.txt"
NUMBER_OF_SPIDERS = 8

queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

#  Create Spider threads, will die when main exists
def create_spiders():
    for _ in range(NUMBER_OF_SPIDERS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

# Each queued link is a new job
def create_jobs():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


# Check if there are items in queue, if so crawl them
def crawl():
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0:
        print(str(len(queue_links)) + " links left in the queue")
        create_jobs()



create_spiders()
crawl()
