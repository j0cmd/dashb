from time import sleep

@medidor_de_tempo
def delay(secs):
    sleep(secs)
    return secs


print(delay(2))
