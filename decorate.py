def announce(f):
    def wrapper():
        print("About to start executing...")
        f()
        print("Execution over")
    return wrapper

@announce
def Hello():
    print("Hello,World")


Hello()