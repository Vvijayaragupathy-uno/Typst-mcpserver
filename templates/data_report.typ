#let data-report(
  title: "Data Analysis Report",
  data-path: none,
  body
) = {
  set page(paper: "a4", margin: 2cm)
  set text(font: "New Computer Modern", size: 11pt)
  
  // Header
  // SECTION: Header
  align(center)[
    #text(size: 24pt, weight: "bold")[#title]
    #v(1cm)
  ]
  // END: Header

  if data-path != none {
    // SECTION: DataOverview
    let data = csv(data-path)
    let headers = data.at(0)
    let rows = data.slice(1)
    
    [== Data Overview (#data-path)]
    v(0.5cm)
    table(
      columns: headers.len(),
      fill: (col, row) => if row == 0 { luma(230) } else { white },
      ..headers.map(h => [*#h*]),
      ..rows.flatten()
    )
    // END: DataOverview
  }

  v(1cm)
  body
}
