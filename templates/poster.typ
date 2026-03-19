#let poster(
  title: "Poster Title",
  authors: "",
  institution: "",
  page_width: 84.1cm,
  page_height: 118.9cm,
  font: "New Computer Modern",
  font_size: 24pt,
  body
) = {
  set page(width: page_width, height: page_height, margin: 2cm)
  set text(font: font, size: font_size)
  set block(spacing: 1.5cm)

  // Header
  // SECTION: Header
  align(center)[
    #text(size: 56pt, weight: "bold")[#title]
    #if authors != "" {
      v(0.5cm)
      text(size: 32pt)[#authors]
    }
    #if institution != "" {
      v(0.3cm)
      text(size: 28pt)[#institution]
    }
  ]
  // END: Header

  v(1cm)
  body
}
