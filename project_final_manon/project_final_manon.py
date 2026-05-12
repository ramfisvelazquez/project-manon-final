"""
Stitch Fix Landing Page — Reflex replica
Single-file, ready to run.
"""

import reflex as rx

from project_final_manon.women import women
from project_final_manon.men import men
from project_final_manon.kids import kids

import json
# ─────────────────────────────────────────────
# DESIGN TOKENS
# ─────────────────────────────────────────────
CORAL = "#E8514A"
CORAL_DARK = "#C93F38"
BLACK = "#1A1A1A"
GRAY = "#555555"
LIGHT_GRAY = "#F7F7F7"
BORDER_GRAY = "#E0E0E0"
WHITE = "#FFFFFF"
YELLOW_HL = "#F5E642"

FONT_SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"

with open("brands.json", "r") as f:
    BRANDS = json.load(f)

# Placeholder image service
def img(w: int, h: int, seed: str = "sf") -> str:
    return f"https://picsum.photos/seed/{seed}/{w}/{h}"


# ─────────────────────────────────────────────
# 1. NAVBAR
# ─────────────────────────────────────────────
def nav_link(label: str) -> rx.Component:
    return rx.link(
        label,
        href="#",
        color=BLACK,
        font_size="0.82rem",
        font_weight="500",
        letter_spacing="0.04em",
        text_decoration="none",
        padding_x="0.6rem",
        _hover={"color": CORAL},
        font_family=FONT_SANS,
    )


def nav_link_secondary(label: str) -> rx.Component:
    return rx.link(
        label,
        href="#",
        color=GRAY,
        font_size="0.78rem",
        font_weight="400",
        text_decoration="none",
        padding_x="0.5rem",
        _hover={"color": CORAL},
        font_family=FONT_SANS,
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            # Logo
            rx.text(
                "STITCH FIX",
                font_size="1.1rem",
                font_weight="800",
                letter_spacing="0.12em",
                color=BLACK,
                font_family=FONT_SANS,
            ),
            # Primary nav links
            rx.flex(
                rx.button("Women",
                          background=WHITE,
                         on_click=rx.scroll_to("categoria"),
                         color="BLACK",
                         _hover={
        "background": "#c98f8f",
        "border": "2px solid #c98f8f",
        "color": "white",}
                           ),
                rx.button("Men",
                          background=WHITE,
                         on_click=rx.scroll_to("categoria"),
                         color="BLACK",
                         _hover={
        "background": "#c98f8f",
        "border": "2px solid #c98f8f",
        "color": "white",}
        ),
                rx.button("Kids",
                          background=WHITE,
                         on_click=rx.scroll_to("categoria"),
                         color="BLACK",
                         _hover={
        "background": "#c98f8f",
        "border": "2px solid #c98f8f",
        "color": "white",}
        ),
                align="center",
                gap="0.2rem",
                margin_left="2rem",
                on_click=rx.scroll_to("categorias"),
            ),
            # Spacer
            rx.box(flex="1"),
            # Secondary nav links
            rx.flex(
                nav_link_secondary("Style Guide"),
                nav_link_secondary("FAQ"),
                nav_link_secondary("Gift Cards"),
                align="center",
                gap="0.2rem",
            ),
            # Sign In button
            rx.button(
                "Sign In",
                border="1px solid",
                border_color=BORDER_GRAY,
                background=WHITE,
                color=BLACK,
                font_size="0.78rem",
                font_family=FONT_SANS,
                font_weight="500",
                padding_x="1rem",
                padding_y="0.35rem",
                border_radius="3px",
                cursor="pointer",
                margin_left="0.8rem",
                _hover={"background": LIGHT_GRAY},
            ),
            align="center",
            width="100%",
        ),
        width="100%",
        padding_x="2rem",
        padding_y="0.7rem",
        background=WHITE,
        border_bottom=f"1px solid {BORDER_GRAY}",
        position="sticky",
        top="0",
        z_index="100",
    )


