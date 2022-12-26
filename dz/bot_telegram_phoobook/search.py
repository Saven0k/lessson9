import data_recording
import log

def search_data(number , phb):
    if phb[number]:
        log.wr2(f"Человек ищет запись под номером{number}")
        return (phb[number])
    else:
        log.wr("Такой записи не существует")
        return ("Такой записи не существует")

