(TeX-add-style-hook
 "main-document"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "12pt")))
   (TeX-run-style-hooks
    "latex2e"
    "../Title-Page/title-page"
    "../Informative-Part/informative-part"
    "../Descriptive-Part/descriptive-part"
    "../Analytic-Part/analytic-part"
    "report"
    "rep12"
    "unicode"
    "setspace"
    "float"
    "graphicx"))
 :latex)

