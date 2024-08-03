from sys import exit
import logging
import rpp


def checkBrowser(log: logging.Logger, browserId: str) -> None:
    """
    Simple check to see if a browser is found

    Args:
        log (logging.Logger): Logger instance
        browserId (str): Browser ID

    Returns:
        None
    """
    log.info("Checking for browser...")
    if not browserId:
        log.info("Browser not found")
        exit()


def browserTools(log: logging.Logger, browserId: str) -> None:
    """
    Browser tools to help with debugging

    Args:
        log (logging.Logger): Logger instance
        browserId (str): Browser ID

    Returns:
        None
    """
    print(f"Browser tools for {browserId}")
    print("1. Close and open browser")
    print("2. Close all browser instances")
    print("3. Open browser with remote debugging")
    print("4. Skip")
    res = input("Choose an option: ")
    if res == "1":
        log.info("Closing and opening browser")
        rpp.killBrowser(rpp.getBrowserProcess(browserId))
        rpp.openRemoteDebuggingPort(9222)
    elif res == "2":
        log.info("Closing all browser instances")
        rpp.killBrowser(rpp.getBrowserProcess(browserId))
        rpp.info("Please restart the application")
        input("Press any key to exit...")
        exit()
    elif res == "3":
        log.info("Opening browser with remote debugging")
        rpp.openRemoteDebuggingPort(9222)
    else:
        log.info("Skipping browser tools")


if __name__ == "__main__":

    log = rpp.getLogger("Main")
    browserId = rpp.getBrowserProgId()
    checkBrowser(log, browserId)
    browserTools(log, browserId)

    runtime = rpp.Runtime(9222)
    main = rpp.Manager(runtime=runtime, dev=False)
    main.load()

    if len(main.presences) == 0:
        log.error("No presences loaded")
        input("Press any key to exit...")
        exit()
    if not main.validate_presences():
        log.error("Presences failed validation")
        input("Press any key to exit...")
        exit()

    log.info(f"Loaded a total of {len(main.presences)} presence/s")
    main.start()
