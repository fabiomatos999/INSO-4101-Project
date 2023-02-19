(TeX-add-style-hook
 "proposal"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "12pt")))
   (TeX-run-style-hooks
    "latex2e"
    "./Title-Page/title-page"
    "report"
    "rep12"
    "unicode"
    "setspace"
    "float"
    "graphicx"))
 :latex)

