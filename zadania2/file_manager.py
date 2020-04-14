
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def read_file(self):
        try:
            plik = open(self.file_name)
            zawartosc = plik.read()
            plik.close()
        except:
            return 'Nie można odczytać pliku'

        return zawartosc

    def update_file(self, text_data):
        try:
            plik = open(self.file_name, 'a')
            plik.write(text_data)
            plik.close()
        except:
            return 'Nie można nadpisać pliku'

        return 'Zapisano zawartość'
