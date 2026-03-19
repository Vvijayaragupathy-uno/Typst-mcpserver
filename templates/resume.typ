#let resume(
  name: "John Doe",
  email: "john@example.com",
  phone: "123-456-7890",
  body
) = {
  set page(paper: "us-letter", margin: 1.25cm)
  set text(size: 10pt, font: "New Computer Modern")
  set par(justify: true)

  // SECTION: Header
  align(center)[
    #text(size: 16pt, weight: "bold")[#upper(name)] \
    #email | #phone
  ]
  // END: Header

  v(0.2cm)
  body
}

#let resume-section(title, body) = {
  // SECTION: #title
  v(0.2cm)
  text(weight: "bold")[#upper(title)]
  line(length: 100%, stroke: 0.5pt)
  body
  // END: #title
}
