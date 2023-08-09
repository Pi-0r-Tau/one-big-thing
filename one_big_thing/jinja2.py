import datetime

import humanize
import jinja2
from django.templatetags.static import static
from django.urls import reverse
from django.utils.text import slugify
from markdown_it import MarkdownIt

markdown_converter = MarkdownIt("js-default") # Need js-default as secure setting

DEFAULT = object()


def url(path, *args, **kwargs):
    assert not (args and kwargs)
    return reverse(path, args=args, kwargs=kwargs)


def markdown(text, cls=None):
    """
    Converts the given text into markdown.
    The `replace` statement replaces the outer <p> tag with one that contains the given class, otherwise the markdown
    ends up double wrapped with <p> tags.
    Args:
        text: The text to convert to markdown
        cls (optional): The class to apply to the outermost <p> tag surrounding the markdown
    Returns:
        Text converted to markdown
    """
    html = markdown_converter.render(text).strip()
    html = html.replace("<p>", f'<p class="{cls or ""}">', 1).replace("</p>", "", 1)
    return html


def is_selected(data, name, value):
    if str(data.get(name)) == str(value):
        return "selected"
    else:
        return ""


def is_in(data, name, value):
    if value in data.get(name, ()):
        return "selected"
    else:
        return ""


def is_checked(data, name, value):
    if str(data.get(name)) == str(value):
        return "checked"
    else:
        return ""


def is_empty_selected(data, name):
    if data.get(name) in ("", None):
        return "selected"
    else:
        return ""


def list_to_options(iterable):
    result = tuple({"value": item[0], "text": item[1]} for item in iterable)
    return result


def humanize_timedelta(minutes=0):
    delta = datetime.timedelta(minutes=minutes)
    return humanize.precisedelta(delta, minimum_unit="minutes")


def environment(**options):
    extra_options = dict()
    env = jinja2.Environment(  # nosec B701
        **{
            "autoescape": True,
            **options,
            **extra_options,
        }
    )
    env.globals.update(
        {
            "static": static,
            "url": url,
            "is_checked": is_checked,
            "is_in": is_in,
            "is_selected": is_selected,
            "slugify": slugify,
            "list_to_options": list_to_options,
            "is_empty_selected": is_empty_selected,
            "DEFAULT": DEFAULT,
            "humanize_timedelta": humanize_timedelta,
        }
    )
    return env
