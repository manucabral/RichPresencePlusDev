import rpp

log = rpp.get_logger("ExampleModule.module1")


def say_hello_module1():
    log.info("Hello from module1")
