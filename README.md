# Song Lyrics PDF Generator

This project is a simple application that generates a PDF file containing the lyrics of a song along with its translation and transcription. The application reads the lyrics, translation, and transcription from separate text files and formats them for output in the PDF.

## Project Structure

```
song-lyrics-pdf-generator
├── src
│   ├── main.py           # Main script to generate the PDF
│   ├── lyrics.txt        # Contains the lyrics of the song
│   ├── translation.txt    # Contains the translation of the lyrics
│   └── transcription.txt   # Contains the transcription of the lyrics
├── requirements.txt      # Lists the dependencies required for the project
└── README.md             # Documentation for the project
```

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

```
pip install -r requirements.txt
```

## Usage

1. Place your song lyrics in `src/lyrics.txt`.
2. Add the corresponding translations in `src/translation.txt`.
3. Include the transcriptions in `src/transcription.txt`.
4. Run the main script to generate the PDF:

```
python src/main.py
```

The generated PDF will contain the lyrics, with the translation displayed below each line in a smaller font, followed by the transcription.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.