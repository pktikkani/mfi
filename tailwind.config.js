module.exports = {
    content: ["./**/*.py"],
    theme: {
        extend: {
            backgroundImage: {

                'linear-to-r': 'linear-gradient(to right in oklab, var(--tw-gradient-stops))',
                'linear-to-r/srgb': 'linear-gradient(to right in srgb, var(--tw-gradient-stops))',
                'linear-to-r/hsl': 'linear-gradient(to right in hsl, var(--tw-gradient-stops))',
                'linear-to-r/oklab': 'linear-gradient(to right in oklab, var(--tw-gradient-stops))',
                'linear-to-r/oklch': 'linear-gradient(to right in oklch, var(--tw-gradient-stops))',
                'linear-to-r/longer': 'linear-gradient(to right in oklab longer, var(--tw-gradient-stops))',
                'linear-to-r/shorter': 'linear-gradient(to right in oklab shorter, var(--tw-gradient-stops))',
                'linear-to-r/increasing': 'linear-gradient(to right in oklab increasing, var(--tw-gradient-stops))',
                'linear-to-r/decreasing': 'linear-gradient(to right in oklab decreasing, var(--tw-gradient-stops))',
            },
            fontFamily: {
                'heading': ['"Playwrite IT Moderna"', 'serif'], // For headings
                'sans': ['"Open Sans"', 'system-ui', 'sans-serif'] // For body text
            },
        }
    },

    plugins: [require("daisyui")],
    daisyui: {
        themes: ["fantasy"]
    }
}