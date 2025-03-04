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


@rt("/")
def get_homepage():
    return Main(
        Div(cls="flex flex-col items-center justify-center relative")(
            Img(cls="max-w-lg mx-auto md:max-w-5xl md:max-h-auto")(src='static/img/meditation.png'),
            H1(cls="absolute text-center text-4xl top-1 md:text-5xl md:top-10 md:mt-14 md:-ml-12")("Meditate for India"),
            Div(cls="absolute flex flex-col items-center justify-center mt-[11.5rem] md:mt-80 text-center")(
                P(cls="text-xl text-teal-800 text-center font-sans max-w-prose leading-loose")
                    (
                    Span(cls="block font-heading")("A Global 24-Hour Immersion in"),
                    Span(cls="block font-heading")("Meditation, Pranayama and Chanting"),
                    Span(cls="block font-bold")("21st June 2025 From: time")
                ),
            ),
            Button(
                cls="bg-[#1DB0CD] hover:bg-[#19a0bb] text-white font-medium py-3 px-6 rounded-md "
                    "transition duration-300 h-12;")
            ("Join Meditate for India"),

        ),



    )


serve()