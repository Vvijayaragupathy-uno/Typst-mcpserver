#import "templates/poster.typ": poster

#show: poster.with(
  title: [AI: ARCHITECTING THE FUTURE],
  authors: "Advanced Intelligent Systems Lab",
  institution: "Global Software Engineering Vision 2030",
  font: "Avenir Next",
  font_size: 24pt,
)

#v(2cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 4cm,
  [
    #set text(size: 32pt)
    == 1. The Generative Revolution
    Software is now co-authored by human creativity and machine precision.
    - *Zero-Boilerplate Dev:* Focus on intent, not implementation.
    - *Legacy Rebirth:* Breathing new life into decades-old systems.

    #v(1cm)
    == 2. Autonomous Systems
    The rise of self-governing, self-healing infrastructure.
    - *Predictive Reliability:* Solving issues before they occur.
    - *Elastic IQ:* Intelligent resource allocation at the edge.

    #v(1cm)
    == 3. Inclusive Innovation
    Democratizing technology through AI-driven accessibility.
    - *Universal Design:* Real-time adaptation for all users.
    - *Global Reach:* Instant, context-aware localization.
  ],
  [
    #set text(size: 32pt)
    == 4. Intelligent QA & Security
    Eliminating the tradeoff between speed and security.
    - *Shift-Left Security:* Catching vulnerabilities at commit time.
    - *Simulated Users:* AI agents testing every user flow.

    #v(1cm)
    == 5. Human-AI Collaboration
    The developer experience redefined by semantic understanding.
    - *Insightful Debugging:* Deep reasoning for complex logical errors.
    - *Agentic Workflows:* AI as a true pair-programming partner.

    #v(1cm)
    == 6. Sustainable Tech
    Optimizing for both performance and the planet.
    - *Green Compute:* Drastic reduction in cloud energy waste.
    - *Carbon-Aware Apps:* Real-time compute optimization.
  ]
)

#v(4cm)

// GEOMETRIC AI ART USING TYPST
#align(center)[
  #box(
    width: 80%,
    height: 40cm,
    stroke: 2pt + blue.lighten(60%),
    radius: 30pt,
    inset: 40pt,
    fill: luma(250),
    [
      #place(center + horizon)[
        #stack(
          dir: ltr,
          spacing: 2cm,
          circle(radius: 5cm, fill: gradient.radial(blue.lighten(40%), blue.darken(30%))),
          circle(radius: 5cm, fill: gradient.radial(aqua.lighten(40%), aqua.darken(30%))),
          circle(radius: 5cm, fill: gradient.radial(purple.lighten(40%), purple.darken(30%))),
        )
      ]
      #place(center + horizon)[
        #for i in range(12) {
          rotate(i * 30deg, line(start: (0pt, 0pt), end: (15cm, 0pt), stroke: (thickness: 1pt, paint: blue.lighten(60%), dash: "dashed")))
        }
      ]
      #place(center + horizon)[
        #circle(radius: 8cm, stroke: 5pt + blue.darken(20%), fill: none)
      ]
      #place(bottom + center)[
        #v(2cm)
        #text(size: 48pt, weight: "bold", fill: blue.darken(40%))[INTELLIGENCE REIMAGINED]
      ]
    ]
  )
]

#v(1fr)
#align(right)[
  #text(size: 20pt, fill: gray)[DESIGNED WITH TYPST MCP | 2026]
]
