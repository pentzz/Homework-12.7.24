temp: float = float(input("please enter the temperature: "))
print("temperature is " + ("freezing" if temp < 0 else "normal" if temp < 20 else "hot"))
