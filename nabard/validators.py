def validate_powerpoint_file(value):
    import os
    from django.core.exceptions import ValidationError

    extension = os.path.splitext(value.text)[1]
    valid_extensions = ['.ppt', '.pptx', ]
    if not extension.lower() in valid_extensions:
        raise ValidationError('پسوند فایل اشتباه است')


def validate_archived_file(value):
    import os
    from django.core.exceptions import ValidationError

    extension = os.path.splitext(value.text)[1]
    valid_extensions = ['zip', 'rar', '7z', 'tar.gz', ]

    if extension not in valid_extensions:
        raise ValidationError('پسوند فایل اشتباه است')
