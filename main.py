import logging
from typing import Optional
from datetime import datetime
from fasthtml.common import *
from sqlmodel import SQLModel, Field, create_engine, Session # Added SQLModel imports
from sqlalchemy.exc import IntegrityError # To catch potential DB errors like duplicates

def checkmark_svg():
    """Returns an SVG checkmark icon using FastHTML Svg and Path components."""
    return Svg( # The outer <svg> tag
        Path( # The inner <path> tag
            d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z", # The path data
            stroke_linecap="round", # Path attributes
            stroke_linejoin="round",
            stroke_width="2"
        ),
        # Attributes for the <svg> tag itself
        cls="w-16 h-16 text-green-500 mx-auto mb-4",
        fill="none",
        stroke="currentColor",
        viewBox="0 0 24 24",
        # xmlns="http://www.w3.org/2000/svg" # Svg component adds xmlns automatically
    )

toggle_script = Script("""
    // Function to toggle the menu visibility
    function toggleMenu() {
        const menu = document.getElementById('mobile-menu');
        if (menu) {
           menu.classList.toggle('hidden');
        }
    }

    // Add event listener to the whole document for clicks
    document.addEventListener('click', function(event) {
        const menu = document.getElementById('mobile-menu');
        const hamburgerButton = document.getElementById('hamburger-btn');

        // If menu or button doesn't exist, do nothing
        if (!menu || !hamburgerButton) {
            return;
        }

        // Check if the menu is currently visible (doesn't have 'hidden' class)
        const isMenuVisible = !menu.classList.contains('hidden');

        // Check if the click target is the hamburger button or inside it
        const isClickOnButton = hamburgerButton.contains(event.target);

        // Check if the click target is inside the menu
        const isClickInsideMenu = menu.contains(event.target);

        // If the menu is visible AND the click was NOT on the button AND NOT inside the menu
        if (isMenuVisible && !isClickOnButton && !isClickInsideMenu) {
            // Hide the menu
            menu.classList.add('hidden');
        }
    });
""")


close_modal_script = Script("""
document.addEventListener('DOMContentLoaded', (event) => {
  // Ensure body exists before adding listener
  if (document.body) {
      document.body.addEventListener('closeModal', function(evt) {
          console.log('closeModal event received, closing modal.'); // Optional: for debugging
          const modal = document.getElementById('join-modal-container');
          if (modal) {
              // Add a fade-out effect before removing (optional)
              modal.style.transition = 'opacity 0.5s ease-out';
              modal.style.opacity = '0';
              setTimeout(() => { modal.remove(); }, 500); // Remove after fade
          } else {
              console.log('Modal container #join-modal-container not found'); // Optional: for debugging
          }
      });
  } else {
      console.error('Document body not found when trying to attach closeModal listener.');
  }
});
""")

hdrs = (
    Meta(name="viewport", content="width=device-width, initial-scale=1.0"),
    Meta(
        name="description",
        content="Fun and enriching yoga summer camp for kids in Bangalore. Combining mindfulness, movement, and play to nurture children's physical and emotional wellbeing. Ages 5-12."
    ),
    Link(rel="stylesheet", href="/static/output.css", type="text/css"),
    close_modal_script,
    toggle_script
)

app, rt = fast_app(hdrs=hdrs, pico=False, live=False)

# --- Database Model & Setup ---

# Define the model for online participants
class OnlineParticipant(SQLModel, table=True):
    __tablename__ = "online_participants" # Give it a distinct name

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    address: Optional[str] = Field(default=None) # Optional address field
    email: str = Field(unique=True, index=True)  # Ensure email is unique
    phone: str
    created_at: datetime = Field(default_factory=datetime.now)
    # Add __table_args__ if you need to support modifications on existing tables
    __table_args__ = ({'extend_existing': True},)


# --- Database Setup Functions (provided by you) ---
def init_db(engine): # Pass engine to init_db
    SQLModel.metadata.create_all(engine, checkfirst=True)

def get_engine(database_url: str):
    # Production settings
    db_engine = create_engine(
        database_url,
        echo=False, # Set to True for debugging SQL queries
        pool_pre_ping=True,
        pool_size=5,
        max_overflow=10
    )
    logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)
    return db_engine

# --- Database Initialization ---
# Make sure this environment variable is set where you run the app
DATABASE_URL = os.getenv("POSTGRES_MFI", "sqlite:///./default_mfi.db") # Provide a default SQLite DB for easy testing

