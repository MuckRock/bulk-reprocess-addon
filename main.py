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
        lang = self.data["language"]
        document_language = self.data.get("document_language")
        if ocr:
            opts = {"force_ocr" : ocr, "language": lang}
        else: 
            opts = {}
        if self.data.get("sure"):
            for document in self.get_documents():
                self.client.post(f"documents/{document.id}/process/", json=opts)


if __name__ == "__main__":
    Reprocess().main()
