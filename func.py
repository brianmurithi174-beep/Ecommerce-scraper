import pandas as pd

with open("C:/Users/hp/Downloads/Fundingstack_Investor_Template_Fiverr.xlsx", "rb") as f:
    raw = f.read()

text = raw.decode("utf-8", errors="ignore")
from io import StringIO
import pandas as pd

df = pd.read_csv(
    StringIO(text),
    engine="python",
    sep=",",
    on_bad_lines="skip"
)


