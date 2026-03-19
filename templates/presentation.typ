#import "@preview/polylux:0.3.1": *

#let presentation(
  title: "Presentation Title",
  author: "Author Name",
  body
) = {
  set page(paper: "presentation-16-9", margin: 2cm)
  set text(font: "New Computer Modern", size: 24pt)

  // Title Slide
  // SECTION: TitleSlide
  polylux-slide[
    #align(center + horizon)[
      #text(size: 36pt, weight: "bold")[#title] \
      #v(1cm)
      #text(size: 24pt)[#author]
    ]
  ]
  // END: TitleSlide

  body
}

#let slide(title, body) = {
  // SECTION: #title
  polylux-slide[
    #text(size: 28pt, weight: "bold")[#title]
    #v(0.5cm)
    #body
  ]
  // END: #title
}
