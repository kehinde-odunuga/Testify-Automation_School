import abc


class IWebElement(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def set_style(self, style):
        pass


class DivElement(IWebElement):

    def get_name(self):
        return  "div"

    def set_style(self, style):
        print("Div Style:", style)


class SpanElement(IWebElement):

    def get_name(self):
        return  "span"

    def set_style(self, style):
        print("Span Style:", style)

class ButtonElement(IWebElement):

    def get_name(self):
        return  "button"

    def set_style(self, style):
        print("Button Style:", style)


div_element = DivElement()
print(div_element.get_name())
div_element.set_style("Width: 100px; height: 100px")

span_element = SpanElement()
print(span_element.get_name())
div_element.set_style("Border: 1px solid red;")

button_element = ButtonElement()
print(button_element.get_name())
div_element.set_style("font-size: 20px; font-weight: bold")