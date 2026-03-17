import fitz

def load_pdf(path):
    try:
        file = fitz.open(path)
    except FileNotFoundError:
        print("Error : File not Found")
    except PermissionError:
        print("Error : Permission ErroR")
    except ValueError:
        print("Error : ValueError")

    text = ""
    for page in file:
        page_text = page.get_text()
        text += page_text
    return text