# ─────────────────────────────────────────────
# 2. HERO SECTION
# ─────────────────────────────────────────────
def hero() -> rx.Component:
    return rx.box(
        # Background image layer
        rx.image(
            src=img(1400, 620, "hero-style"),
            width="100%",
            height="100%",
            object_fit="cover",
            position="absolute",
            top="0",
            left="0",
        ),
        # Dark overlay
        rx.box(
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background="rgba(0,0,0,0.32)",
        ),
        # Content
        rx.flex(
            rx.vstack(
                rx.heading(
                    "Personal Styling",
                    font_size=["2rem", "2.8rem", "3.4rem"],
                    font_weight="700",
                    color=WHITE,
                    text_align="center",
                    line_height="1.15",
                    font_family=FONT_SANS,
                ),
                rx.heading(
                    "for Everybody",
                    font_size=["2rem", "2.8rem", "3.4rem"],
                    font_weight="700",
                    color=WHITE,
                    text_align="center",
                    line_height="1.15",
                    font_family=FONT_SANS,
                ),
                rx.button(
                    "TAKE YOUR STYLE QUIZ →",
                    background=CORAL,
                    color=WHITE,
                    font_size="0.78rem",
                    font_family=FONT_SANS,
                    font_weight="700",
                    letter_spacing="0.08em",
                    padding_x="2rem",
                    padding_y="0.7rem",
                    border_radius="3px",
                    margin_top="1.4rem",
                    cursor="pointer",
                    border="none",
                    _hover={"background": CORAL_DARK},
                ),
                align="center",
                spacing="1",
            ),
            justify="center",
            align="center",
            position="absolute",
            top="0",
            left="0",
            width="100%",
            height="100%",
        ),
        position="relative",
        width="100%",
        height=["340px", "440px", "580px"],
        overflow="hidden",
    )


# ─────────────────────────────────────────────
# 3. CATEGORIES SECTION
# ─────────────────────────────────────────────
def category_card(label: str, seed: str, link: str) -> rx.Component:
    return rx.box(
        rx.image(
            src=img(400, 480, seed),
            width="100%",
            height="360px",
            object_fit="cover",
            border_radius="4px",
        ),

        rx.box(
            rx.link(
                f"{label} →",
                href=link,
                font_size="0.82rem",
                font_weight="600",
                color=BLACK,
                text_decoration="none",
                font_family=FONT_SANS,
                letter_spacing="0.04em",
                _hover={"color": CORAL},
            ),
            background=WHITE,
            padding_x="0.9rem",
            padding_y="0.5rem",
            position="absolute",
            bottom="12px",
            left="12px",
            border_radius="2px",
            box_shadow="0 1px 4px rgba(0,0,0,0.15)",
        ),

        position="relative",
        overflow="hidden",
        border_radius="4px",
        _hover={
            "transform": "scale(1.015)",
            "transition": "transform 0.25s ease",
        },
        cursor="pointer",
    )

def categories_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "We'll Find Style For Your Life",
                font_size=["1.4rem", "1.8rem"],
                font_weight="700",
                color=BLACK,
                text_align="center",
                font_family=FONT_SANS,
            ),
            rx.text(
                "With clothing hand selected by our expert stylists for your unique size & style, you'll\nalways look and feel your best. No subscription required.",
                font_size="0.9rem",
                color=GRAY,
                text_align="center",
                max_width="520px",
                line_height="1.6",
                font_family=FONT_SANS,
            ),
            rx.grid(
    category_card("Women", "woman-fashion", "/women"),
    category_card("Men", "man-fashion", "/men"),
    category_card("Kids", "kids-fashion", "/kids"),
    columns="3",
    gap="1.2rem",
    width="100%",
    margin_top="1.5rem",
),
            align="center",
            spacing="4",
            width="100%",
        ),
        max_width="1100px",
        margin="0 auto",
        padding_x="2rem",
        padding_y="4rem",
        id="categoria"
    )


# ─────────────────────────────────────────────
# 4. HOW IT WORKS (Info Section)
# ─────────────────────────────────────────────
def info_column(title: str, highlight: str, body: str, is_bold_title: bool = True) -> rx.Component:
    return rx.vstack(
        rx.text(
            title,
            font_size="0.88rem",
            font_weight="700" if is_bold_title else "400",
            color=BLACK,
            text_align="center",
            font_family=FONT_SANS,
            as_="span",
        ),
        rx.text(
            body,
            font_size="0.84rem",
            color=GRAY,
            text_align="center",
            line_height="1.6",
            font_family=FONT_SANS,
        ),
        align="center",
        spacing="2",
        flex="1",
        padding_x="1rem",
    )


