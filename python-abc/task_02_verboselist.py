#!/usr/bin/env python3
"""
Extending Python List with Notifications
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        if item in self:
            print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is None:
            index = len(self) - 1
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
