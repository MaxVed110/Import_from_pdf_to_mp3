# на входе путь до пдф файла и язык воспроизведения, а на выходе mp3 файл

import gtts
import pdfplumber
import tkinter as tk
from tkinter.filedialog import askopenfilename


def pdf_to_text():

    window = tk.Tk()
    intro = tk.Label(text="Выберите необходимый pdf файл\n(для продолжения закройте это окно)",
                     width=40, height=4, font='Times 20')
    intro.pack()
    window.mainloop()

    filelocation = askopenfilename()
    with pdfplumber.open(filelocation) as pdf:
        text_pages = [pages.extract_text() for pages in pdf.pages]
    text = ' '.join(text_pages)
    text = text.replace('\n', ' ')
    return text


def text_to_mp3(text: str):

    name_file = input("Ведите название для звукового файла: ")
    print('Старт импорта pdf_to_mp3')
    sound_file = gtts.gTTS(text, lang='ru')
    sound_file.save(name_file + '.mp3')
    print('Импорт успешно завершён')


def main():

    text_to_mp3(pdf_to_text())


if __name__ == '__main__':
    main()
