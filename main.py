import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def create_pdf(title, artist, lyrics, translations, transcriptions, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Register the Andika font
    pdfmetrics.registerFont(TTFont('Andika', 'Andika-Regular.ttf'))

    y_position = height - 40  # Start position from the top

    # Add title and artist to the first page in one line
    c.setFont("Andika", 16)
    c.drawString(40, y_position, f"{artist.strip()} - {title.strip()}")
    y_position -= 40  # Add some space before the lyrics

    for lyric, translation, transcription in zip(lyrics, translations, transcriptions):
        c.setFont("Andika", 12)
        c.drawString(40, y_position, lyric.strip())
        y_position -= 20

        c.setFont("Andika", 10)
        c.drawString(40, y_position, translation.strip())
        y_position -= 20

        c.setFont("Andika", 12)
        c.drawString(40, y_position, transcription.strip())
        y_position -= 30  # Add a little space between sections

        if y_position < 40:  # Check if we need to add a new page
            c.showPage()
            y_position = height - 40

    c.save()

def main():
    title_data = read_file('title.txt')
    title = title_data[1]
    artist = title_data[0]

    lyrics = read_file('track.fr')
    translations = read_file('track.txt')
    transcriptions = read_file('track.ipa')

    create_pdf(title, artist, lyrics, translations, transcriptions, 'track.pdf')

def proc_dir(text_path, tranlsation_path, transcription_path, output_path, artist, title):
    
    lyrics = read_file(text_path)
    translations = read_file(tranlsation_path)
    transcriptions = read_file(transcription_path)

    create_pdf(title, artist, lyrics, translations, transcriptions, output_path)

    pass


def proc_all_dirs(path = "C:\\Projects\\YandexMusic\\data"):
    for root, dirs, files in os.walk(path):
        #if 'track.pdf' in files:
        #    continue;
        #if 'ok' in files:
        #    continue;
        files_set = ["track.fr", "track.txt", "track.ipa"]
        if set(files_set).issubset(files):
            print(f'proc in {root}')
            
            path_parts = root.split(os.sep)
            artist = path_parts[-2]
            title = path_parts[-1]
            files_set.append("track.pdf")
            params = [os.path.join(root, f) for f in files_set]
            proc_dir(*params, artist, title)
    

if __name__ == "__main__":
    proc_all_dirs()