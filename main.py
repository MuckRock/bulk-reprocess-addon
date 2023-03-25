"""
This DocumentCloud Add-On allows you to bulk reprocress documents on DocumentCloud
"""

from documentcloud.addon import SoftTimeOutAddOn

class Reprocess(SoftTimeOutAddOn):
    """Force reprocress documents given ocr, ocr engine, and language"""

    def main(self):
        """The main add-on functionality goes here."""
        """ ocr = self.data.get("ocr")
        ocr_engine = self.data.get("ocr_engine")
        document_language = self.data.get("document_language")"""
        for document in self.get_documents():
            document.procress()


if __name__ == "__main__":
    HelloWorld().main()
