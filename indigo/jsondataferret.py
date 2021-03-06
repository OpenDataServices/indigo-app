from indigo.tasks import (
    task_after_fund_update,
    task_after_organisation_update,
    task_after_project_update,
)

from . import TYPE_FUND_PUBLIC_ID, TYPE_ORGANISATION_PUBLIC_ID, TYPE_PROJECT_PUBLIC_ID
from .updatedata import update_fund, update_organisation, update_project


def on_update_callback(record):
    if record.type.public_id == TYPE_PROJECT_PUBLIC_ID:
        update_project(
            record, update_include_organisations=True, update_include_funds=True
        )
        task_after_project_update.delay(record.public_id)
    elif record.type.public_id == TYPE_ORGANISATION_PUBLIC_ID:
        update_organisation(record, update_projects=True)
        task_after_organisation_update.delay(record.public_id)
    elif record.type.public_id == TYPE_FUND_PUBLIC_ID:
        update_fund(record, update_projects=True)
        task_after_fund_update.delay(record.public_id)
