from fasthtml.common import *

hdrs = (
    Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    Meta(
        name="description",
        content="Fun and enriching yoga summer camp for kids in Bangalore. Combining mindfulness, movement, and play to nurture children's physical and emotional wellbeing. Ages 5-12."
    ),
    Link(rel="stylesheet", href="/static/output.css", type="text/css"),
)

app, rt = fast_app(hdrs=hdrs, htmlkw={"data-theme": "fantasy"}, pico=False, live=False)

def meditation_button(additional_classes=""):
    """Helper function to avoid button style duplication"""
    base_classes = "bg-[#1DB0CD] hover:bg-[#19a0bb] text-white font-medium py-3 px-3 rounded-md transition duration-300 h-12 w-44 text-sm"
    return Button(cls=f"{base_classes} {additional_classes}")("Join Meditate for India")


@rt("/")
def get_homepage():
    return Main(
        Section(cls="mt-16 relative w-full flex flex-col items-center justify-center")(
            Img(cls="md:max-w-3xl md:max-h-auto")(src='static/img/meditation.png'),
            H1(cls="absolute text-center text-4xl -top-5 ml-3.5 md:text-5xl md:top-6 md:mt-10 md:-mr-12")("Meditate for India"),
            Div(cls="absolute flex flex-col text-sm items-center justify-center mt-[9rem] md:mt-80 md:text-xl text-center")(
                P(cls="text-teal-800 text-center font-sans max-w-prose leading-relaxed md:mt-10")
                    (
                    Span(cls="block font-heading")("A Free Global 24-Hour Immersion in"),
                    Span(cls="block font-heading")("Meditation, Pranayama, Asana and Chanting"),
                    Span(cls="block font-bold pt-1 md:pt-4")("21st June 2025 From: time")
                ),
                meditation_button("hidden md:block mt-4 md:text-base md:w-52")
            ),
            meditation_button("block md:hidden mt-4"),
        ),

        Section(cls="mt-16 w-full flex items-center justify-center")(
            Div(cls="flex justify-center")(
                Div(cls="flex flex-col items-center justify-center mx-6")(
                    Img(cls="md:w-14 md:m-8 w-6")(src='static/img/imagine.svg'),
                    P(cls="text-xs md:text-xl text-center text-slate-700")("Reimagining a Mindful India"),
                    P(cls="text-xs m-2 md:text-lg text-slate-600 text-center")("पुनर्निर्मिं मः मनस्वी भारतम्")
                ),
                Div(cls="flex flex-col items-center justify-center mx-6")(
                    Img(cls="md:w-14 md:m-8 w-6")(src='static/img/celebrate.svg'),
                    P(cls="text-xs md:text-xl text-center text-slate-700")("Celebrating Our Heritage"),
                    P(cls="text-xs md:text-lg text-slate-600 text-center m-2")("उत्सवामः स्वधर्म मंम")
                ),
                Div(cls="flex flex-col items-center justify-center mx-6")(
                    Img(cls="md:w-14 md:m-8 w-6")(src='static/img/cultivate.svg'),
                    P(cls=" text-xs md:text-xl text-center text-slate-700")("Cultivating Inner Wisdom"),
                    P(cls="text-xs md:text-lg text-slate-600 text-center m-2")("पालयामः अन्तःप्रज्ञाम्")
                ),

            )
        ),

    )

serve()