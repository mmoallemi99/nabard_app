def validate_powerpoint_file(value):
    import os
    from django.core.exceptions import ValidationError

    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.ppt', '.pptx', '.zip', '.rar', '.7z', '.tar.gz', ]
    if not extension.lower() in valid_extensions:
        valid_str = " , ".join(valid_extensions)
        error_msg = 'پسوند فایل اشتباه است - پسوند های مجاز: {0}'.format(valid_str)
        raise ValidationError(error_msg)


def validate_archived_file(value):
    import os
    from django.core.exceptions import ValidationError

    extension = os.path.splitext(value.name)[1]
    valid_extensions = ['.zip', '.rar', '.7z', '.tar.gz', ]

    if extension not in valid_extensions:
        valid_str = " , ".join(valid_extensions)
        error_msg = 'پسوند فایل اشتباه است - پسوند های مجاز: {0}'.format(valid_str)
        raise ValidationError(error_msg)
