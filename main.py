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


@rt("/")
def get_homepage():
    return (
        Body()(
            Main(
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
                        P(cls="text-2xl text-center font-rest leading-relaxed text-[#006478] font-[400px]")(
                            "Discover the inspiring teachers and experts who will guide you through mindfulness, inner peace, and self-discovery"
                        )
                    ),

                    # Div(cls="mt-16 w-[384px] md:w-[1552px] md:flex flex-col items-center justify-center relative")(
                    #     Div(
                    #         Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                    #             cls="flex justify-center"),
                    #         Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                    #             cls="flex justify-center"),
                    #         Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                    #             cls="flex justify-center"),
                    #         Div(Img(src="static/img/speaker.png", cls="w-[60px] hidden lg:w-[180px] h-auto object-cover"),
                    #             cls="flex justify-center"),
                    #         cls="grid grid-cols-3 lg:grid-cols-4 gap-6 md:gap-15"
                    #     ),
                    #
                    #     # Second row - 3 cols on large screens, 2 cols on smaller screens
                    #     Div(
                    #         Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                    #             cls="flex justify-center"),
                    #         Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                    #             cls="flex justify-center"),
                    #         Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                    #             cls="flex justify-center"),
                    #         cls="grid grid-cols-2 lg:grid-cols-3 gap-2 md:gap-15"
                    #     ),
                    # ),

                    Div(cls="mt-40 w-[384px] md:w-[1552px]")(
                        # First row - 3 cols on small screens, 4 cols on large screens
                        Div(cls="grid grid-cols-3 lg:grid-cols-4")(
                            # First 3 speakers (visible on all screens)
                            *[Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                                  cls="flex justify-center")
                              for _ in range(3)],

                            # 4th speaker (only visible on large screens)
                            Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                                cls="hidden lg:flex justify-center"),
                        ),

                        # Second row (flex container with justify-center for small screens)
                        Div(cls="flex flex-wrap justify-center lg:grid lg:grid-cols-3")(
                            # On small screens, these 2 items will be centered
                            # On large screens, they'll be part of a 3-column grid
                            Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                                cls="flex justify-center lg:mx-0"),
                            Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                                cls="flex justify-center lg:mx-0"),

                            # 3rd speaker in second row (only visible on large screens)
                            Div(Img(src="static/img/speaker.png", cls="w-[60px] lg:w-[180px] h-auto object-cover"),
                                cls="hidden lg:flex justify-center"),
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


                ),

            ),

        )

    )



serve()