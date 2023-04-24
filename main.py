"""
This DocumentCloud Add-On allows you to bulk reprocress documents on DocumentCloud
"""

import requests
from documentcloud.addon import SoftTimeOutAddOn

class Reprocess(SoftTimeOutAddOn):
    """Force reprocress documents given ocr, ocr engine, and language"""

    def main(self):
        """The main add-on functionality goes here."""
        ocr = self.data.get("force_ocr")
        if ocr is None:
            ocr = False
        ocr_engine = self.data.get("ocr_engine")
        document_language = self.data.get("document_language")
        opts = {"force_ocr" : ocr}
        if self.data.get("sure"):
            for document in self.get_documents():
                self.client.post(f"document/{document.id}/process", json=opts)


if __name__ == "__main__":
    Reprocess().main()
