# pylint: disable=import-error

#
# Reset the thesaurus generating a entry for each different string in descriptors,
# the replace the abbreviations, and finally clean the entries.
#
from techminer2.thesaurus.descriptors import reset_thesaurus  # type: ignore

if __name__ == "__main__":

    reset_thesaurus(root_dir="./")
