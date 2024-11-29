# hello-streamlit
Small projects to learn Streamlit. You can see a demo [here](https://data-rabbit.streamlit.app/).

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
- text output supports markdown, latex, and html/css, you can also easily show code, json, images, etc.
- use `st.cache_data` for data that doesn't change often, use `st.cache_resource` to share objects across sessions
- data visualization is a first-class concern in Streamlit, with built-in support for charts and graphs
- secrets are stored in `.streamlit/secrets.toml` and can be accessed with `st.secrets["key"]`, make sure you add it to `.gitignore` to avoid leaking secrets
- session state is a way to share data between runs, it can be accessed with `st.session_state.key`
- an easy way to deploy your app is to use Streamlit Community Cloud, see [this guide](https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app)

## References
- [Streamlit Documentation](https://docs.streamlit.io/en/stable/)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)