import time

def loading() :
  print("|              _|         ____________ ")
  time.sleep(0.25)
  print("|            _|          |            |")
  time.sleep(0.25)
  print("|          _|            |            |")
  time.sleep(0.25)
  print("|        _|              |            |")
  time.sleep(0.25)
  print("|      _|                |            |")
  time.sleep(0.25)
  print("|    _|                  |            |")
  time.sleep(0.25)
  print("|  _|                    |            |")
  time.sleep(0.25)
  print("|_|                      |            |")
  time.sleep(0.25)
  print("|_                       |------------|")
  time.sleep(0.25)
  print("| |_                     |            |")
  time.sleep(0.25)
  print("|   |_                   |            |")
  time.sleep(0.25)
  print("|     |_                 |            |")
  time.sleep(0.25)
  print("|       |_               |            |")
  time.sleep(0.25)
  print("|         |_             |            |")
  time.sleep(0.25)
  print("|           |_           |            |")
  time.sleep(0.25)
  print("|             |_         |            |")
  time.sleep(0.25)
  print("|               |        |            |")
  time.sleep(2)
  print("\n"*10000)
  loading_in_percentage = 0
  while loading_in_percentage != 100:
    print("Loading... " + str(loading_in_percentage) + "% Complete")
    loading_in_percentage = loading_in_percentage + 1
    time.sleep(0.05)
    print("\n"*1000)
  print("Loading Complete!\nEntering Game...")


if __name__ == "__main__":
  loading()