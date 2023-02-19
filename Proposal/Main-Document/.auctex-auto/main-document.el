(TeX-add-style-hook
 "main-document"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("report" "12pt")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("hyperref" "hidelinks")))
   (TeX-run-style-hooks
    "latex2e"
    "../Title-Page/title-page"
    "../Informative-Part/informative-part"
    "../Descriptive-Part/descriptive-part"
    "../Analytic-Part/analytic-part"
    "../References/references"
    "report"
    "rep12"
    "apacite"
    "unicode"
    "setspace"
    "float"
    "graphicx"
    "hyperref"
    "natbib"))
 :latex)

