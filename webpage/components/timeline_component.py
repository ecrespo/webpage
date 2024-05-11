import reflex as rx


class TimeLine(rx.Component):
    library = "react-chrono"
    tag = "Chrono"
    items = [
        {
            "title": "prueba",
            "date": "2021-09-01",
        }
    ]
    mode = "HORIZONTAL"


timeline = TimeLine.create