if not DATABASE_URL:
    print("Warning: POSTGRES_MFI environment variable not set. Using default SQLite DB.")
    # Optionally raise an error if PostgreSQL is strictly required:
    # raise ValueError("POSTGRES_SCAMP_URL environment variable is required")

engine = get_engine(DATABASE_URL)

# --- End Database Model & Setup ---



# --- Helper Functions & Components ---

def primary_button(text, **kwargs):
    """Creates a button with the primary color #1DB0CD and hover state."""
    base_classes = "bg-[#1DB0CD] hover:bg-[#19a0bb] text-white font-semibold py-2 px-4 rounded-md transition duration-300"
    # Combine base classes with any additional classes passed
    all_classes = f"{base_classes} {kwargs.pop('cls', '')}"
    return Button(text, cls=all_classes.strip(), **kwargs)

def join_online_modal():
    """Creates the modal popup using DaisyUI classes like the Attendance Form."""
    modal_container = Div(
        # Backdrop (Standard Tailwind)
        Div(cls="fixed inset-0 backdrop-blur-sm bg-white/30 z-[90]",
            hx_get="/close-modal", hx_target="#join-modal-container", hx_swap="delete"),
        # Centering wrapper (Standard Tailwind)
        Div(cls="fixed inset-0 z-[100] flex items-center justify-center p-4")(
            # Modal Box (Using DaisyUI Card Style)
            Div(cls="card flex-shrink-0 w-full md:max-w-[647px] shadow-lg backdrop-blur-lg bg-white/70 rounded-lg border border-white/30 relative")( # Card classes from example
                # Close button (Standard Tailwind, positioned relative to card)
                Button("×",
                       cls="absolute top-2 right-3 text-[#1DB0CD] hover:text-[#19a0bb] opacity-70 hover:opacity-100 text-2xl font-bold", # Use base-content for text
                       hx_get="/close-modal", hx_target="#join-modal-container", hx_swap="delete"),
                # Modal Content Area / Card Body
                Div(id="modal-content", cls="card-body")( # Added card-body class
                     # --- Registration Form (Using DaisyUI Form Control/Input/Button Styles) ---
                    Form(
                        # Name Input
                        Div(cls="form-control")( # form-control class
                            Label(cls="label")( # label class
                                Span("Name", cls="label-text") # label-text class
                            ),
                            Input(type="text", id="name", name="name", required=True, placeholder="Enter Name...",
                                  cls="input input-bordered w-full") # input input-bordered classes
                        ),
                        # Address Input (Optional)
                        Div(cls="form-control mt-4")( # form-control and margin
                            Label(cls="label")(
                                Span("Address (Optional)", cls="label-text")
                            ),
                            Input(type="text", id="address", name="address", placeholder="Enter Address...",
                                  cls="input input-bordered w-full") # input input-bordered classes
                        ),
                        # Email Input
                        Div(cls="form-control mt-4")( # form-control and margin
                            Label(cls="label")(
                                Span("Email", cls="label-text")
                            ),
                            Input(type="email", id="email", name="email", required=True, placeholder="Enter Email...",
                                 cls="input input-bordered w-full") # input input-bordered classes
                        ),
                        # Phone Input
                        Div(cls="form-control mt-4")( # form-control and margin
                            Label(cls="label")(
                                Span("Phone no", cls="label-text")
                            ),
                            Input(type="tel", id="phone", name="phone", required=True, placeholder="Enter Phone Number...",
                                  cls="input input-bordered w-full") # input input-bordered classes
                        ),
                        # Submit Button
                        Div(cls="form-control mt-6")( # form-control and margin
                            primary_button("Continue", type="submit",
                                   # Use btn and btn-primary from DaisyUI, make it full width
                                   cls="w-full")
                        ),
                        # HTMX attributes
                        hx_post="/participants/online",
                        hx_target="#modal-content",
                        hx_swap="innerHTML"
                    )
                    # --- End Registration Form ---
                ) # End #modal-content / card-body
            ) # End Modal Box / card
        ), # End Centering wrapper
        id="join-modal-container"
    )
    return modal_container

def registration_success_message(name, email):
    """Generates the final success message Div styled like the screenshot."""
    # Main container for the success message content
    return Div(id="modal-content", cls="text-center")( # Use padding from card-body
        # Checkmark Icon
        checkmark_svg(), # Assumes checkmark_svg() produces the desired icon/styling

        # Heading
        H3("Registration successful!!",
           cls="font-heading text-2xl md:text-3xl text-[#004552] mb-4"), # Center alignment is inherited

        # Paragraph 1
        P(cls="font-rest text-base md:text-lg text-[#004552] mb-3")(
            "Thank you! You have successfully registered for ", B("Meditate for India."), " We are eager to host you!"
        ),

        # Paragraph 2 with email
        P(cls="font-rest text-base md:text-lg text-[#004552] mb-6")(
             "We have sent you an email on ", B(email), " that has the event meeting link and other required details."
        ),
        # Note: No button, auto-close is handled by HX-Trigger from the route
    )


