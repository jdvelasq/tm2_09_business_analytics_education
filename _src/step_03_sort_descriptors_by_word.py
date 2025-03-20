# pylint: disable=import-error
"""Review if all definitions present in descriptors.the.txt are defined in abbreviations.the.txt."""

#
# Step 1: review the descriptors.the.txt file
# Step 2: add other descriptions to the file
#
from techminer2.thesaurus.descriptors import sort_thesaurus  # type: ignore

if __name__ == "__main__":

    sort_thesaurus(
        #
        # SORT OPTIONS:
        order="by-word-length",
        #
        # DATABASE PARAMS:
        root_dir="./",
    )
