from django.core.exceptions import ValidationError
import re
import pdb


def validator_allowed_tags(text):
    """
    Validation field 'text' for allowed tags.
    Allowed tags: <p>, <i>, <a>, <code>, <strong>,
    if another tag: raise ValidationError
    """
    pattern = re.compile(r"<(?!/?code\b)(?!/?p\b)(?!/?i\b)(?!/?a\b)(?!br\b)(?!/?strong\b)[^>]+>")
    unallowed_tag = pattern.search(text)
    if unallowed_tag:
        raise ValidationError(message="You are using an unallowed tag: %(value)s",
                              code="unallowed",
                              params={"value": text[unallowed_tag.start():unallowed_tag.end()]})
    return text
