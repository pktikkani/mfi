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
        Div(cls="mt-8 flex flex-col items-center justify-center relative")(
            Img(cls="md:max-w-3xl md:max-h-auto")(src='static/img/meditation.png'),
            H1(cls="absolute text-center text-3xl top-1 md:text-5xl md:top-6 md:mt-10 md:-mr-12")("Meditate for India"),
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



    )


serve()