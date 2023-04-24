"""
This DocumentCloud Add-On allows you to bulk reprocress documents on DocumentCloud
"""

import requests
from documentcloud.addon import SoftTimeOutAddOn
from documentcloud.constants import BULK_LIMIT
from documentcloud.toolbox import grouper, requests_retry_session

class Reprocess(SoftTimeOutAddOn):
    """Force reprocress documents given ocr, ocr engine, and language"""

    def main(self):
        """The main add-on functionality goes here."""
        ocr = self.data.get("force_ocr")
        if ocr is None:
            ocr = False
        lang = self.data["language"]
        """
        if ocr:
            opts = {"force_ocr" : ocr, "language": lang}
        else: 
            opts = {}
        """

        for doc_group in grouper(self.get_documents(), BULK_LIMIT):
            doc_group = [
                {   
                    "id": d.id
                    "force_ocur": ocr, 
                    "language": lang
                }
                for d in doc_group
            ]
            resp = self.client.post("documents/process/", json=doc_group)
        """
        if self.data.get("sure"):
            for document in self.get_documents():
                self.client.post(f"documents/{document.id}/process/", json=opts)
        """

if __name__ == "__main__":
    Reprocess().main()