def info_section() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                rx.heading(
                    "How Stitch Fix Works",
                    font_size=["1.3rem", "1.7rem"],
                    font_weight="700",
                    color=BLACK,
                    text_align="center",
                    font_family=FONT_SANS,
                ),
                rx.flex(
                    info_column(
                        "Tell us your price range,",
                        "",
                        "size & style. You'll pay just a $20 styling fee, which gets credited toward pieces you keep.",
                    ),
                    rx.box(
                        width="1px",
                        height="80px",
                        background=BORDER_GRAY,
                        align_self="center",
                        display=["none", "block"],
                    ),
                    info_column(
                        "Get a Fix when you want.",
                        "",
                        "Try on pieces at home before you buy. Keep your favorites, send back the rest.",
                    ),
                    rx.box(
                        width="1px",
                        height="80px",
                        background=BORDER_GRAY,
                        align_self="center",
                        display=["none", "block"],
                    ),
                    info_column(
                        "Free shipping, returns & exchanges",
                        "",
                        "—a prepaid return envelope is included. There are no hidden fees, ever.",
                    ),
                    direction="row",
                    gap="0",
                    width="100%",
                    margin_top="1.5rem",
                ),
                rx.flex(
                    rx.text(
                        "No subscription required.",
                        font_size="0.84rem",
                        font_weight="700",
                        color=BLACK,
                        background=YELLOW_HL,
                        padding_x="0.3rem",
                        font_family=FONT_SANS,
                    ),
                    rx.text(
                        " Try Stitch Fix once or set up automatic deliveries.",
                        font_size="0.84rem",
                        color=GRAY,
                        font_family=FONT_SANS,
                    ),
                    align="center",
                    justify="center",
                    flex_wrap="wrap",
                    margin_top="1.5rem",
                ),
                align="center",
                spacing="2",
                width="100%",
            ),
            background=WHITE,
            border=f"1px solid {BORDER_GRAY}",
            border_radius="6px",
            box_shadow="0 2px 12px rgba(0,0,0,0.06)",
            padding="2.5rem",
            max_width="960px",
            margin="0 auto",
            width="100%",
        ),
        padding_x="2rem",
        padding_y="3rem",
        background=LIGHT_GRAY,
        width="100%",
    )


# ─────────────────────────────────────────────
# 5. GALLERY SECTION
# ─────────────────────────────────────────────
def gallery_section() -> rx.Component:
    images = [
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "https://images.unsplash.com/photo-1517841905240-472988babdf9",
        "https://images.unsplash.com/photo-1494526585095-c41746248156",
        "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
        "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
        "https://images.unsplash.com/photo-1493246318656-5bfd4cfb29b8",
    ]

    all_images = images + images

    return rx.box(
        rx.vstack(
            rx.heading(
                "Endless styles for your best fit",
                font_size="2.3rem",
                font_weight="700",
                color="#111",
                text_align="center",
            ),

            rx.text(
                "Your stylist gets to know you, discovering your perfect fit from limitless style options.",
                font_size="1rem",
                color="#666",
                text_align="center",
                max_width="700px",
            ),

            rx.box(
                rx.hstack(
                    *[
                        rx.image(
                            src=img,
                            width="230px",
                            height="290px",
                            object_fit="cover",
                            border_radius="10px",
                            flex_shrink="0",
                        )
                        for img in all_images
                    ],
                    spacing="4",
                    class_name="infinite-scroll",
                ),
                overflow="hidden",
                width="100%",
                padding_top="2rem",
            ),

            spacing="4",
            align="center",
            width="100%",
        ),

        width="100%",
        padding="5rem 3rem",
        background="#F5F5F5",

        style={
            "@keyframes scrollLeft": {
                "0%": {
                    "transform": "translateX(0)",
                },
                "100%": {
                    "transform": "translateX(-50%)",
                },
            },

            ".infinite-scroll": {
                "display": "flex",
                "width": "max-content",
                "animation": "scrollLeft 30s linear infinite",
            },
        },
    )

# ─────────────────────────────────────────────
# 6. BRANDS SECTION
# ─────────────────────────────────────────────


def brand_logo(brand: dict) -> rx.Component:
    return rx.box(
        rx.image(
            src=brand["logo"],
            width="120px",
            height="40px",
            object_fit="contain",
            filter="brightness(1)",
        ),
        display="flex",
        align_items="center",
        justify_content="center",
        padding="1rem",
        min_width="140px",
    )


