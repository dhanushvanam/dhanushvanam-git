import time
def start():
    fuel = oxygen = netlink = power = engine = True
    if fuel:
        print("05.FUEL is checked at ",end="")
        localtime = time.localtime()
        result = time.strftime("%I:%M:%S %p", localtime)
        print(result)
        time.sleep(2)
        if oxygen:
            print("04.OXYGEN is checked at ",end="")
            localtime = time.localtime()
            result = time.strftime("%I:%M:%S %p", localtime)
            print(result)
            time.sleep(2)
            if netlink:
                print("03.NETLINK is checked at ",end="")
                localtime = time.localtime()
                result = time.strftime("%I:%M:%S %p", localtime)
                print(result)
                time.sleep(2)
                if power:
                    print("02.POWER is checked at ",end="")
                    localtime = time.localtime()
                    result = time.strftime("%I:%M:%S %p", localtime)
                    print(result)
                    time.sleep(2)
                    if engine:
                        print("01.ENGINE is checked at ",end="")
                        localtime = time.localtime()
                        result = time.strftime("%I:%M:%S %p", localtime)
                        print(result)
                        time.sleep(2)
                        if True:
                            print("LAUNCHING THE ROCKET")
                    else:
                        print("Terminated at Stage 01")
                else:
                    print("Terminated at Stage 02")
            else:
                print("Terminated at Stage 03")
        else:
            print("Terminated at Stage 04")
    else:
        print("Terminated at Stage 05")
opt = input("LAUNCH THE ROCKET(Y/N): ")
if (opt=="Y" or opt=="y"):
    start()
else:
    print("No,don't launch the rocket")
print(time.localtime())
