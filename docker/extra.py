from slugify import slugify, SLUG_OK

def slugify_filter(input, **kwargs):
  if "extra_chars" in kwargs:
    kwargs["ok"] = SLUG_OK+kwargs["extra_chars"]
    del kwargs["extra_chars"]
  return slugify(input, **kwargs)

JINJA2_FILTERS = {
    'slugify': slugify_filter,
}
