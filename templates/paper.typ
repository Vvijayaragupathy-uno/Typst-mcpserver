#let paper(
  title: "Paper Title",
  authors: (),
  abstract: none,
  columns: 1,
  body
) = {
  set page(paper: "a4", margin: 2.5cm)
  set text(font: "New Computer Modern", size: 11pt)
  set par(justify: true)

  // Title and Authors
  // SECTION: Header
  align(center)[
    #text(size: 18pt, weight: "bold")[#title]
    #v(0.5cm)
    #grid(
      columns: (1fr,) * calc.min(3, authors.len()),
      column-gap: 1cm,
      ..authors.map(author => align(center)[
        #text(size: 12pt, weight: "bold")[#author.name] \
        #text(size: 10pt)[#author.affiliation] \
        #text(size: 10pt, style: "italic")[#author.email]
      ])
    )
  ]
  // END: Header

  // Abstract
  if abstract != none {
    v(0.5cm)
    // SECTION: Abstract
    block(inset: (x: 1cm))[
      #text(weight: "bold")[Abstract] \
      #abstract
    ]
    // END: Abstract
  }

  v(0.5cm)

  if columns > 1 {
    show: col => show-columns(columns, col)
    body
  } else {
    body
  }
}

#let show-columns(n, body) = {
  set page(columns: n)
  body
}
