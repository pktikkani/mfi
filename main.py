from fasthtml.common import *
from fasthtml.components import Raw


hdrs = (
    Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    Meta(
        name="description",
        content="Fun and enriching yoga summer camp for kids in Bangalore. Combining mindfulness, movement, and play to nurture children's physical and emotional wellbeing. Ages 5-12."
    ),
    Link(rel="stylesheet", href="/static/output.css", type="text/css"),
)

app, rt = fast_app(hdrs=hdrs, pico=False, live=False)


# --- Helper Functions & Components ---

def meditation_button(additional_classes=""):
    """Helper function to avoid button style duplication"""
    base_classes = "bg-[#1DB0CD] hover:bg-[#19a0bb] text-white font-medium py-3 px-3 rounded-md transition duration-300 h-12 w-44 text-sm"
    return Button(cls=f"{base_classes} {additional_classes}")("Join Meditate for India")

# --- Responsive Navbar Components ---

def hamburger_button():
    """Creates the hamburger button visible only on mobile."""
    # SVG for hamburger icon
    hamburger_icon = Img(src="/static/img/hamburger.svg", alt="Menu", cls="w-6 h-6")
    # Button shown only below md breakpoint, triggers JS toggle function
    return Button(hamburger_icon,
                  cls="md:hidden p-2 text-gray-800 hover:bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500", # Added focus styles
                  onclick="toggleMenu()") # Simple JS toggle

def footer():
    return Div(cls="mt-16 hidden md:block w-full bg-[#F4F8F9] py-10 relative")(
                        # Shadow element positioned at the top of the footer
                        Div(cls="absolute top-0 left-0 right-0 h-4 shadow-[0_-2px_4px_rgba(0,0,0,0.1)] pointer-events-none"),

                        Div(cls="container mx-auto px-4 flex flex-col md:flex-row justify-between")(
                            # Left column - Brand and tagline
                            Div(cls="mb-8 md:mb-0")(
                                H2(cls="text-xl font-medium mb-2 text-gray-700")("The Mindful Initiative | Ashtanga Yoga"),
                                P(cls="text-gray-700")("Helping People to be more Mindful and Compassionate Since 2017")
                            ),

                            # Center column - Contact information
                            Div(cls="mb-8 md:mb-0")(
                                H3(cls="text-lg font-medium mb-4")("Contact"),
                                P(cls="flex items-center mb-2 text-gray-700")(
                                    Span(cls="mr-2 text-gray-700")("✉️"), "info@themindfulinitiative.com"
                                ),
                                P(cls="flex items-center mb-2 text-gray-700")(
                                    Span(cls="mr-2 text-gray-700")("📞"), "+91 9535 4186 04"
                                ),
                                P(cls="flex items-start")(
                                    Span(cls="mr-2 ")("📍"),
                                    Span(cls="text-gray-700")(
                                        "87, 3rd Main, 4th Phase, Dollars Layout, JP Nagar 7th Phase, Bengaluru, Karnataka 560078")
                                )
                            ),

                            # Social media column
                            Div(cls="mb-8 md:mb-0")(
                                H3(cls="text-lg font-medium mb-4 text-gray-700")("Social media"),
                                P(cls="flex items-center mb-2 text-gray-700")(
                                    Span(cls="mr-2 text-gray-700")("📷"), "Instagram"
                                ),
                                P(cls="flex items-center mb-2 text-gray-700")(
                                    Span(cls="mr-2 text-gray-700")("💼"), "LinkedIn"
                                ),
                                P(cls="flex items-center mb-2 text-gray-700")(
                                    Span(cls="mr-2 text-gray-700")("🐦"), "Twitter"
                                )
                            ),

                            # Legal column
                            Div()(
                                H3(cls="text-lg font-medium mb-4")("Legal"),
                                P(cls="mb-2 text-gray-700")("Terms and conditions"),
                                P(cls="mb-2 text-gray-700")("Privacy policy"),
                                P(cls="mb-2 text-gray-700")("Cookies policy")
                            )
                        ),

                        # Copyright section
                        Div(cls="container mx-auto px-4 mt-8 pt-4 border-t border-gray-300")(
                            P(cls="text-sm text-gray-600")("The Mindful Initiative. All rights reserved.")
                        )
    )



