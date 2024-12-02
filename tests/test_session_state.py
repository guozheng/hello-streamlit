from streamlit.testing.v1 import AppTest

def test_increment_button():
    app = AppTest.from_file("pages/session_state.py").run()

    # Clicking the button should increment both counters to 1
    assert app.button[0].label == "Increment"
    app.button[0].click().run()
    # use the universal .value accessor to get the value of the widget
    assert app.info[0].value == "Counter in session state: 1, Counter outside session state: 1"

    # Clicking the button again should increment the counter 1, but not counter2
    app.button[0].click().run()
    assert app.info[0].value == "Counter in session state: 2, Counter outside session state: 1"