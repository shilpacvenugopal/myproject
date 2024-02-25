# Resource.py for import file
from import_export.resources import ModelResource
from .models import Table2
from import_export.fields import Field


class Table2Resource(ModelResource):
    id = Field(attribute='id', column_name='id', readonly=True)  # Exclude 'id' field from import

    class Meta:
        model = Table2
        skip_unchanged = True
        report_skipped = False
        import_id_fields = ('id',)

    def import_data(self, dataset, dry_run=False, raise_errors=False, use_transactions=None, collect_failed_rows=False,
                    **kwargs):
        # default import
        result = super().import_data(dataset, dry_run, raise_errors, use_transactions, collect_failed_rows, **kwargs)
        existing_students = Table2.objects.values_list('student__id', flat=True)
        formatted_invalid_rows = []

        for row_idx, row in enumerate(dataset.dict, start=1):
            if row['student'] in str(existing_students):
                error_msg = f"Student already exists. Row: {row_idx}"
                formatted_invalid_rows.append({
                    'ROW': row_idx,
                    'ERRORS': error_msg,
                    **row
                })

        # Addition of  formatted invalid rows to results.invalid_rows
        result.invalid_rows += formatted_invalid_rows

        # Removed the skipped rows from the dataset
        dataset.dict = [row for row in dataset.dict if row not in result.invalid_rows]

        return result