def mobile_menu():
    """Creates the mobile navigation menu, hidden by default."""
    # Define links for the mobile menu
    links = [
        A("Home", href="/", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("Join the event", href="/join-event", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("Become a Partner", href="#", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("About Us", href="/about-us", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("FAQ", href="#", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("Login/ Sign up", href="#", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded")
    ]
    # Mobile menu container, hidden by default, absolutely positioned
    return Div(*links,
               id="mobile-menu",
               # Initially hidden, shown only below md when toggled
               cls="hidden md:hidden fixed top-16 left-0 right-0 bg-[#F4F8F9] shadow-md flex-col p-4 space-y-1 z-50") # Adjusted top, space-y

def desktop_navbar():
    """The original navbar, now specifically for desktop (md and up)."""
    return Nav(cls="hidden md:flex space-x-8")( # Renamed variable, adjusted spacing
        A("Home", href="/", cls="text-gray-800 hover:text-blue-600 font-medium"),
        A("Join the event", href="/join-event", cls="text-gray-800 hover:text-blue-600 font-medium"),
        A("Become a Partner", href="#", cls="text-gray-800 hover:text-blue-600 font-medium"),
        A("About Us", href="/about-us", cls="text-gray-800 hover:text-blue-600 font-medium"),
        A("FAQ", href="#", cls="text-gray-800 hover:text-blue-600 font-medium"),
    )

# --- JavaScript for Toggle ---

toggle_script = Script("""
    function toggleMenu() {
        const menu = document.getElementById('mobile-menu');
        if (menu) { // Basic check if element exists
           menu.classList.toggle('hidden');
        }
    }
""")


header_container = Div(cls="bg-[#F4F8F9] shadow-sm")(
        # Added relative positioning for absolute mobile menu
        Div(cls="container mx-auto flex justify-between items-center p-4")(  # Inner container for alignment
            # Logo/Brand Name (visible on all screens)
            # Div(A("Meditate For India", href="/", cls="text-xl font-bold text-[#004552]")),

            # Desktop Navigation Links (hidden on mobile)
            desktop_navbar(),

            # Login Link for Desktop (hidden on mobile)
            A("Login/ Sign up", href="#", cls="hidden md:block text-gray-800 hover:text-blue-600 font-medium"),

            # Hamburger Button (visible on mobile)
            hamburger_button()
        ),
    )

@rt("/")
def get_homepage():
    # Header container holds logo, desktop nav, and hamburger button


    return (

        Body()(
            toggle_script,
            Main(
                header_container,
                mobile_menu(),
                Div(cls="w-full flex flex-col items-center justify-center mt-16")(

                    Div(cls="relative w-full flex flex-col items-center justify-center")(
                        Img(cls="md:w-auto md:h-auto hidden md:block", src='static/img/meditation-desktop.png',
                            alt="mfi-desktop"),
                        Img(cls="w-98 md:hidden", src='static/img/meditation-desktop.png', alt="mfi-mobile"),
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
                            P(cls="text-xs md:text-xl text-center text-[#004552]")(
                                Span(cls="block")("Reimagining a"),
                                Span(cls="block")("Mindful India")
                            ),
                            P(cls="text-xs m-2 md:text-lg text-[#004552] text-center")(
                                Span(cls="block")("पुनर्नि र्निर्मा मः"),
                                Span(cls="block")("मनस्वीं भारतम्")
                            )
                        ),
                        Div(cls="flex flex-col items-center justify-center")(
                            Img(cls="md:w-25 md:h-25 w-12 h-12", src='static/img/celebrate.svg', alt="celebrate")(),
                            P(cls="text-xs md:text-xl text-center text-[#004552]")(
                                Span(cls="block")("Celebrating"),
                                Span(cls="block")("Our Heritage")
                            ),
                            P(cls="text-xs md:text-lg text-[#004552] text-center m-2")(
                                Span(cls="block")("उत्सवामः"),
                                Span(cls="block")("स्वधर्म मंम")
                            )
                        ),
                        Div(cls="flex flex-col items-center justify-center")(
                            Img(cls="md:w-25 md:h-25 w-12 h-12", src='static/img/cultivate-desktop.png',
                                alt="cultivate")(),
                            P(cls=" text-xs md:text-xl text-center text-[#004552]")(
                                Span(cls="block")("Cultivating"),
                                Span(cls="block")("Inner Wisdom")
                            ),
                            P(cls="text-xs md:text-lg text-[#004552] text-center m-2")(
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
                            P(cls="m-2 text-base text-[16px] md:text-[24px] text-center font-rest leading-relaxed text-[#006478] font-extralight")(
                                B("Meditate for India", cls="font-bold font-rest md:text-[24px]"),
                                " is more than just an event; it is a collective movement to bring India's ancient wisdom into modern life. The first Meditate for India was held during the ",
                                B("COVID-19 pandemic, offering thousands a space for healing, "
                                  "resilience, and connection",
                                  cls="font-bold font-rest md:text-[24px]"),
                            ),

                            P(cls="m-2 text-[16px] md:text-[24px] text-base text-center font-rest leading-relaxed text-[#006478] font-extralight")(
                                "Now, we come together again not in response to crisis, but as a ",
                                B("step toward cultivating lasting well-being.",
                                  cls="font-bold font-rest md:text-[24px]"),
                                " Meditation is not just an individual practice; "
                                "it is a shared journey that uplifts communities and strengthens societies."
                            ),
                            P(cls="m-2 text-[16px] md:text-[24px] text-base text-center font-rest leading-relaxed text-[#006478] font-extralight")(
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
                        P(cls="md:text-2xl text-[16px] text-center font-rest leading-relaxed text-[#006478] font-extralight")(
                            "Discover the inspiring teachers and experts who will guide you through mindfulness, inner peace, and self-discovery"
                        )
                    ),

                    # Speakers section
                    Div(cls="mt-16 md:mt-40 container mx-auto px-4")(
                        # Desktop layout (7 speakers) - hidden on mobile
                        Div(cls="hidden md:block")(
                            # First row - 4 speakers
                            Div(cls="grid grid-cols-4 gap-8 mb-8")(
                                *[Div(cls="flex flex-col items-center")(
                                    Div(cls="w-44 h-44 rounded-full overflow-hidden mb-4")(
                                        Img(src="static/img/speaker.png", cls="w-full h-full object-cover")
                                    ),
                                    P(cls="text-center font-[500px] text-[24px] text-[#006478] mb-1")("Sri Kunal Kendurkar"),
                                    P(cls="text-center text-[24px] text-[#006478]")("Yoga Coach")
                                ) for _ in range(4)],
                            ),

                            # Second row - 3 speakers (centered)
                            Div(cls="grid grid-cols-3 gap-8 mx-auto w-3/4")(
                                *[Div(cls="flex flex-col items-center")(
                                    Div(cls="w-44 h-44 rounded-full overflow-hidden mb-4")(
                                        Img(src="static/img/speaker.png", cls="w-full h-full object-cover")
                                    ),
                                    P(cls="text-center font-[500px] text-[24px] text-[#006478] mb-1")("Sri Kunal Kendurkar"),
                                    P(cls="text-center text-[24px] text-[#006478]")("Yoga Coach")
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
                                    P(cls="text-center font-[500px] text-[12px] text-[#006478] mb-0.5")(
                                        "Sri Kunal Kendurkar"),
                                    P(cls="text-center text-[12px] text-[#006478]")("Yoga Coach")
                                ) for _ in range(3)],
                            ),

                            # Second row - 2 speakers (centered)
                            Div(cls="flex justify-center gap-2")(
                                *[Div(cls="flex flex-col items-center")(
                                    Div(cls="w-24 h-24 rounded-full overflow-hidden mb-2")(
                                        Img(src="static/img/speaker.png", cls="w-full h-full object-cover")
                                    ),
                                    P(cls="text-center font-[500px] text-[12px] text-[#006478] mb-0.5")(
                                        "Sri Kunal Kendurkar"),
                                    P(cls="text-center text-[12px] text-[#006478]")("Yoga Coach")
                                ) for _ in range(2)],
                            ),
                        ),
                    ),

                    Div(cls="mt-16 w-full hidden md:flex flex-col items-center justify-center gap-10 relative")(
                        Img(cls="md:w-auto md:h-auto hidden md:block", src='static/img/join-us-desktop.png',
                            alt="mfi-desktop"),
                        H1(cls="absolute text-center text-[64px] font-heading mt-60 text-[#006478]")("“Join Us”"),
                        P(cls="absolute text-center font-rest leading-relaxed text-2xl text-[#006478] font-extralight mt-100")(
                            B("Online:"),
                            " Join live-streamed sessions from anywhere."
                        ),
                        P(cls="absolute text-center font-rest leading-relaxed text-2xl text-[#006478] font-extralight mt-120")(
                            B("In-Person:"),
                            " Attend a gathering at a partner yoga shala or meditation center."
                        ),
                        meditation_button("absolute hidden mt-160 md:block md:text-base md:w-52")
                    ),

                    footer()

                ),

            ),

        )

    )


@rt("/about-us")
def about():
    # Define the main content for the About Us page
    # REMOVED min-h-full as flex-grow will handle expansion
    about_content = Div(cls="min-w-full max-w-2xl mx-auto px-4 py-8 md:py-16 flex flex-col justify-center items-center text-center mb-16 flex-grow")( # ADDED flex-grow
        Img(cls="mb-10", src='static/img/TMIlogo.png'),
        # H1(cls="font-heading font-light text-[32px]  text-[#004552] mb-6")("The Mindful Initiative"),
        P(cls="font-rest text-[24px] font-light text-[#006478] leading-relaxed mb-4")(
            Span(cls="block")("Meditate for India is organized by The Mindful Initiative, an organization"),
                 Span(cls="block")("dedicated to integrating mindfulness, yoga, and contemplative"),
                Span(cls="block")("practices into daily life.")
        ),
        P(cls="font-rest font-light text-[24px] text-[#006478] leading-relaxed mb-8")(
            Span(cls="block")("Since 2017, we have created podcasts, workshops, and programs to"),
            Span(cls="block")("make these ancient practices accessible and impactful.")
        ),
        P(cls="font-rest text-lg md:text-xl text-[#006478] leading-relaxed")(B(
            "To learn more, visit: ",
            A("https://www.themindfulinitiative.com",
              href="https://www.themindfulinitiative.com",
              target="_blank",
              rel="noopener noreferrer",
              cls="text-[#006478]")
        )),
    )

    # Apply flex container classes directly to Body
    return Body(cls="flex flex-col min-h-screen")( # CHANGED classes here
        toggle_script,      # Child 1
        header_container,   # Child 2
        mobile_menu(),      # Child 3
        about_content,      # Child 4 (This now has flex-grow)
        footer()            # Child 5
    )

@rt("/join-event")
def join():
    join_content = Div(
        cls="min-w-full max-w-2xl mx-auto px-4 py-8 md:py-16 flex flex-col items-center text-center justify-center mb-16 flex-grow")(
        # ADDED flex-grow
        Img(cls="mb-10", src='static/img/together.png'),
        H1(cls="font-heading text-[32px] text-[#006478] mb-6 font-light")("Let’s Meditate for India."),
        H1(cls="font-heading text-[32px] font-light text-[#006478] mb-6")("Let’s Meditate for Ourselves."),
        P(cls="font-rest font-light text-[24px] text-lg md:text-[24px] text-[#006478] leading-relaxed mb-4")(
            Span(cls="block")("The transformation of a nation begins from within. When we heal"),
            Span(cls="block")(" ourselves, we heal our surroundings. When we meditate together, we"),
            Span(cls="block")("create an unstoppable wave of clarity, peace, and well-being.")
        ),

        P(cls="mt-4 font-rest font-light text-[24px] text-lg md:text-[24px] text-[#006478] leading-relaxed mb-4")(
            Span(cls="block")(
                B(cls="font-bold")("Online:"),
                " Join live-streamed sessions from anywhere."
            ),
            Span(cls="block")(
                B(cls="font-bold")("In-Person:"),
                " Attend a gathering at a partner yoga shala or meditation center."
            ),
        ),
        Div(cls="flex items-center justify-center mb-16 gap-x-4")(
            Button(cls="bg-[#1DB0CD] hover:bg-[#19a0bb] text-[14px] text-white font-medium rounded-md transition duration-300 h-12 w-30 text-sm")("Join in person"),
            Button(cls="bg-white text-[#1DB0CD] font-light text-[14px] rounded-md transition duration-300 h-12 w-30 text-sm border-[#1DB0CD] border-1")("Join online")
        )

    )

    # Apply flex container classes directly to Body
    return Body(cls="flex flex-col min-h-screen")(  # CHANGED classes here
        toggle_script,  # Child 1
        header_container,  # Child 2
        mobile_menu(),  # Child 3
        join_content,  # Child 4 (This now has flex-grow)
        footer()  # Child 5
    )

serve()