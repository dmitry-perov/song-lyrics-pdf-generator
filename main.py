from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def create_pdf(lyrics, translations, transcriptions, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    # Register the Andika font
    pdfmetrics.registerFont(TTFont('Andika', 'Andika-Regular.ttf'))

    y_position = height - 40  # Start position from the top

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
    lyrics = read_file('track.fr')
    translations = read_file('track.txt')
    transcriptions = read_file('track.ipa')

    create_pdf(lyrics, translations, transcriptions, 'output.pdf')

if __name__ == "__main__":
    main()