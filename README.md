# hello-streamlit
Small projects to learn Streamlit. Try it out: [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://data-rabbit.streamlit.app/)


## Requirements
Install the requirements:
```
pip install -r requirements.txt
```

## Run
```
streamlit run home.py
```

## Notes
- execution model:
    - code is executed from top to bottom
    - when the appplication is loaded in a browser/tab, a new session starts
    - when the user interacts with the widgets, e.g. clicks a button, enters some text, selects a value, etc. the code is executed again/rerun, Streamlit redraws the page
- widget execution order of operations:
    - the widget value in `st.session_state` is updated
    - the widget callback function is executed
    - the page reruns and the new widget value is used to update the UI
- text output supports markdown, latex, and html/css, you can also easily show code, json, images, etc.
- use `st.cache_data` to cache data from expensive computations, e.g. loading from a database, a large file or over the network, it makes a copy at each function call. 
    - Internally, it uses `pickle` module to serialize and deserialize the data. 
    - Supported parameters: `ttl` (time to live) in seconds and `max_entries` (maximum number of entries) to limit memory usage. There is also a special `show_spinner` parameter to show a spinner while the data is being loaded.
    - a cache key is generated using the function parameters, so if the function is called with different parameters, it will be cached separately. If you don't want a parameter to be part of the cache key, you can prefix it with underscore, e.g. `_my_param`. When you use custom classes as parameters, you need to implement a special `hash_func` and pass it to `st.cache_data` decorator.
- use `st.cache_resource` to cache objects across sessions, e.g. a machine learning model or a database connection. It does not make a copy of the object, it only stores a reference to the original object.
- create multi-page apps by adding more `.py` files to the `pages` folder. You can also manually use `st.Page` and `st.navigation` to create custom multi-page apps in more flexible ways.
- data visualization is a first-class concern in Streamlit, with built-in support for charts and graphs
- secrets are stored in `.streamlit/secrets.toml` and can be accessed with `st.secrets["key"]`, make sure you add it to `.gitignore` to avoid leaking secrets
- session state is a way to share data between runs, it can be accessed with `st.session_state.key`
- an easy way to deploy your app is to use Streamlit Community Cloud, see [this guide](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)
- define a custom class in a separate file and import it into your app, e.g. `from my_module import MyClass` to avoid redefining the class since the page code is rerun often
- easy to use integration with pytest, including integration with github actions, see [Streamlit's native app testing framework](https://docs.streamlit.io/develop/concepts/app-testing)

## References
- [Streamlit Documentation](https://docs.streamlit.io/en/stable/)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [30 Days of Streamlit (developed using Streamlit as well)](https://30days.streamlit.app/)