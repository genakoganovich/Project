import win32com.client

def extract_courier_text(doc_path, output_path):
    # Открытие Word через COM
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = False

    doc = word.Documents.Open(doc_path)

    found_text = None

    # Перебираем все параграфы
    for para in doc.Paragraphs:
        rng = para.Range
        font_name = rng.Font.Name
        font_size = rng.Font.Size

        # Ищем первый фрагмент с нужным шрифтом и размером
        if font_name == "Courier New" and font_size == 9.0:
            found_text = rng.Text.strip()
            break

    # Закрытие документа и Word
    doc.Close(False)
    word.Quit()

    # Сохраняем в файл, если найдено
    if found_text:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(found_text)
    else:
        print("Текст со шрифтом Courier New 9pt не найден.")


if __name__ == "__main__":
    extract_courier_text("Listings.doc", "output_path")