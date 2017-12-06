from webdriver_util import init


def query_vecka(keywords):
    print("Loading Firefox driver...")
    driver, waiter, selector, datapath = init()

    print("Fetching vecka.nu front page...")
    driver.get("http://vecka.nu")

    print("Taking a screenshot...")
    waiter.shoot("frontpage")

    print("Get week")
    print("The current week is %s" % selector.get("time").text)


if __name__ == '__main__':
    query_vecka('test')