def brands_section() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "1,000+ top brands",
                font_size=["1.3rem", "1.7rem"],
                font_weight="700",
                color=BLACK,
                text_align="center",
                font_family=FONT_SANS,
            ),
            rx.text(
                "Women's sizes 0-24W (XS-3X)—Plus, Petite and Maternity",
                font_size="0.82rem",
                color=GRAY,
                text_align="center",
                font_family=FONT_SANS,
            ),
            rx.text(
                "Men's sizes XS-3XL, waists 28-48\" and inseams 28-36\"—including Big & Tall",
                font_size="0.82rem",
                color=GRAY,
                text_align="center",
                font_family=FONT_SANS,
            ),
            rx.flex(
                *[brand_logo(brand) for brand in BRANDS],
                flex_wrap="wrap",
                justify="center",
                gap="0.4rem",
                width="100%",
                margin_top="1.5rem",
            ),
            align="center",
            spacing="2",
            width="100%",
        ),
        max_width="1000px",
        margin="0 auto",
        padding_x="2rem",
        padding_y="3.5rem",
    )


# ─────────────────────────────────────────────
# 7. FINAL CTA
# ─────────────────────────────────────────────
def final_cta() -> rx.Component:
    return rx.box(
        rx.box(
            rx.vstack(
                rx.heading(
                    "Ready to Sign Up?",
                    font_size=["1.3rem", "1.6rem"],
                    font_weight="700",
                    color=BLACK,
                    text_align="center",
                    font_family=FONT_SANS,
                ),
                rx.button(
                    "TAKE YOUR STYLE QUIZ →",
                    background=CORAL,
                    color=WHITE,
                    font_size="0.78rem",
                    font_family=FONT_SANS,
                    font_weight="700",
                    letter_spacing="0.08em",
                    padding_x="2rem",
                    padding_y="0.75rem",
                    border_radius="3px",
                    cursor="pointer",
                    border="none",
                    margin_top="0.5rem",
                    _hover={"background": CORAL_DARK},
                ),
                rx.flex(
                    rx.text(
                        "Already have an account? ",
                        font_size="0.82rem",
                        color=GRAY,
                        font_family=FONT_SANS,
                    ),
                    rx.link(
                        "Sign in »",
                        href="#",
                        font_size="0.82rem",
                        color="blue",
                        font_family=FONT_SANS,
                        text_decoration="none",
                        _hover={"text_decoration": "underline"},
                    ),
                    align="center",
                ),
                align="center",
                spacing="3",
                width="100%",
            ),
            background=WHITE,
            border=f"1px solid {BORDER_GRAY}",
            border_radius="6px",
            box_shadow="0 2px 10px rgba(0,0,0,0.05)",
            padding="2.5rem 3rem",
            max_width="520px",
            margin="0 auto",
            width="100%",
        ),
        padding_x="2rem",
        padding_y="3rem",
        background=LIGHT_GRAY,
        width="100%",
    )


# ─────────────────────────────────────────────
# 8. FOOTER
# ─────────────────────────────────────────────
def footer_col(title: str, links: list[str]) -> rx.Component:
    return rx.vstack(
        rx.text(
            title,
            font_size="0.72rem",
            font_weight="700",
            color=BLACK,
            letter_spacing="0.08em",
            font_family=FONT_SANS,
            margin_bottom="0.4rem",
        ),
        *[
            rx.link(
                lnk,
                href="#",
                font_size="0.78rem",
                color=GRAY,
                font_family=FONT_SANS,
                text_decoration="none",
                _hover={"color": CORAL},
                line_height="1.9",
            )
            for lnk in links
        ],
        align="start",
        spacing="0",
    )


