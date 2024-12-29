mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
heafless = true\n\
\n\
">~/.streamlit/config.toml