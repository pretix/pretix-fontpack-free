import functools
import json
from django.contrib.staticfiles import finders
from django.dispatch import receiver
from django.utils.safestring import mark_safe
from pretix.plugins.ticketoutputpdf.signals import register_fonts

BASEPATH = 'pretix_fontpackfree'


@functools.cache
def load_catalog():
    catalog_file: str | None = finders.find(BASEPATH + "/catalog.json")
    if not catalog_file:
        raise RuntimeError("catalog.json not found")

    with open(catalog_file, "r") as f:
        noto_catalog = json.load(f)

    fonts = {}
    for family, variants in noto_catalog.items():
        fonts[family] = {}
        for variant, formats in variants.items():
            fonts[family][variant] = {}
            if variant == "sample":
                fonts[family][variant] = mark_safe(formats)
            elif isinstance(formats, dict):
                for format, path in formats.items():
                    fonts[family][variant][format] = BASEPATH + "/" + path
            else:
                fonts[family][variant] = formats

    return fonts


@receiver(register_fonts, dispatch_uid="fontpack_free_fonts")
def fontpack_free(sender, **kwargs):
    return {
        **load_catalog(),
        "Droid Serif": {
            "regular": {
                "truetype": BASEPATH + "/DroidSerif-Regular-webfont.ttf",
                "woff": BASEPATH + "/DroidSerif-Regular-webfont.woff",
            },
            "bold": {
                "truetype": BASEPATH + "/DroidSerif-Bold-webfont.ttf",
                "woff": BASEPATH + "/DroidSerif-Bold-webfont.woff",
            },
            "italic": {
                "truetype": BASEPATH + "/DroidSerif-Italic-webfont.ttf",
                "woff": BASEPATH + "/DroidSerif-Italic-webfont.woff",
            },
            "bolditalic": {
                "truetype": BASEPATH + "/DroidSerif-BoldItalic-webfont.ttf",
                "woff": BASEPATH + "/DroidSerif-BoldItalic-webfont.woff",
            },
        },
        "Titillium": {
            "regular": {
                "truetype": BASEPATH + "/titillium-regular-webfont.ttf",
                "woff": BASEPATH + "/titillium-regular-webfont.woff",
                "woff2": BASEPATH + "/titillium-regular-webfont.woff2",
            },
            "bold": {
                "truetype": BASEPATH + "/titillium-bold-webfont.ttf",
                "woff": BASEPATH + "/titillium-bold-webfont.woff",
                "woff2": BASEPATH + "/titillium-bold-webfont.woff2",
            },
            "italic": {
                "truetype": BASEPATH + "/titillium-regularitalic-webfont.ttf",
                "woff": BASEPATH + "/titillium-regularitalic-webfont.woff",
                "woff2": BASEPATH + "/titillium-regularitalic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": BASEPATH + "/titillium-bolditalic-webfont.ttf",
                "woff": BASEPATH + "/titillium-bolditalic-webfont.woff",
                "woff2": BASEPATH + "/titillium-bolditalic-webfont.woff2",
            },
        },
        "Titillium Upright": {
            "pdf_only": True,  # does not have italic scripts and doesn't look good as a full-page font
            "regular": {
                "truetype": BASEPATH + "/titillium-regularupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-regularupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-regularupright-webfont.woff2",
            },
            "bold": {
                "truetype": BASEPATH + "/titillium-boldupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-boldupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-boldupright-webfont.woff2",
            },
            "italic": {
                "truetype": BASEPATH + "/titillium-regularupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-regularupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-regularupright-webfont.woff2",
            },
            "bolditalic": {
                "truetype": BASEPATH + "/titillium-boldupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-boldupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-boldupright-webfont.woff2",
            },
        },
        "Titillium Semibold Upright": {
            "pdf_only": True,  # does not have italic scripts and doesn't look good as a full-page font
            "regular": {
                "truetype": BASEPATH + "/titillium-semiboldupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-semiboldupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-semiboldupright-webfont.woff2",
            },
            "bold": {
                "truetype": BASEPATH + "/titillium-boldupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-boldupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-boldupright-webfont.woff2",
            },
            "italic": {
                "truetype": BASEPATH + "/titillium-semiboldupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-semiboldupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-semiboldupright-webfont.woff2",
            },
            "bolditalic": {
                "truetype": BASEPATH + "/titillium-boldupright-webfont.ttf",
                "woff": BASEPATH + "/titillium-boldupright-webfont.woff",
                "woff2": BASEPATH + "/titillium-boldupright-webfont.woff2",
            }
        },
        "DejaVu Sans": {
            "regular": {
                "truetype": BASEPATH + "/DejaVuSans-webfont.ttf",
                "woff": BASEPATH + "/DejaVuSans-webfont.woff",
            },
            "bold": {
                "truetype": BASEPATH + "/DejaVuSans-Bold-webfont.ttf",
                "woff": BASEPATH + "/DejaVuSans-Bold-webfont.woff",
            },
            "italic": {
                "truetype": BASEPATH + "/DejaVuSans-Oblique-webfont.ttf",
                "woff": BASEPATH + "/DejaVuSans-Oblique-webfont.woff",
            },
            "bolditalic": {
                "truetype": BASEPATH + "/DejaVuSans-BoldOblique-webfont.ttf",
                "woff": BASEPATH + "/DejaVuSans-BoldOblique-webfont.woff",
            },
            "sample": mark_safe(
                "Съешь же ещё этих мягких французских булок да выпей чаю.<br>"
                "דג סקרן שט לו בים זך אך לפתע מצא חבורה נחמדה שצצה כך."
                "<br>"
                "Ταχίστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός"
                "<br>"
                "نص حكيم له سر قاطع وذو شأن عظيم مكتوب على ثوب أخضر ومغلف بجلد أزرق"
            ),
        },
        "Baloo Bhaijaan": {
            "regular": {
                "truetype": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "bold": {
                "truetype": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "italic": {
                "truetype": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "bolditalic": {
                "truetype": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": BASEPATH + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "sample": mark_safe(
                "Do bạch kim rất quý nên sẽ dùng để lắp vô xương<br>"
                "نص حكيم له سر قاطع وذو شأن عظيم مكتوب على ثوب أخضر ومغلف بجلد أزرق"
            )
        }
    }
