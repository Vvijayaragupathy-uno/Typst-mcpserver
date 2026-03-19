#let report(
  title: "Report Title",
  subtitle: none,
  author: "Author Name",
  date: datetime.today().display(),
  body
) = {
  set page(paper: "a4", margin: 2.5cm)
  set text(font: "New Computer Modern", size: 11pt)
  
  // Cover Page
  // SECTION: Cover
  page(align(center + horizon)[
    #text(size: 28pt, weight: "bold")[#title] \
    #if subtitle != none {
      v(0.5cm)
      text(size: 18pt)[#subtitle]
    }
    #v(2cm)
    #text(size: 14pt)[#author] \
    #v(0.5cm)
    #text(size: 12pt)[#date]
  ])
  // END: Cover

  // TOC
  // SECTION: TOC
  outline(indent: auto)
  pagebreak()
  // END: TOC

  set page(numbering: "1")
  counter(page).update(1)
  
  body
}
