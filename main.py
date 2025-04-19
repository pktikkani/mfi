from fasthtml.common import *

hdrs = (
    Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    Meta(
        name="description",
        content="Fun and enriching yoga summer camp for kids in Bangalore. Combining mindfulness, movement, and play to nurture children's physical and emotional wellbeing. Ages 5-12."
    ),
    Link(rel="stylesheet", href="/static/output.css", type="text/css"),
)

app, rt = fast_app(hdrs=hdrs, pico=False, live=False)

def meditation_button(additional_classes=""):
    """Helper function to avoid button style duplication"""
    base_classes = "bg-[#1DB0CD] hover:bg-[#19a0bb] text-white font-medium py-3 px-3 rounded-md transition duration-300 h-12 w-44 text-sm"
    return Button(cls=f"{base_classes} {additional_classes}")("Join Meditate for India")



navbar = Nav(cls="hidden bg-[#F4F8F9] shadow-sm py-4 md:flex border-0")(
        Div(cls="mt-6 container m-0 flex justify-between min-w-full")(
            # Left navigation items
            Div(cls="px-6 flex bg-[#F4F8F9] space-x-8 ")(
                A("Home", href="#", cls="text-gray-800 hover:text-blue-600 font-medium"),
                A("Join the event", href="#", cls="text-gray-800 hover:text-blue-600 font-medium"),
                A("Become a Partner", href="#", cls="text-gray-800 hover:text-blue-600 font-medium"),
                A("About Us", href="#", cls="text-gray-800 hover:text-blue-600 font-medium"),
                A("FAQ", href="#", cls="text-gray-800 hover:text-blue-600 font-medium"),
            ),
            # Login link
            A("Login/ Sign up", href="#", cls="text-gray-800 hover:text-blue-600 font-medium px-6")
        )
    )


