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
        print(BULK_LIMIT)
        if self.data.get("sure"):
            for document in self.get_documents():
                doc_group = [
                    {"id": document.id, "force_ocr": ocr, "language": lang} ]
                self.client.post("documents/process/", json=doc_group)

        else:
            self.set_message(
                "You did not select sure, this Add-On did not do anything."
            )


if __name__ == "__main__":
    Reprocess().main()
