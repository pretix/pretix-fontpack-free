from django.dispatch import receiver
from django.utils.safestring import mark_safe

from pretix.plugins.ticketoutputpdf.signals import register_fonts


@receiver(register_fonts, dispatch_uid="fontpack_free_fonts")
def fontpack_free(sender, **kwargs):
    basepath = 'pretix_fontpackfree'
    return {
        "Noto Sans": {
            "regular": {
                "truetype": basepath + "/NotoSans-Regular-webfont.ttf",
                "woff": basepath + "/NotoSans-Regular-webfont.woff",
                "woff2": basepath + "/NotoSans-Regular-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/NotoSans-Bold-webfont.ttf",
                "woff": basepath + "/NotoSans-Bold-webfont.woff",
                "woff2": basepath + "/NotoSans-Bold-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/NotoSans-Italic-webfont.ttf",
                "woff": basepath + "/NotoSans-Italic-webfont.woff",
                "woff2": basepath + "/NotoSans-Italic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/NotoSans-BoldItalic-webfont.ttf",
                "woff": basepath + "/NotoSans-BoldItalic-webfont.woff",
                "woff2": basepath + "/NotoSans-BoldItalic-webfont.woff2",
            },
            "sample": mark_safe(
                "Съешь же ещё этих мягких французских булок да выпей чаю.<br>"
                "Ταχίστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός"
            )
        },
        "Roboto": {
            "regular": {
                "truetype": basepath + "/Roboto-Regular.ttf",
                "woff": basepath + "/Roboto-Regular-webfont.woff",
            },
            "bold": {
                "truetype": basepath + "/Roboto-Bold.ttf",
                "woff": basepath + "/Roboto-Bold-webfont.woff",
            },
            "italic": {
                "truetype": basepath + "/Roboto-Italic.ttf",
                "woff": basepath + "/Roboto-Italic-webfont.woff",
            },
            "bolditalic": {
                "truetype": basepath + "/Roboto-BoldItalic.ttf",
                "woff": basepath + "/Roboto-BoldItalic-webfont.woff",
            }
        },
        "Roboto Condensed": {
            "regular": {
                "truetype": basepath + "/RobotoCondensed-Regular-webfont.ttf",
                "woff": basepath + "/RobotoCondensed-Regular-webfont.woff",
            },
            "bold": {
                "truetype": basepath + "/RobotoCondensed-Bold-webfont.ttf",
                "woff": basepath + "/RobotoCondensed-Bold-webfont.woff",
            },
            "italic": {
                "truetype": basepath + "/RobotoCondensed-Italic-webfont.ttf",
                "woff": basepath + "/RobotoCondensed-Italic-webfont.woff",
            },
            "bolditalic": {
                "truetype": basepath + "/RobotoCondensed-BoldItalic-webfont.ttf",
                "woff": basepath + "/RobotoCondensed-BoldItalic-webfont.woff",
            }
        },
        "Droid Serif": {
            "regular": {
                "truetype": basepath + "/DroidSerif-Regular-webfont.ttf",
                "woff": basepath + "/DroidSerif-Regular-webfont.woff",
            },
            "bold": {
                "truetype": basepath + "/DroidSerif-Bold-webfont.ttf",
                "woff": basepath + "/DroidSerif-Bold-webfont.woff",
            },
            "italic": {
                "truetype": basepath + "/DroidSerif-Italic-webfont.ttf",
                "woff": basepath + "/DroidSerif-Italic-webfont.woff",
            },
            "bolditalic": {
                "truetype": basepath + "/DroidSerif-BoldItalic-webfont.ttf",
                "woff": basepath + "/DroidSerif-BoldItalic-webfont.woff",
            },
        },
        "Fira Sans": {
            "regular": {
                "truetype": basepath + "/firasans-regular-webfont.ttf",
                "woff": basepath + "/firasans-regular-webfont.woff",
                "woff2": basepath + "/firasans-regular-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/firasans-bold-webfont.ttf",
                "woff": basepath + "/firasans-bold-webfont.woff",
                "woff2": basepath + "/firasans-bold-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/firasans-italic-webfont.ttf",
                "woff": basepath + "/firasans-italic-webfont.woff",
                "woff2": basepath + "/firasans-italic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/firasans-bolditalic-webfont.ttf",
                "woff": basepath + "/firasans-bolditalic-webfont.woff",
                "woff2": basepath + "/firasans-bolditalic-webfont.woff2",
            }
        },
        "Lato": {
            "regular": {
                "truetype": basepath + "/Lato-Regular.ttf",
                "woff": basepath + "/lato-regular-webfont.woff",
                "woff2": basepath + "/lato-regular-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/Lato-Bold.ttf",
                "woff": basepath + "/lato-bold-webfont.woff",
                "woff2": basepath + "/lato-bold-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/Lato-Italic.ttf",
                "woff": basepath + "/lato-italic-webfont.woff",
                "woff2": basepath + "/lato-italic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/Lato-BoldItalic.ttf",
                "woff": basepath + "/lato-bolditalic-webfont.woff",
                "woff2": basepath + "/lato-bolditalic-webfont.woff2",
            }
        },
        "Oswald": {
            "regular": {
                "truetype": basepath + "/oswald-regular-webfont.ttf",
                "woff": basepath + "/oswald-regular-webfont.woff",
                "woff2": basepath + "/oswald-regular-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/oswald-bold-webfont.ttf",
                "woff": basepath + "/oswald-bold-webfont.woff",
                "woff2": basepath + "/oswald-bold-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/oswald-regularitalic-webfont.ttf",
                "woff": basepath + "/oswald-regularitalic-webfont.woff",
                "woff2": basepath + "/oswald-regularitalic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/oswald-bolditalic-webfont.ttf",
                "woff": basepath + "/oswald-bolditalic-webfont.woff",
                "woff2": basepath + "/oswald-bolditalic-webfont.woff2",
            }
        },
        "Titillium": {
            "regular": {
                "truetype": basepath + "/titillium-regular-webfont.ttf",
                "woff": basepath + "/titillium-regular-webfont.woff",
                "woff2": basepath + "/titillium-regular-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/titillium-bold-webfont.ttf",
                "woff": basepath + "/titillium-bold-webfont.woff",
                "woff2": basepath + "/titillium-bold-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/titillium-regularitalic-webfont.ttf",
                "woff": basepath + "/titillium-regularitalic-webfont.woff",
                "woff2": basepath + "/titillium-regularitalic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/titillium-bolditalic-webfont.ttf",
                "woff": basepath + "/titillium-bolditalic-webfont.woff",
                "woff2": basepath + "/titillium-bolditalic-webfont.woff2",
            }
        },
        "Titillium Upright": {
            "pdf_only": True,  # does not have italic scripts and doesn't look good as a full-page font
            "regular": {
                "truetype": basepath + "/titillium-regularupright-webfont.ttf",
                "woff": basepath + "/titillium-regularupright-webfont.woff",
                "woff2": basepath + "/titillium-regularupright-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/titillium-boldupright-webfont.ttf",
                "woff": basepath + "/titillium-boldupright-webfont.woff",
                "woff2": basepath + "/titillium-boldupright-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/titillium-regularupright-webfont.ttf",
                "woff": basepath + "/titillium-regularupright-webfont.woff",
                "woff2": basepath + "/titillium-regularupright-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/titillium-boldupright-webfont.ttf",
                "woff": basepath + "/titillium-boldupright-webfont.woff",
                "woff2": basepath + "/titillium-boldupright-webfont.woff2",
            }
        },
        "Titillium Semibold Upright": {
            "pdf_only": True,  # does not have italic scripts and doesn't look good as a full-page font
            "regular": {
                "truetype": basepath + "/titillium-semiboldupright-webfont.ttf",
                "woff": basepath + "/titillium-semiboldupright-webfont.woff",
                "woff2": basepath + "/titillium-semiboldupright-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/titillium-boldupright-webfont.ttf",
                "woff": basepath + "/titillium-boldupright-webfont.woff",
                "woff2": basepath + "/titillium-boldupright-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/titillium-semiboldupright-webfont.ttf",
                "woff": basepath + "/titillium-semiboldupright-webfont.woff",
                "woff2": basepath + "/titillium-semiboldupright-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/titillium-boldupright-webfont.ttf",
                "woff": basepath + "/titillium-boldupright-webfont.woff",
                "woff2": basepath + "/titillium-boldupright-webfont.woff2",
            }
        },
        "Montserrat": {
            "regular": {
                "truetype": basepath + "/montserrat-regular-webfont.ttf",
                "woff": basepath + "/montserrat-regular-webfont.woff",
                "woff2": basepath + "/montserrat-regular-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/montserrat-bold-webfont.ttf",
                "woff": basepath + "/montserrat-bold-webfont.woff",
                "woff2": basepath + "/montserrat-bold-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/montserrat-italic-webfont.ttf",
                "woff": basepath + "/montserrat-italic-webfont.woff",
                "woff2": basepath + "/montserrat-italic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/montserrat-bolditalic-webfont.ttf",
                "woff": basepath + "/montserrat-bolditalic-webfont.woff",
                "woff2": basepath + "/montserrat-bolditalic-webfont.woff2",
            }
        },
        "Vollkorn": {
            "regular": {
                "truetype": basepath + "/Vollkorn-Regular.ttf",
                "woff": basepath + "/vollkorn-regular-webfont.woff",
                "woff2": basepath + "/vollkorn-regular-webfont.woff2",
            },
            "bold": {
                "truetype": basepath + "/Vollkorn-Bold.ttf",
                "woff": basepath + "/vollkorn-bold-webfont.woff",
                "woff2": basepath + "/vollkorn-bold-webfont.woff2",
            },
            "italic": {
                "truetype": basepath + "/Vollkorn-Italic.ttf",
                "woff": basepath + "/vollkorn-italic-webfont.woff",
                "woff2": basepath + "/vollkorn-italic-webfont.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/Vollkorn-BoldItalic.ttf",
                "woff": basepath + "/vollkorn-bolditalic-webfont.woff",
                "woff2": basepath + "/vollkorn-bolditalic-webfont.woff2",
            },
        },
        "DejaVu Sans": {
            "regular": {
                "truetype": basepath + "/DejaVuSans-webfont.ttf",
                "woff": basepath + "/DejaVuSans-webfont.woff",
            },
            "bold": {
                "truetype": basepath + "/DejaVuSans-Bold-webfont.ttf",
                "woff": basepath + "/DejaVuSans-Bold-webfont.woff",
            },
            "italic": {
                "truetype": basepath + "/DejaVuSans-Oblique-webfont.ttf",
                "woff": basepath + "/DejaVuSans-Oblique-webfont.woff",
            },
            "bolditalic": {
                "truetype": basepath + "/DejaVuSans-BoldOblique-webfont.ttf",
                "woff": basepath + "/DejaVuSans-BoldOblique-webfont.woff",
            },
            "sample": mark_safe(
                "Съешь же ещё этих мягких французских булок да выпей чаю.<br>"
                "דג סקרן שט לו בים זך אך לפתע מצא חבורה נחמדה שצצה כך." 
                "<br>"
                "Ταχίστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός"
                "<br>"
                "نص حكيم له سر قاطع وذو شأن عظيم مكتوب على ثوب أخضر ومغلف بجلد أزرق"
            )
        },
        "Baloo Bhaijaan": {
            "regular": {
                "truetype": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "bold": {
                "truetype": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "italic": {
                "truetype": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.ttf",
                "woff": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff",
                "woff2": basepath + "/baloo-bhaijaan-v6-latin-ext_vietnamese_latin_arabic-regular.woff2",
            },
            "sample": mark_safe(
                "Do bạch kim rất quý nên sẽ dùng để lắp vô xương<br>"
                "نص حكيم له سر قاطع وذو شأن عظيم مكتوب على ثوب أخضر ومغلف بجلد أزرق"
            )
        },
        "Tajawal": {
            "regular": {
                "truetype": basepath + "/tajawal-v3-latin_arabic-regular.ttf",
                "woff": basepath + "/tajawal-v3-latin_arabic-regular.woff",
                "woff2": basepath + "/tajawal-v3-latin_arabic-regular.woff2",
            },
            "bold": {
                "truetype": basepath + "/tajawal-v3-latin_arabic-700.ttf",
                "woff": basepath + "/tajawal-v3-latin_arabic-700.woff",
                "woff2": basepath + "/tajawal-v3-latin_arabic-700.woff2",
            },
            "italic": {
                "truetype": basepath + "/tajawal-v3-latin_arabic-regular.ttf",
                "woff": basepath + "/tajawal-v3-latin_arabic-regular.woff",
                "woff2": basepath + "/tajawal-v3-latin_arabic-regular.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/tajawal-v3-latin_arabic-700.ttf",
                "woff": basepath + "/tajawal-v3-latin_arabic-700.woff",
                "woff2": basepath + "/tajawal-v3-latin_arabic-700.woff2",
            },
            "sample": "نص حكيم له سر قاطع وذو شأن عظيم مكتوب على ثوب أخضر ومغلف بجلد أزرق"
        },
        "Poppins": {
            "regular": {
                "truetype": basepath + "/poppins-v12-latin-500.ttf",
                "woff": basepath + "/poppins-v12-latin-500.woff",
                "woff2": basepath + "/poppins-v12-latin-500.woff2",
            },
            "bold": {
                "truetype": basepath + "/poppins-v12-latin-700.ttf",
                "woff": basepath + "/poppins-v12-latin-700.woff",
                "woff2": basepath + "/poppins-v12-latin-700.woff2",
            },
            "italic": {
                "truetype": basepath + "/poppins-v12-latin-500italic.ttf",
                "woff": basepath + "/poppins-v12-latin-500italic.woff",
                "woff2": basepath + "/poppins-v12-latin-500italic.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/poppins-v12-latin-700italic.ttf",
                "woff": basepath + "/poppins-v12-latin-700italic.woff",
                "woff2": basepath + "/poppins-v12-latin-700italic.woff2",
            },
        },
        "Almarai": {
            "regular": {
                "truetype": basepath + "/almarai-v5-arabic-regular.ttf",
                "woff": basepath + "/almarai-v5-arabic-regular.woff",
                "woff2": basepath + "/almarai-v5-arabic-regular.woff2",
            },
            "bold": {
                "truetype": basepath + "/almarai-v5-arabic-800.ttf",
                "woff": basepath + "/almarai-v5-arabic-800.woff",
                "woff2": basepath + "/almarai-v5-arabic-800.woff2",
            },
            "italic": {
                "truetype": basepath + "/almarai-v5-arabic-regular.ttf",
                "woff": basepath + "/almarai-v5-arabic-regular.woff",
                "woff2": basepath + "/almarai-v5-arabic-regular.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/almarai-v5-arabic-800.ttf",
                "woff": basepath + "/almarai-v5-arabic-800.woff",
                "woff2": basepath + "/almarai-v5-arabic-800.woff2",
            },
            "sample": "نص حكيم له سر قاطع وذو شأن عظيم مكتوب على ثوب أخضر ومغلف بجلد أزرق"
        },
        "Ubuntu": {
            "regular": {
                "truetype": basepath + "/ubuntu-v15-latin-ext_latin-regular.ttf",
                "woff": basepath + "/ubuntu-v15-latin-ext_latin-regular.woff",
                "woff2": basepath + "/ubuntu-v15-latin-ext_latin-regular.woff2",
            },
            "bold": {
                "truetype": basepath + "/ubuntu-v15-latin-ext_latin-700.ttf",
                "woff": basepath + "/ubuntu-v15-latin-ext_latin-700.woff",
                "woff2": basepath + "/ubuntu-v15-latin-ext_latin-700.woff2",
            },
            "italic": {
                "truetype": basepath + "/ubuntu-v15-latin-ext_latin-italic.ttf",
                "woff": basepath + "/ubuntu-v15-latin-ext_latin-italic.woff",
                "woff2": basepath + "/ubuntu-v15-latin-ext_latin-italic.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/ubuntu-v15-latin-ext_latin-700italic.ttf",
                "woff": basepath + "/ubuntu-v15-latin-ext_latin-700italic.woff",
                "woff2": basepath + "/ubuntu-v15-latin-ext_latin-700italic.woff2",
            },
        },
        "Space Mono": {
            "regular": {
                "truetype": basepath + "/space-mono-v10-latin-ext_latin-regular.ttf",
                "woff": basepath + "/space-mono-v10-latin-ext_latin-regular.woff",
                "woff2": basepath + "/space-mono-v10-latin-ext_latin-regular.woff2",
            },
            "bold": {
                "truetype": basepath + "/space-mono-v10-latin-ext_latin-700.ttf",
                "woff": basepath + "/space-mono-v10-latin-ext_latin-700.woff",
                "woff2": basepath + "/space-mono-v10-latin-ext_latin-700.woff2",
            },
            "italic": {
                "truetype": basepath + "/space-mono-v10-latin-ext_latin-italic.ttf",
                "woff": basepath + "/space-mono-v10-latin-ext_latin-italic.woff",
                "woff2": basepath + "/space-mono-v10-latin-ext_latin-italic.woff2",
            },
            "bolditalic": {
                "truetype": basepath + "/space-mono-v10-latin-ext_latin-700italic.ttf",
                "woff": basepath + "/space-mono-v10-latin-ext_latin-700italic.woff",
                "woff2": basepath + "/space-mono-v10-latin-ext_latin-700italic.woff2",
            },
        },
    }
