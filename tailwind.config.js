module.exports = {
    content: ["./**/*.py"],
    theme: {
        extend: {
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