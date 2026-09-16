from datetime import datetime, timedelta



def current_time():
    """
    Returns the current time in host's timezone.
    """

    return datetime.now().astimezone().time().replace(microsecond=0).isoformat()


def current_date():
    """
    Returns the current date in host's timezone.
    """
    return datetime.now().astimezone().date().isoformat()



if __name__ == "__main__":
    print(f"Current time: {current_time()}")