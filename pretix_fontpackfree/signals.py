from django.dispatch import receiver

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
            }
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
            }
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
            }
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
            }
        },
    }
