# ***Project*** &nbsp; → &nbsp; **0x01. AirBnB clone - Web static**
***Scope*** &nbsp; → &nbsp; ` HTML ` &nbsp; ` css ` &nbsp; ` Front-end ` <br />

* ## ***Tasks***
  * **[0-index.html](./0-index.html)** &nbsp; → &nbsp; an HTML page that displays a header and a footer.
    - Layout:
      - Body:
        - no margin
        - no padding
      - Header:
        - color #FF0000 (red)
        - height: 70px
        - width: 100%
      - Footer:
        - color #00FF00 (green)
        - height: 60px
        - width: 100%
        - text Best School center vertically and horizontally always at the bottom at the page
    - Requirements:
      - You must use the header and footer tags
      - You are not allowed to import any files
      - You are not allowed to use the style tag in the head tag
      - Use inline styling for all your tags

  * **[1-index.html](./1-index.html)** &nbsp; → &nbsp; an HTML page that displays a header and a footer by using the style tag in the head tag (same as [0-index.html](./0-index.html))
    - Requirements:
      - You must use the header and footer tags
      - You are not allowed to import any files
      - No inline styling
      - You must use the style tag in the head tag

  * **[2-index.html](./2-index.html)** &nbsp; → &nbsp; an HTML page that displays a header and a footer by using CSS files (same as [1-index.html](./1-index.html))
    - Requirements:
      - You must use the header and footer tags
      - No inline styling
      - You must have 3 CSS files:
        - [` styles/2-common.css `](./styles/2-common.css): for global style (i.e. the ` body ` style)
        - [` styles/2-header.css `](./styles/2-header.css): for header style
        - [` styles/2-footer.css `](./styles/2-footer.css): for footer style
    - > The layout must be exactly the same as [1-index.html](./1-index.html)

  * **[3-index.html](./3-index.html)** &nbsp; → &nbsp;  an HTML page that displays a header and footer by using CSS files (same as [2-index.html](./2-index.html))
   - Layout:
      - Common:
        - no margin
        - no padding
        - font color: #484848
        - font size: 14px
        - font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
        - icon in the browser tab
      - Header:
        - color: white
        - height: 70px
        - width: 100%
        - border bottom 1px #CCCCCC
        - logo align on left and center vertically (20px space at the left)
      - Footer:
        - color white
        - height: 60px
        - width: 100%
        - border top 1px #CCCCCC
        - text Best School center vertically and horizontally
        - always at the bottom at the page
    - Requirements:
      - No inline style
      - You are not allowed to use the img tag
      - You are not allowed to use the style tag in the head tag
      - All images must be stored in the images folder
      - You must have 3 CSS files:
        - [` styles/3-common.css `](./styles/3-common.css): for the global style (i.e ` body ` style)
        - [` styles/3-header.css `](./styles/3-header.css): for the header style
        - [` styles/3-footer.css `](./styles/3-footer.css): for the footer style

  * **[4-index.html](./4-index.html)** &nbsp; → &nbsp;  an HTML page that displays a header, footer and a filters box with a search button.

  - Layout: (based on [` 3-index.html `](./3-index.html))
      - Container:
        - between header and footer tags, add a div:
          - classname: `container`
          - max width 1000px
          - margin top and bottom 30px - it should be 30px under the bottom of the `header`
          - center horizontally
    - Filter section:
      - tag section
      - classname filters
      - inside the .container
      - color white
      - height: 70px
      - width: 100% of the container
      - border 1px #DDDDDD with radius 4px
    - Button search:
      - tag button
      - text Search
      - font size: 18px
      - inside the section filters
      - background color #FF5A5F
      - text color #FFFFFF
      - height: 48px
      - width: 20% of the section filters
      - no borders
      - border radius: 4px
      - center vertically and at 30px of the right border
      - change opacity to 90% when the mouse is on the button

  - Requirements:
    - You must use: header, footer, section, button tags
    - No inline style
    - You are not allowed to use the img tag
    - You are not allowed to use the style tag in the head tag
    - All images must be stored in the images folder
    - You must have 4 CSS files:
      - [` styles/4-common.css `](./styles/4-common.css): for the global style (i.e ` body ` style)
      - [` styles/4-header.css `](./styles/4-header.css): for the header style
      - [` styles/4-footer.css `](./styles/4-footer.css): for the footer style
      - [` styles/4-filters.css `](./styles/4-filters.css): for the filters style
