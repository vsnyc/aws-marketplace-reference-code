"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) to create an AMI draft product
with a draft public offer.
CAPI-02
"""

import os
import sys
import utils.start_changeset as sc
import utils.stringify_details as sd


def main(change_set_file=None):
    if change_set_file is None:
        fname = "changeset.json"
    else:
        fname = change_set_file
    
    print("Executing change set for " + fname)
        
    change_set_file = os.path.join(os.path.dirname(__file__), fname)
    stringified_change_set = sd.stringify_changeset(change_set_file)

    response = sc.usage_demo(
        stringified_change_set,
        "AMI draft product with draft public offer",
    )

    return response


if __name__ == "__main__":
    if sys.argv[1]:
        change_set_fname = sys.argv[1]
        main(change_set_file=change_set_fname)
    else:
        main()
