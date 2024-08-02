from sys import exit
import rpp

if __name__ == "__main__":

    log = rpp.getLogger("Main")
    log.info("Checking for browser...")
    browserId = rpp.getBrowserProgId()
    if not browserId:
        log.info("Browser not found")
        exit()

    log.info(f"Browser found: {browserId}")
    print("Browser tools")
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
    elif res == "3":
        log.info("Opening browser with remote debugging")
        rpp.openRemoteDebuggingPort(9222)
    else:
        log.info("Skipping browser setup")

    runtime = rpp.Runtime(9222)
    main = rpp.Manager(runtime=runtime, dev=True)
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
