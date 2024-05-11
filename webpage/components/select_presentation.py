import reflex as rx

from webpage.utils import slideshare_urls


elements = list(slideshare_urls.keys())

class FormSelectState1(rx.State):
    form_data: str = slideshare_urls[elements[0]]

    def handle_submit(self, form_data: str):
        """Handle the form submit."""
        self.form_data = form_data


def select_presentation() -> rx.Component:
    return rx.vstack(
        rx.text("Seleccione una presentación"),
        rx.form.root(
            rx.vstack(
                rx.select(
                    elements,
                    default_value=elements[0],
                    name="select",
                    #on_change=FormSelectState1.handle_submit,
                ),
                rx.button("Submit", type="submit"),
                # width="100%",
            ),
            on_submit=FormSelectState1.handle_submit,
            reset_on_submit=True,
            width="100%",
        ),

    )