def footer() -> rx.Component:
    return rx.box(
        rx.box(
            # Top footer
            rx.flex(
                # Brand column
                rx.vstack(
                    rx.text(
                        "STITCH FIX",
                        font_size="1rem",
                        font_weight="800",
                        letter_spacing="0.12em",
                        color=BLACK,
                        font_family=FONT_SANS,
                    ),
                    rx.flex(
                        rx.text("🇺🇸", font_size="0.9rem"),
                        rx.text(
                            "United States ∨",
                            font_size="0.78rem",
                            color=GRAY,
                            font_family=FONT_SANS,
                        ),
                        align="center",
                        gap="0.3rem",
                    ),
                    rx.box(
                        rx.text(
                            "⬇ App Store",
                            font_size="0.75rem",
                            color=WHITE,
                            font_family=FONT_SANS,
                            font_weight="600",
                        ),
                        background=BLACK,
                        padding_x="1rem",
                        padding_y="0.45rem",
                        border_radius="6px",
                        cursor="pointer",
                        margin_top="0.5rem",
                    ),
                    align="start",
                    spacing="3",
                    min_width="140px",
                ),
                footer_col(
                    "THE SERVICE",
                    ["Gift Cards", "iPhone App", "Plus Sizes", "Maternity",
                     "Petite", "Big & Tall", "Women's Jeans", "Business Casual"],
                ),
                footer_col(
                    "THE COMPANY",
                    ["About Us", "Press", "Investor Relations", "Careers", "Tech Blog"],
                ),
                footer_col(
                    "HAVE A QUESTION?",
                    ["FAQ", "Help"],
                ),
                rx.vstack(
                    rx.text(
                        "FOLLOW US",
                        font_size="0.72rem",
                        font_weight="700",
                        color=BLACK,
                        letter_spacing="0.08em",
                        font_family=FONT_SANS,
                        margin_bottom="0.4rem",
                    ),
                    rx.flex(
                        *[
                            rx.box(
                                rx.hstack(
                                    rx.link(
    rx.image(
        src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSUJxiJCf8DG8a-_oFjLqIU7Y2AMXggRdgotA&s",
        width="25px",
        height="25px",
        object_fit="cover",
        border_radius="50px",
        flex_shrink="0",
    ),
    href="https://facebook.com",
    is_external=True,
),
               rx.link(
    rx.image(
        src="https://e7.pngegg.com/pngimages/771/708/png-clipart-computer-icons-logo-instagram-logo-miscellaneous-text.png",
        width="25px",
        height="25px",
        object_fit="cover",
        border_radius="5px",
        flex_shrink="0",
    ),
    href="https://instagram.com",
    is_external=True,
),

rx.link(
    rx.image(
        src="data:image/png;base64,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",
        width="25px",
        height="25px",
        object_fit="cover",
        border_radius="5px",
        flex_shrink="0",
    ),
    href="https://pinterest.com",
    is_external=True,
),

rx.link(
    rx.image(
        src="data:image/png;base64,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",
        width="25px",
        height="25px",
        object_fit="cover",
        border_radius="5px",
        flex_shrink="0",
    ),
    href="https://twitter.com",
    is_external=True,
),

)
)

                        ],
                        gap="0.4rem",
                    ),
                    align="start",
                    spacing="2",
                ),
                gap=["1.5rem", "3rem"],
                flex_wrap="wrap",
                align="start",
                width="100%",
                padding_bottom="2rem",
            ),
            rx.divider(border_color=BORDER_GRAY, margin_y="0"),
            # Bottom legal bar
            rx.flex(
                rx.text(
                    "Stitch Fix and Fix are trademarks of Stitch Fix, Inc.",
                    font_size="0.7rem",
                    color="#999",
                    font_family=FONT_SANS,
                ),
                rx.flex(
                    *[
                        rx.link(
                            t,
                            href="#",
                            font_size="0.7rem",
                            color="#999",
                            font_family=FONT_SANS,
                            text_decoration="none",
                            _hover={"color": GRAY},
                        )
                        for t in ["Terms of Use", "Privacy Policy", "Sitemap",
                                  "Supply Chain Information", "Ad Choices"]
                    ],
                    gap="0.6rem",
                    flex_wrap="wrap",
                ),
                justify="between",
                align="center",
                flex_wrap="wrap",
                gap="0.5rem",
                padding_top="1rem",
            ),
            max_width="1100px",
            margin="0 auto",
            padding_x="2rem",
            padding_top="2.5rem",
            padding_bottom="1.5rem",
        ),
        background=WHITE,
        border_top=f"1px solid {BORDER_GRAY}",
        width="100%",
    )


# ─────────────────────────────────────────────
# PAGE INDEX
# ─────────────────────────────────────────────
def index() -> rx.Component:
    return rx.box(
        navbar(),
        hero(),
        categories_section(),
        info_section(),
        gallery_section(),
        brands_section(),
        final_cta(),
        footer(),
        background=WHITE,
        min_height="100vh",
        font_family=FONT_SANS,
    )


# ─────────────────────────────────────────────
# APP ENTRY POINT
# ─────────────────────────────────────────────
app = rx.App(
    style={
        "font_family": FONT_SANS,
        "background": WHITE,
        "*": {"box_sizing": "border-box"},
    }
)
app.add_page(index, route="/", title="Stitch Fix — Personal Styling for Everybody")
app.add_page(index)
app.add_page(women, route="/women")
app.add_page(men, route="/men")
app.add_page(kids, route="/kids")