import json
from report import Report

r = Report("myreport_templates")

r.jinja["section1"] = "<h1></h1>"

r.create_report()
