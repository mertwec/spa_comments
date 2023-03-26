from django.core.exceptions import ValidationError
import re
import pdb


def validator_closed_tags(text_message: str):
    text = text_message
    text = text.replace("<br>", '')
    pattern = re.compile(r'<(\w+).*?>', re.DOTALL)
    tags = pattern.findall(text)

    for tag in tags:
        open_tag = tag
        close_tag = "</" + open_tag + ">"
        if text.find(close_tag, text.find("<" + open_tag)) == -1:
            raise ValidationError(message="You are have unclossed tag: %(value)s",
                                  code="unclossed",
                                  params={"value": open_tag})
        text = text.replace(close_tag, '', 1)
    return text_message


def validator_allowed_tags(text: str):
    """
    Validation field 'text' for allowed tags.
    Allowed tags: <p>, <i>, <a>, <code>, <strong>,
    if another tag: raise ValidationError
    """
    pattern = re.compile(
        r"<(?!/?code\b)(?!/?p\b)(?!/?i\b)(?!/?br\b)(?!/?a\b)(?!/?strong\b)[^>]+>")
    unallowed_tag = pattern.search(text)
    if unallowed_tag:
        raise ValidationError(message="You are using an unallowed tag: %(value)s",
                              code="unallowed",
                              params={"value": text[unallowed_tag.start():unallowed_tag.end()]})
    return text
