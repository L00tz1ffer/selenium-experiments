import browserController



driver = browserController.getDriver()
driver1 = browserController.getDriver()

i = 0
timeframe = 25
while i<10:
    i = i+1


    browserController.searchByGoogle(driver,"test nummer " + str(i * 6),timeframe)
    browserController.searchByDuckDuckGo(driver1,"test nummer " + str(i * 6),timeframe)

    print("test successful")

browserController.killDriver(driver)
browserController.killDriver(driver1)