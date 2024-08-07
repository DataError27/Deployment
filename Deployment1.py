import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf

# Title and header
st.set_page_config(layout="wide")
st.title('Singapore Bank Stock Analysis Tool')
st.header('Leverage data analytics and machine learning to anticipate future market movements and make strategic choices.\n\n')

# Using columns for side-by-side layout with custom widths
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.subheader('Technical Analysis')
    st.write('Technical analysis involves studying historical price data and trading volumes to forecast future price movements. This method relies on chart patterns, technical indicators (e.g., moving averages, RSI), and statistical measures to identify trends and market conditions. The core assumption is that past market activity can predict future behavior.')

with col2:
    st.subheader('Fundamental Analysis')
    st.write("Fundamental analysis evaluates a financial instrument's intrinsic value by examining economic indicators, financial statements, industry conditions, and other factors that affect its value. This approach looks at a company's earnings, revenue, profit margins, and overall economic environment to determine whether a stock is undervalued or overvalued.")

with col3:
    st.subheader('Sentiment Analysis')
    st.write('Sentiment analysis assesses the mood or tone of market participants. It involves analyzing the news using natural language processing (NLP) to give a sentiment.')

# Define the options and corresponding information
options = {
    "Select": "Please select an option:",
    "Development Bank of Singapore Ltd (DBS)": (
        "Overview: Established in 1968, DBS Bank is one of the largest and most prominent banks in Singapore. It has a strong presence in Asia and offers a wide range of financial services, including consumer banking, wealth management, and corporate banking.\n\n"
        "Assets: As of recent reports, DBS has total assets exceeding S$646 billion, making it one of the most financially robust institutions in the region.\n\n"
        "Reputation: Known for its innovative digital banking solutions and customer service, DBS has won numerous awards, including being named 'World’s Best Bank' by Euromoney in recent years."
    ),
    "Oversea-Chinese Banking Corporation Ltd (OCBC)": (
        "OCBC Bank, formed in 1932 from the merger of three local banks, is the oldest local bank in Singapore. It offers a comprehensive range of financial services, including personal and business banking, investment banking, and asset management.\n\n"
        "Assets: OCBC is well-capitalized with significant assets, contributing to its reputation as one of the safest banks.\n\n"
        "Reputation: The bank is renowned for its financial stability and innovative products, particularly in the wealth management sector."
    ),
    "United Overseas Bank Ltd (UOB)": (
        "Established in 1935, UOB is another major local bank in Singapore. It provides a wide range of financial services such as commercial and corporate banking, personal financial services, private banking, and asset management.\n\n"
        "Assets: UOB has a strong financial standing, with extensive operations not just in Singapore but across Asia, including Malaysia, Thailand, Indonesia, and China.\n\n"
        "Reputation: UOB is known for its prudent management and extensive network of branches across the region, making it a preferred bank for many businesses and individuals."
    )
}

# Create a selectbox for user to select a bank
selected_bank = st.selectbox("Choose a Bank:", list(options.keys()))

# Display the corresponding information
st.write(options[selected_bank])

# Get the current stock price based on the selected bank
if selected_bank == "Development Bank of Singapore Ltd (DBS)":
    ticker = "D05.SI"
elif selected_bank == "Oversea-Chinese Banking Corporation Ltd (OCBC)":
    ticker = "O39.SI"
elif selected_bank == "United Overseas Bank Ltd (UOB)":
    ticker = "U11.SI"
else:
    ticker = None

if ticker:
    stock = yf.Ticker(ticker)
    stock_price = stock.history(period="1d")['Close'][0]
    st.write(f"Current {selected_bank} stock price: ${stock_price:.2f}")

# Embed the Tableau dashboard using Streamlit's components.html
components.html(
    """<div class='tableauPlaceholder' id='viz1722992681749' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DB&#47;DBS1&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DBS1&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;DB&#47;DBS1&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1722992681749');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1400px';vizElement.style.height='900px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1400px';vizElement.style.height='900px';} else { vizElement.style.width='100%';vizElement.style.height='800px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>""",
    height=900,
)
