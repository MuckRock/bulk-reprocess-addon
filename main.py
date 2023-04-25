"""
This DocumentCloud Add-On allows you to bulk reprocress documents on DocumentCloud
"""

from documentcloud.addon import SoftTimeOutAddOn
from documentcloud.constants import BULK_LIMIT
from documentcloud.toolbox import grouper

class Reprocess(SoftTimeOutAddOn):
    """Force reprocress documents given ocr, ocr engine, and language"""

    def main(self):
        """The main add-on functionality goes here."""
        ocr = self.data.get("force_ocr", False)
        lang = self.data["language"]
        if self.data["sure"]:
            for doc_group in grouper(self.get_documents(), BULK_LIMIT):
                doc_group = [
                    {"id": d.id, "force_ocur": ocr, "language": lang} for d in doc_group
                ]
                self.client.post("documents/process/", json=doc_group)


if __name__ == "__main__":
    Reprocess().main()