@rt("/")
def get_homepage():
    return (

        Body()(
            Main(
                # Navigation bar with bottom shadow
                # Navigation bar - desktop only with proper alignment
                # Navigation bar with extreme left and right positioning
                # Navigation bar with extreme left and right positioning

                navbar,
                Div(cls="w-full flex flex-col items-center justify-center mt-16")(

                    Div(cls="relative w-full flex flex-col items-center justify-center")(
                        Img(cls="md:w-auto md:h-auto hidden md:block", src='static/img/meditation-desktop.png',
                            alt="mfi-desktop"),
                        Img(cls="w-98 md:hidden", src='static/img/meditation-mobile.png', alt="mfi-mobile"),
                        H1(cls="absolute text-[#004552] text-center text-4xl -top-5 ml-3.5 md:text-[64px] md:top-4 md:mt-18 md:-mr-12 font-heading")(
                            "Meditate for India"),
                        Div(cls="absolute flex flex-col text-sm items-center justify-center mt-[9rem] md:mt-80 md:text-xl text-center")(
                            P(cls="text-teal-800 text-center font-sans max-w-prose leading-relaxed md:mt-32")
                                (
                                Span(cls="block font-heading md:text-[26px]")("A Free Global 24-Hour Immersion in"),
                                Span(cls="block font-heading md:text-[26px]")(
                                    "Meditation, Pranayama, Asana and Chanting"),
                                Span(cls="block font-bold pt-1 md:text-[24px] md:pt-4")("21st June 2025 From: time")
                            ),

                            meditation_button("hidden md:block mt-4 md:text-[14px] md:w-52")
                        ),
                        meditation_button("block md:hidden mt-4"),
                    ),
                    Div(cls="mt-16 w-full flex items-center justify-center gap-12 lg:gap-50")(
                        Div(cls="flex flex-col items-center justify-center")(
                            Img(cls="md:w-25 md:h-25 w-12 h-12", src='static/img/imagine-desktop.png', alt="imagine")(),
                            P(cls="text-xs md:text-xl text-center text-slate-700")(
                                Span(cls="block")("Reimagining a"),
                                Span(cls="block")("Mindful India")
                            ),
                            P(cls="text-xs m-2 md:text-lg text-slate-600 text-center")(
                                Span(cls="block")("पुनर्नि र्निर्मा मः"),
                                Span(cls="block")("मनस्वीं भारतम्")
                            )
                        ),
                        Div(cls="flex flex-col items-center justify-center")(
                            Img(cls="md:w-25 md:h-25 w-12 h-12", src='static/img/celebrate.svg', alt="celebrate")(),
                            P(cls="text-xs md:text-xl text-center text-slate-700")(
                                Span(cls="block")("Celebrating"),
                                Span(cls="block")("Our Heritage")
                            ),
                            P(cls="text-xs md:text-lg text-slate-600 text-center m-2")(
                                Span(cls="block")("उत्सवामः"),
                                Span(cls="block")("स्वधर्म मंम")
                            )
                        ),
                        Div(cls="flex flex-col items-center justify-center")(
                            Img(cls="md:w-25 md:h-25 w-12 h-12", src='static/img/cultivate-desktop.png',
                                alt="cultivate")(),
                            P(cls=" text-xs md:text-xl text-center text-slate-700")(
                                Span(cls="block")("Cultivating"),
                                Span(cls="block")("Inner Wisdom")
                            ),
                            P(cls="text-xs md:text-lg text-slate-600 text-center m-2")(
                                Span(cls="block")("अन्तः"),
                                Span(cls="block")("प्रज्ञा संवर्धनम्"),
                            )
                        ),
                    ),
                    Div(cls="mt-16 w-[370px] md:w-[1088px] flex flex-col items-center justify-center gap-10 content-center")(
                        Img(cls="md:w-auto md:h-auto hidden md:block", src='static/img/meditate-desktop.svg',
                            alt="meditate2.0-desktop"),
                        Img(cls="md:hidden w-60", src='static/img/meditate.svg', alt="meditate2.0-mobile"),
                        Div(cls="w-[370px] md:w-[1034px] flex flex-col items-center justify-center gap-10 content-center")(
                            H1(cls="font-heading font-[400px] text-[24px] md:text-[32px] text-center text-[#004552]")(
                                "A Movement Rooted in Tradition"),
                            P(cls="m-2 text-base text-[16px] md:text-[24px] text-center font-rest leading-relaxed text-[#006478] font-normal")(
                                B("Meditate for India", cls="font-bold font-rest md:text-[24px]"),
                                " is more than just an event; it is a collective movement to bring India's ancient wisdom into modern life. The first Meditate for India was held during the ",
                                B("COVID-19 pandemic, offering thousands a space for healing, "
                                  "resilience, and connection",
                                  cls="font-bold font-rest md:text-[24px]"),
                            ),

                            P(cls="m-2 text-[16px] md:text-[24px] text-base text-center font-rest leading-relaxed text-[#006478] font-normal")(
                                "Now, we come together again not in response to crisis, but as a ",
                                B("step toward cultivating lasting well-being.",
                                  cls="font-bold font-rest md:text-[24px]"),
                                " Meditation is not just an individual practice; "
                                "it is a shared journey that uplifts communities and strengthens societies."
                            ),
                            P(cls="m-2 text-[16px] md:text-[24px] text-base text-center font-rest leading-relaxed text-[#006478] font-normal")(
                                "This year, Meditate for India will be held ",
                                B("online and in-person ", cls="font-bold font-rest md:text-[24px] leading-relaxed"),
                                " across cities worldwide. Whether you join from ",
                                B("home, a yoga Shala,", cls="font-bold font-rest md:text-[24px] leading-relaxed"),
                                "or a meditation center, you will be part of a global wave of stillness, breath, and sound."
                            )
                        ),
                    ),
                    Div(cls="mt-16 w-[404px] md:w-[1920px] flex flex-col items-center justify-center gap-10")(
                        Img(
                            src="static/img/reason-mobile.svg",
                            alt="Meditate for India Infographic",
                            cls="w-full block md:hidden"
                        ),
                        Img(
                            src="static/img/reasons.svg",
                            alt="Meditate for India Infographic",
                            cls="w-full hidden md:block"
                        ),

                    ),
                    Div(cls="mt-16 w-384px md:w-[994px] flex flex-col items-center justify-center gap-10")(
                        H1(cls="font-heading text-2xl md:text-[64px] text-center text-[#004552]")(
                            "Wisdom Form Our Speakers"),
                        P(cls="md:text-2xl text-[16px] text-center font-rest leading-relaxed text-[#006478] font-[400px]")(
                            "Discover the inspiring teachers and experts who will guide you through mindfulness, inner peace, and self-discovery"
                        )
                    ),

                    # Speakers section
                    Div(cls="mt-40 container mx-auto px-4")(
                        # Desktop layout (7 speakers) - hidden on mobile
                        Div(cls="hidden md:block")(
                            # First row - 4 speakers
                            Div(cls="grid grid-cols-4 gap-8 mb-8")(
                                *[Div(cls="flex flex-col items-center")(
                                    Div(cls="w-44 h-44 rounded-full overflow-hidden mb-4")(
                                        Img(src="static/img/speaker.png", cls="w-full h-full object-cover")
                                    ),
                                    P(cls="text-center font-[500px] text-xl text-[#006478] mb-1")("Sri Kunal Kendurkar"),
                                    P(cls="text-center text-lg text-[#006478]")("Yoga Coach")
                                ) for _ in range(4)],
                            ),

                            # Second row - 3 speakers (centered)
                            Div(cls="grid grid-cols-3 gap-8 mx-auto w-3/4")(
                                *[Div(cls="flex flex-col items-center")(
                                    Div(cls="w-44 h-44 rounded-full overflow-hidden mb-4")(
                                        Img(src="static/img/speaker.png", cls="w-full h-full object-cover")
                                    ),
                                    P(cls="text-center font-[500px] text-xl text-[#006478] mb-1")("Sri Kunal Kendurkar"),
                                    P(cls="text-center text-lg text-[#006478]")("Yoga Coach")
                                ) for _ in range(3)],
                            ),
                        ),

                        # Mobile layout (5 speakers) - hidden on desktop
                        Div(cls="md:hidden")(
                            # First row - 3 speakers
                            Div(cls="flex justify-center gap-2 mb-4")(
                                *[Div(cls="flex flex-col items-center")(
                                    Div(cls="w-24 h-24 rounded-full overflow-hidden mb-2")(
                                        Img(src="static/img/speaker.png", cls="w-full h-full object-cover")
                                    ),
                                    P(cls="text-center font-[500px] text-sm text-[#006478] mb-0.5")(
                                        "Sri Kunal Kendurkar"),
                                    P(cls="text-center text-xs text-[#006478]")("Yoga Coach")
                                ) for _ in range(3)],
                            ),

                            # Second row - 2 speakers (centered)
                            Div(cls="flex justify-center gap-2")(
                                *[Div(cls="flex flex-col items-center")(
                                    Div(cls="w-24 h-24 rounded-full overflow-hidden mb-2")(
                                        Img(src="static/img/speaker.png", cls="w-full h-full object-cover")
                                    ),
                                    P(cls="text-center font-[500px] text-sm text-[#006478] mb-0.5")(
                                        "Sri Kunal Kendurkar"),
                                    P(cls="text-center text-xs text-[#006478]")("Yoga Coach")
                                ) for _ in range(2)],
                            ),
                        ),
                    ),

                    Div(cls="mt-16 w-full hidden md:flex flex-col items-center justify-center gap-10 relative")(
                        Img(cls="md:w-auto md:h-auto hidden md:block", src='static/img/join-us-desktop.png',
                            alt="mfi-desktop"),
                        H1(cls="absolute text-center text-[64px] font-heading mt-60")("“Join Us”"),
                        P(cls="absolute text-center font-rest leading-relaxed text-2xl text-[#006478] font-normal mt-100")(
                            B("Online:"),
                            " Join live-streamed sessions from anywhere."
                        ),
                        P(cls="absolute text-center font-rest leading-relaxed text-2xl text-[#006478] font-normal mt-120")(
                            B("In-Person:"),
                            " Attend a gathering at a partner yoga shala or meditation center."
                        ),
                        meditation_button("absolute hidden mt-160 md:block md:text-base md:w-52")
                    ),

                    # Footer section with shadow at the top
                    Div(cls="mt-16 hidden md:block w-full bg-[#F4F8F9] py-10 relative")(
                        # Shadow element positioned at the top of the footer
                        Div(cls="absolute top-0 left-0 right-0 h-4 shadow-[0_-2px_4px_rgba(0,0,0,0.1)] pointer-events-none"),

                        Div(cls="container mx-auto px-4 flex flex-col md:flex-row justify-between")(
                            # Left column - Brand and tagline
                            Div(cls="mb-8 md:mb-0")(
                                H2(cls="text-xl font-medium mb-2")("The Mindful Initiative | Ashtanga Yoga"),
                                P(cls="text-gray-700")("Helping People to be more Mindful and Compassionate Since 2017")
                            ),

                            # Center column - Contact information
                            Div(cls="mb-8 md:mb-0")(
                                H3(cls="text-lg font-medium mb-4")("Contact"),
                                P(cls="flex items-center mb-2")(
                                    Span(cls="mr-2")("✉️"), "info@themindfulinitiative.com"
                                ),
                                P(cls="flex items-center mb-2")(
                                    Span(cls="mr-2")("📞"), "+91 9535 4186 04"
                                ),
                                P(cls="flex items-start")(
                                    Span(cls="mr-2")("📍"),
                                    Span()(
                                        "87, 3rd Main, 4th Phase, Dollars Layout, JP Nagar 7th Phase, Bengaluru, Karnataka 560078")
                                )
                            ),

                            # Social media column
                            Div(cls="mb-8 md:mb-0")(
                                H3(cls="text-lg font-medium mb-4")("Social media"),
                                P(cls="flex items-center mb-2")(
                                    Span(cls="mr-2")("📷"), "Instagram"
                                ),
                                P(cls="flex items-center mb-2")(
                                    Span(cls="mr-2")("💼"), "LinkedIn"
                                ),
                                P(cls="flex items-center mb-2")(
                                    Span(cls="mr-2")("🐦"), "Twitter"
                                )
                            ),

                            # Legal column
                            Div()(
                                H3(cls="text-lg font-medium mb-4")("Legal"),
                                P(cls="mb-2")("Terms and conditions"),
                                P(cls="mb-2")("Privacy policy"),
                                P(cls="mb-2")("Cookies policy")
                            )
                        ),

                        # Copyright section
                        Div(cls="container mx-auto px-4 mt-8 pt-4 border-t border-gray-300")(
                            P(cls="text-sm text-gray-600")("The Mindful Initiative. All rights reserved.")
                        )
                    )

                ),

            ),

        )

    )



serve()