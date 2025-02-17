import os
import sys
import pandas as pd
from htpy import a, body, br, div, footer, h3, head, html, img, link, meta, p, script, section, span, strong, title, table, tr, td

def get_marks_and_grade( row, col ):
	if pd.isna( row[ col ] ): return 0, 'F'

	marks = row[ col ]
	if marks >= 90: letter = 'A'
	elif marks >= 80: letter = 'B'
	elif marks >= 70: letter = 'C'
	elif marks >= 60: letter = 'D'
	elif marks >= 50: letter = 'E'
	elif marks < 50: letter = 'F'

	return int(marks), letter

df_students = pd.read_csv( '../records/students.csv' )

divs = []
groups = ["a", "b"]

tfs = ["Felix", "James", "Nyalimo", "Modi", "Thiong"]
images = {}
images['Felix'] = 'omon.jpg'
images['Nyalimo'] = 'nyalimo.jpg'
images['James'] = 'james.jpg'
images['Thiong'] = 'thiong.jpg'
images['Modi'] = 'modi.jpg'


times = ["Tuesdays 2:00 - 4:00 pm","Thursdays 2:00 - 4:00 pm"]
departments = {'IT':'Information Technology', 'CS':'Computer Science'}
colors = {'IT':'text-alt-blue', 'CS':'text-alt-green'}
for g, t in zip(groups, times):

	div_fellows = []
	t_fellows = table(".border-none.background-inherit.small")[
					tr(".border-yellow.background-inherit")[
						td(".align-td-bottom")[
							span(f"#GROUP-{g.upper()}.text-heading1.align-bottom")[strong[f"Group {g.upper()}"]], 
							br, 
							f"{t}"], 
							td[ div_fellows ]
						]
					]

	d = div(".flex.py-1.pt-1.bg-item-lightgray")[br]
	divs.append( d )

	d = div(f"#GROUP-{g.upper()}.flex.bg-item-lightyellow")[  div(".card-body.text-center.bottom-white.px-3.py-1")[ t_fellows ] ]
	divs.append( d )

	d = div(".ml-3.mr-3.bg-white.session-item-line-lightyellow"),
	divs.append( d )

	trs = []
	trs.append(
		tr(".m-3.border-yellow.aborder-none.background-inherit.font-italic")[
			td(".name-column")["Student"],
			td(".attendance-column")["Assignment 1"],
			td(".attendance-column")["Assignment 2"],
			td(".attendance-column")["Assignment 3"],
			td(".attendance-column")["Assignment 4"],
			td(".attendance-column")["Assignment 5"],
			td(".attendance-column")["Quiz 1"],
			td(".attendance-column")["Quiz 2"],
			td(".attendance-column")["Quiz 3"],
			td(".attendance-column")["Quiz 4"],
			td(".attendance-column")["Quiz 5"],
		]
	)
	g_index = 0
	for index, row in df_students.iterrows():
		if row['GROUP'] != g.upper(): continue

		g_index += 1
		tds = []
		td_element = td(".name-column")[
			div[
				div(".mt-auto.mb-auto.number-outer.text-yellow.float-left")[
					div(".number.bullet-yellow.small")[f"{g_index}"]
				],
				div(".pl-3.mt-1.float-left")[
					span(".flex.small.float-left")[f"{row['NAME']} "],
					span(f".pl-3.flex.text-bold.small-alt.font-italic.float-left.{colors[ row['DEPARTMENT'].upper() ]}")[f" ({departments[ row['DEPARTMENT'].upper() ]} )"]
				]
			]
		]
		tds.append( td_element )

		marks, grade = get_marks_and_grade( row, 'A1' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'A2' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'A3' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )
		#td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{agrades[0].lower()}")[f"{ marks }"]]]

		marks, grade = get_marks_and_grade( row, 'A4' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'A5' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'Q1' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'Q2' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'Q3' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'Q4' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		marks, grade = get_marks_and_grade( row, 'Q5' )
		tds.append( td(".attendance-column")[div(".wrapper")[div(f".circle.extra-small.{grade.lower()}")[f"{ marks }"]]] )

		trs.append( tr(".m-3.border-yellow.background-inherit")[ tds ] )


	table_element = table(".ml-3.mr-3.mt-5.border-none.background-inherit.small")[ trs ]
	divs.append( div(".flex.apy-2.bg-item-lightyellow")[ table_element ] )
	divs.append( div(".flex.py-4.bg-item-lightyellow") )


page = html(lang="en-US", style="scroll-padding-top: 72px;")[
    head(".at-element-marker")[
        meta(charset="UTF-8"),
        meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
        meta(http_equiv="x-ua-compatible", content="ie=edge"),
        link(rel="SHORTCUT ICON", href="/favicon.ico", type="image/x-icon"),
        meta(name="robots", content="index, follow"),
        title["Labs | Deep Learning | University of Juba"],
        meta(name="description", content="Deep Learning"),
        link(rel="stylesheet", href="css/core.css", type="text/css"),
        link(rel="stylesheet", href="css/grid.css", type="text/css"),
        link(rel="stylesheet", href="css/style.css", type="text/css"),
        link(rel="stylesheet", href="css/students.css", type="text/css"),
		link(rel="stylesheet", href="css/lab.css", type="text/css")
    ],
    body[
        div[
            section[
                div(".d-flex.mx-lg-0")[
                    div(".w-100.ml-5.mr-5.mt-3")[
                        div(".depth-lg-none.bg-lg-transparent.bg-lg-transparent.depth-lg-none")[
                            div(".deeplearning.w-100.lab-group-page")[
                                img(".banner.w-100", src="images/cv_banner.jpg")
                            ],
                            div(".ml-3.mr-3.mt-3.mb-3.link-group")[
                                a(".elementor-button.elementor-button-orange", href="index.html")[span["Home"]],
                                a(".elementor-button.elementor-button-orange", href="schedule.html")[span["Schedule"]],
								a(".elementor-button.elementor-button-orange.elementor-button-orange-selected", href="standing.html")[span["Your Group & Grades"]],
                                a(".elementor-button.elementor-button-orange", href="resources.html")[span["Resources"]]
                            ]
                        ]
                    ]
                ]
            ],
            section[
                div(".d-flex.mx-lg-0")[
                    div(".w-100.ml-5.mr-5.mt-3")[
                        div(".depth-lg-none.bg-lg-transparent.bg-lg-transparent.depth-lg-none")[
                            div(".w-100")[
                                div(".w-100.lab-group-page")[
                                    div(".pl-3.pt-4.pb-1.w-full.rounded-t.text-black.dark:text-dark-contrastText.bg-light-gray"),
                                    div(".acard-body.p-3.bg-light-gray")[
                                        h3(".mt-1a.cool-title")["""Grading Policy"""],
                                        div(".small.font-italic")["""The course grading breakdown is as follows: 30% for assignments and 70% for the final exam. There are 6 assignment in this course, each accounting for 5% of your 30% marks.  This page presents the student performance on assignments and final exam, categorized by letter grades as outlined below in color codes. Letter grade for each assignment color-coded according to the marks obtained.  If you did not complete an assignment, you will automatically receive 0 marks for it"""]
                                    ],
                                    div(".pl-3.pr-3.pb-5.pt-1.bg-light-gray")[
                                        div[
                                            div(".float-left.mr-3")["Legend:"],
                                            div(".grade.a"),
                                            div(".grade-description")[strong["A"], " (90%-100%)"],
                                            div(".grade.b"),
                                            div(".grade-description")[strong["B"], " (80%-89%)"],
                                            div(".grade.c"),
                                            div(".grade-description")[strong["C"], " (70%-79%)"],
                                            div(".grade.d"),
                                            div(".grade-description")[strong["D"], " (60%-69%)"],
                                            div(".grade.e"),
                                            div(".grade-description")[strong["E"], " (50%-59%)"],
                                            div(".grade.f"),
                                            div(".grade-description")[strong["F"], " (", "<", "50%)"]
                                        ]
                                    ],									
                                    div(".card-body.aflex.py-0.px-1.pl-3.pr-3.bg-light-gray")[
                                        div(".pl-0.w-100")[
                                            div[
                                                div(".card-body.aflex.flex-column.py-0.px-0.pl-0")[
                                                    div[
                                                        div[
                                                            divs
                                                        ]
                                                    ]
                                                ]
                                            ]
                                        ]
                                    ],
                                    div(".h-2.py-3.w-full.bg-light-gray"),
                                    div(".bg-white.session-item-line-gray"),
                                    div(".h-2.pt-4.pb-3.w-full.rounded-b.text-black.dark:text-dark-contrastText.bg-light-gray")
                                ]
                            ]
                        ]
                    ]
                ]
            ],
            section[
                div(".azure-footer.aem-GridColumn.aem-GridColumn--default--12")[
                    footer(".azure-footer-nav")[
                        span["© University of Juba 2025"]
                    ]
                ]
            ]
        ],
        script(type="text/javascript", src="index.js")
    ]
]

print(page)
