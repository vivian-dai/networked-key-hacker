# Home
Key Hacker allows you to take over someone's keyboard with consent.

## Project layout

    LICENSES            # Licensed under the MIT licenses
    mkdocs.yml          # The configuration file.
    README.md           # You might want to read me
    requirements.txt    # Packages needed to run this
    docs/
        index.md        # The documentation homepage.
        ...             # Other markdown pages, images and other files.
        theme/
            main.html   # HTML file for the theme which just inherits from mkdocs theme
        key_hacker/     # The src folder except it isn't called src
            classes/    # Classes used
            interface/  # The client side "interfaces"
            modules/    # Random misc functions the server uses that got tossed here instead of in the server
            client.py   # The client file
            server.py   # The server file
        scripts/        # Contains some scripts that might save time and be useful but probably won't
    
