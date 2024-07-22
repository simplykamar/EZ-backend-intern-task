from django.core.exceptions import ValidationError

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Get file extension
    valid_extensions = ['.pptx', '.docx', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension. Allowed extensions are: .pptx, .docx, .xlsx')
