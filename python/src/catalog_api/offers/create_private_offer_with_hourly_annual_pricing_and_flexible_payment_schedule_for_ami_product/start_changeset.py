"""
Purpose
Shows how to use the AWS SDK for Python (Boto3) to create a private offer with hourly annual pricing and flexible payment schedule for my AMI product
CAPI-XX
"""

import os

import utils.start_changeset as sc
import utils.stringify_details as sd

fname = "changeset.json"
change_set_file = os.path.join(os.path.dirname(__file__), fname)

change_set = sd.stringify_changeset(change_set_file)


def main():
    sc.usage_demo(
        change_set,
        "Create private offer with hourly annual pricing and flexible payment schedule for my AMI product",
    )


if __name__ == "__main__":
    main()
