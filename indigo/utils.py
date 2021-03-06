import re

import openpyxl
from django.core.exceptions import ValidationError


def get_project_spreadsheet_version(filename):
    return _get_spreadsheet_version(filename)


def get_organisation_spreadsheet_version(filename):
    return _get_spreadsheet_version(filename)


def _get_spreadsheet_version(filename):
    workbook = openpyxl.load_workbook(filename, read_only=True)
    worksheet = workbook["Introduction"]
    for row_idx in range(1, worksheet.max_row + 1):
        if worksheet["A" + str(row_idx)].value == "SPREADSHEET VERSION":
            return worksheet["A" + str(row_idx + 1)].value
    return None


def validate_project_id(value):
    m = re.search("^INDIGO-POJ-[0-9][0-9][0-9][0-9]$", value)
    if not m:
        raise ValidationError("Project IDs should be of the format INDIGO-POJ-0000")


def validate_fund_id(value):
    m = re.search("^INDIGO-FUND-[0-9][0-9][0-9][0-9]$", value)
    if not m:
        raise ValidationError("Fund IDs should be of the format INDIGO-FUND-0000")


def validate_organisation_id(value):
    m = re.search("^INDIGO-ORG-[0-9][0-9][0-9][0-9]$", value)
    if not m:
        raise ValidationError(
            "Organisation IDs should be of the format INDIGO-ORG-0000"
        )
