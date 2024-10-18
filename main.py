import pdf_to_image
import diode_recognition
import label
import rename


def main():
    rename.rename_pdf_to_input()
    pdf_to_image.main()
    diode_recognition.main()
    label.main()


if __name__ == "__main__":
    main()
