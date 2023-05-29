from Ocr import Ocr
from Ner import Ner
from JsonParser import JsonParser


def test_normal_table():
    ocr = Ocr()
    with open("test_images\\normal.jpg", "rb") as f:
        image_data = f.read()
        ocr_result = ocr.get_recognition(image_data)
        jsonParser = JsonParser(ocr_result)
        df = jsonParser.get_property()
        assert len(df) == 2


def test_normal_multiline_table():
    ocr = Ocr()
    with open("test_images\\multiline.jpg", "rb") as f:
        image_data = f.read()
        ocr_result = ocr.get_recognition(image_data)
        jsonParser = JsonParser(ocr_result)
        df = jsonParser.get_property()
        assert len(df) == 21


def test_broken_wrong_doc():
    ocr = Ocr()
    with open("test_images\\wrong_doc.jpg", "rb") as f:
        image_data = f.read()
        ocr_result = ocr.get_recognition(image_data)
        jsonParser = JsonParser(ocr_result)
        df = jsonParser.get_property()
        print(df)
        assert len(df) == 0


def test_ner_normal():
    ocr = Ocr()
    with open("test_images\\normal.jpg", "rb") as f:
        image_data = f.read()
        ocr_result = ocr.get_recognition(image_data)
        jsonParser = JsonParser(ocr_result)
        ner = Ner(jsonParser.doc_text)

        assert ner.get_notif_number() == "07-1496/22"
        assert "Сулав" in ner.get_debtor_name()
        assert "Сбербанк" in ner.get_claimant()


def test_ner_contracted():
    ocr = Ocr()
    with open("test_images\\multiline.jpg", "rb") as f:
        image_data = f.read()
        ocr_result = ocr.get_recognition(image_data)
        jsonParser = JsonParser(ocr_result)
        ner = Ner(jsonParser.doc_text)

        assert ner.get_notif_number() == "62-1567/22"
        assert ner.get_debtor_name() == "-"
        assert ner.get_claimant() == "-"


def test_ner_wrong_doc():
    ocr = Ocr()
    with open("test_images\\wrong_doc.jpg", "rb") as f:
        image_data = f.read()
        ocr_result = ocr.get_recognition(image_data)
        jsonParser = JsonParser(ocr_result)
        ner = Ner(jsonParser.doc_text)

        assert ner.get_notif_number() == "-"
        assert ner.get_debtor_name() == "-"
        assert ner.get_claimant() == "-"
