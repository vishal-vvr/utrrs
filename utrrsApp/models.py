from django.db import models

rendering_engines = (
    ("pango","pango"),
    ("harfbuz", "harfbuzz"),
    ("other","other"),
)

reference_types=(
    ("codepoint", "codepoint"),
    ("gsub", "gsub"),
    ("gpos", "gpos"),
)

class Lang(models.Model):
    locale_code=models.CharField(max_length=7, primary_key=True)
    language=models.CharField(max_length=20,null=False)
    description=models.TextField(null=False)
    unicode_range=models.CharField(max_length=20, null=False)
    unicode_chart=models.CharField(max_length=50, null=False)
    font_used=models.CharField(max_length=50, null=False)
    rendering_engine_used=models.CharField(max_length=20, choices= rendering_engines, default="pango")

class Utrrs(models.Model):
    locale_code=models.ForeignKey(Lang, on_delete=models.CASCADE)
    reference_data_type=models.CharField(max_length=20, choices=reference_types, default="codepoint")
    image=models.ImageField(upload_to="reference_images")
    rawcode=models.CharField(max_length=100, null=False)
    desc=models.TextField(null=False)