def registration_error_message(message_text):
    """Generates an error message Div."""
    return Div(id="modal-content", cls="text-center p-4 text-red-600")( # Target the same ID
        H3("Registration Failed", cls="font-heading text-xl mb-4"),
        P(message_text, cls="font-rest mb-6"),
        Button("Close",
                cls="bg-gray-300 hover:bg-gray-400 text-gray-800 font-medium py-2 px-4 rounded-md transition duration-300",
                hx_get="/close-modal",
                hx_target="#join-modal-container",
                hx_swap="delete")
    )


def meditation_button(additional_classes=""):
    """Helper function to avoid button style duplication"""
    base_classes = "bg-[#1DB0CD] hover:bg-[#19a0bb] text-white font-medium py-3 px-3 rounded-md transition duration-300 h-12 w-44 text-sm"
    return Button(cls=f"{base_classes} {additional_classes}",
                  hx_get = "/modal/join-online",  # Fetch modal content from this endpoint
                  hx_target = "#modal-container",  # Append modal to the body
                  hx_swap = "beforeend"  # Add it at the end
                  )("Join Meditate for India")

# --- Responsive Navbar Components ---

def hamburger_button():
    """Creates the hamburger button visible only on mobile."""
    # SVG for hamburger icon
    hamburger_icon = Img(src="/static/img/hamburger.svg", alt="Menu", cls="w-6 h-6")
    # Button shown only below md breakpoint, triggers JS toggle function
    return Button(hamburger_icon,
                  id="hamburger-btn",
                  cls="md:hidden ml-auto p-2 text-gray-800 hover:bg-gray-100 rounded focus:outline-none focus:ring-2 focus:ring-inset focus:ring-blue-500", # Added focus styles
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

# You can place this function definition alongside your other component functions

def faq_accordion_item(question: str, answer: Any, faq_id: str):
    """Creates a single DaisyUI collapse item for the FAQ accordion."""
    return Div(cls="collapse collapse-arrow bg-base-100 shadow-md mb-3 rounded-lg border border-base-300")( # Added border/shadow
        # Use radio input for accordion behavior (only one open at a time)
        Input(type="checkbox", name="faq_id", id=faq_id), # Need unique ID for label
        # The visible question part (acts as label for radio)
        Label(cls="collapse-title text-lg md:text-xl font-medium font-rest text-[#004552] cursor-pointer", _for=faq_id)( # Use Label for accessibility
            question
        ),
        # The hidden answer part
        Div(cls="collapse-content font-rest text-gray-700 px-4 md:px-6 pb-4")( # Add padding
            P(answer) # Wrap answer in P for consistent spacing
        )
    )

def faq_content():
    """Generates the main content for the FAQ page."""
    faqs = [
        ("What is Meditate for India?",
         "It's a free, global 24-hour immersion event featuring Meditation, Pranayama, Asana, and Chanting. It aims to bring India's ancient wisdom into modern life and foster collective well-being."),
        ("When is the event?",
         "The main event is scheduled for June 21st, 2025. Specific timings for sessions will be announced closer to the date."),
        ("How can I participate?",
         Span("You can join ", B("online")," from anywhere through live-streamed sessions. Please visit the 'Join Event' page to register .")),
        ("Who is organizing this?",
         Span("Meditate for India is organized by ", A("The Mindful Initiative", href="/about-us", cls="link link-hover text-[#1DB0CD]"), ", an organization dedicated to integrating mindfulness, yoga, and contemplative practices into daily life since 2017.")),
        ("Is this the first Meditate for India event?",
         "No, the first Meditate for India was held during the COVID-19 pandemic, offering thousands a space for healing, resilience, and connection. This event continues the movement as a proactive step toward cultivating lasting well-being, rather than just in response to a crisis."),
        ("What is the purpose or goal?",
         "It's a collective movement focused on three core pillars: Reimagining a Mindful India, Celebrating Our Heritage, and Cultivating Inner Wisdom through shared practice.")
    ]

    return Div(cls="max-w-3xl mx-auto")( # Container for the accordion items
        *[faq_accordion_item(q, a, f"faq-{i}") for i, (q, a) in enumerate(faqs)]
    )



def mobile_menu():
    """Creates the mobile navigation menu, hidden by default."""
    # Define links for the mobile menu
    links = [
        A("Home", href="/", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("Join the event", href="/join-event", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("About Us", href="/about-us", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("FAQ", href="/faq", cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded"),
        A("Login / Sign up",  # Changed text slightly for clarity
          # href="#", # Remove default href or set to javascript:void(0) if needed
          cls="block py-2 px-4 text-gray-800 hover:bg-gray-200 rounded",  # Keep existing classes
          # Add HTMX attributes to trigger modal
          hx_get="/modal/join-online",
          hx_target="#modal-container",
          hx_swap="beforeend"
          ),
    ]

    # Mobile menu container, hidden by default, absolutely positioned
    return Div(*links,
               id="mobile-menu",
               # Initially hidden, shown only below md when toggled
               cls="hidden md:hidden fixed top-16 left-0 right-0 bg-[#F4F8F9] shadow-md flex-col p-4 space-y-1 z-50") # Adjusted top, space-y

def desktop_navbar():
    """The original navbar, now specifically for desktop (md and up)."""
    return Nav(cls="hidden md:flex space-x-8")( # Renamed variable, adjusted spacing
        A("Home", href="/", cls="text-gray-800 hover:text-[#004552] font-medium"),
        A("Join the event", href="/join-event", cls="text-gray-800 hover:text-[#004552] font-medium"),
        A("About Us", href="/about-us", cls="text-gray-800 hover:text-[#004552] font-medium"),
        A("FAQ", href="/faq", cls="text-gray-800 hover:text-[#004552] font-medium"),

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


# header_container = Div(cls="bg-[#F4F8F9] shadow-sm")(
#         # Added relative positioning for absolute mobile menu
#         Div(cls="container m-0 flex justify-between items-center p-4")(  # Inner container for alignment
#             # Logo/Brand Name (visible on all screens)
#             # Div(A("Meditate For India", href="/", cls="text-xl font-bold text-[#004552]")),
#
#             A(href="/")(
#                         Img(src="/static/img/TMIlogo.png", # Path to your logo
#                             alt="The Mindful Initiative Logo",
#                             cls="h-8 w-auto") # Adjust height (h-8, h-10, etc.) as needed, width adjusts automatically
#                     ),
#
#             # Desktop Navigation Links (hidden on mobile)
#             # desktop_navbar(),
#
#             # Login Link for Desktop (hidden on mobile)
#             A("Login / Sign up",  # Changed text slightly for clarity
#               # href="#", # Remove default href or set to javascript:void(0) if needed
#               cls="py-2 hidden md:block px-4 text-gray-800 rounded justify-end",  # Keep existing classes
#               # Add HTMX attributes to trigger modal
#               hx_get="/modal/join-online",
#               hx_target="#modal-container",
#               hx_swap="beforeend"
#               ),
#
#             # Hamburger Button (visible on mobile)
#             hamburger_button()
#         ),
#     )

header_container = Div(cls="bg-[#F4F8F9] shadow-sm")(
    # Main container with padding and flex alignment
    Div(cls="container flex items-center p-4 m-0 min-w-full")( # Removed justify-between

        # --- Group Logo and Main Nav Links ---
        Div(cls="flex items-center gap-x-8")( # Group logo and nav, add gap
            # Logo Link
            A(href="/")(
                Img(src="/static/img/TMIlogo.png",
                    alt="The Mindful Initiative Logo",
                    cls="h-8 w-auto")
            ),
            # Desktop Navigation Links (Main Links Only)
            desktop_navbar() # Function now returns only the main Nav
        ),
        # --- End Group ---

        # --- Login/Sign up Link (Pushed Right) ---
        # This is now separate and outside the grouping Div
        A("Login / Sign up",
          cls="ml-auto hidden md:block text-gray-800 hover:text-blue-600 font-medium", # ml-auto pushes it right, hidden md:block for desktop only
          hx_get="/modal/join-online", # Keep the modal trigger
          hx_target="#modal-container",
          hx_swap="beforeend"
        ),
        # --- End Login/Sign up Link ---

        # Hamburger Button (Still needed for mobile)
        # This should appear correctly on mobile as it's the last item flex pushes right by default if space allows,
        # but the login link is hidden on mobile. If alignment issues occur on mobile, adjustments might be needed.
        hamburger_button()
    ),
)

@rt("/")
def get_homepage():
    # Header container holds logo, desktop nav, and hamburger button


    return (

        Body(cls="m-0")(
            toggle_script,
            Main(
                header_container,
                mobile_menu(),
                Div(id="modal-container"),
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
                                B("online ", cls="font-bold font-rest md:text-[24px] leading-relaxed"),
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
        ),
        Div(cls="flex items-center justify-center mb-16 gap-x-4")(
            Button(cls="bg-[#1DB0CD] hover:bg-[#19a0bb] font-light text-[14px] rounded-md transition duration-300 h-12 w-30 text-sm border-[#1DB0CD] border-1",
                    hx_get = "/modal/join-online",  # Fetch modal content from this endpoint
                    hx_target = "#modal-container",  # Append modal to the body
                    hx_swap = "beforeend"  # Add it at the end
                   )("Join online")
        )

    )

    # Apply flex container classes directly to Body
    return Body(cls="flex flex-col min-h-screen")(  # CHANGED classes here
        toggle_script,  # Child 1
        header_container,  # Child 2
        mobile_menu(),  # Child 3
        Div(id="modal-container"),
        join_content,  # Child 4 (This now has flex-grow)
        footer()  # Child 5
    )

# --- New Routes for Modal and Form Handling ---

@rt("/modal/join-online")
def get_join_modal():
    """Route to serve the join online modal HTML."""
    return join_online_modal()

@rt("/participants/online")
def add_online_participant(participant: OnlineParticipant):
    """Handles submission, saves data, and returns the confirmation step."""
    try:
        with Session(engine) as session:
            session.add(participant)
            session.commit()
            session.refresh(participant)

            # --- RETURN CONFIRMATION STEP ---
            # This replaces the form inside the modal
            confirmation_step = Div(id="modal-content", cls="text-center p-6")( # Target same ID
                H3("Confirm", cls="font-heading text-2xl text-[#004552] mb-4"),
                P("You will be receiving a meeting link on the email id that you provided.",
                  cls="font-rest text-gray-700 mb-6"),
                primary_button( # Use the helper for styling
                    "Confirm",
                    hx_get=f"/registration-confirmed?name={participant.name}&email={participant.email}", # Pass name for final message
                    hx_target="#modal-content",  # Target same content area
                    hx_swap="innerHTML"         # Replace confirmation with success message
                ),
                Button(  # Use standard secondary/gray button style
                    "Cancel",
                    cls="bg-gray-200 hover:bg-gray-300 text-gray-700 font-medium py-2 px-4 rounded-md transition duration-300",
                    hx_get="/close-modal",
                    hx_target="#join-modal-container",
                    hx_swap="delete"  # Close modal directly
                )
            )
            return confirmation_step
            # --- END CONFIRMATION STEP ---

    except IntegrityError:
        return registration_error_message("An account with this email address already exists.")
    except Exception as e:
        logging.error(f"Error saving participant: {e}")
        return registration_error_message("Something went wrong. Please try again later.")

@rt("/registration-confirmed")
def show_confirmation(name: str = "Participant", email: str = "your email"): # Add email parameter
    """Returns the final registration success message and triggers auto-close."""
    success_content = registration_success_message(name, email)

    # Define HX-Trigger header to fire 'closeModal' event after 20 seconds
    # Note: Use trigger_after_settle to ensure content is rendered first
    headers = HtmxResponseHeaders(trigger_after_settle='{"closeModal": "" }', trigger_delay='20s')

    # Return the content AND the header
    return success_content


@rt("/faq")
def faq_page():
    """Renders the FAQ page."""

    page_content = Div(cls="container mx-auto px-4 py-8 md:py-16 flex-grow")( # Use flex-grow to push footer down
        H1("Frequently Asked Questions", cls="font-heading text-3xl md:text-4xl text-[#004552] mb-8 text-center"),
        faq_content() # Include the accordion content generated above
    )

    # Structure the page using existing components + new content
    return Body(cls="flex flex-col min-h-screen")(
        toggle_script,
        header_container, # Your existing header
        mobile_menu(),    # Your existing mobile menu (now with FAQ link)
        Div(id="modal-container"), # Keep the modal container
        page_content,     # The FAQ content defined above
        footer()          # Your existing footer
    )

@rt("/close-modal")
def close_modal():
    """Route to handle closing the modal. Returns empty response because HTMX handles deletion."""
    return "" # Return empty string, HTMX swap="delete" handles removal

# --- End New Routes ---
init_db(engine)
serve()