#let cv(
  name: "John Doe",
  contact: (),
  body
) = {
  set page(paper: "a4", margin: (x: 1.5cm, y: 1.5cm))
  set text(font: "Arial", size: 10pt)
  
  // Header
  // SECTION: Header
  grid(
    columns: (1fr, auto),
    align(left + horizon)[
      #text(size: 24pt, weight: "bold")[#name]
    ],
    align(right + horizon)[
      #contact.join(" | ")
    ]
  )
  line(length: 100%, stroke: 0.5pt)
  // END: Header

  v(0.5cm)
  body
}

#let section(title, body) = {
  v(0.3cm)
  // SECTION: #title
  text(size: 12pt, weight: "bold", fill: blue.darken(20%))[#upper(title)]
  v(-0.2cm)
  line(length: 100%, stroke: 0.5pt)
  body
  // END: #title
}
