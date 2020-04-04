# pandas_markdown_summary
Markdown summaries of pandas DataFrame and Series

### Installation - 

```
pip install pandas_md_summary
```

### Usage
To generate markdown summary for a pandas DataFrame - 
```
from pandas_md_summary import gen_markdown_for_df
gen_markdown_for_df(df, 'therapy', out_dir='out, top=100)
# df is the DataFrame
# 'therapy' is a label for the table name. The generated table summary and folder will be named using this variable.
# out_dir - the path where you would want the markdown summary generated
# top - the number of most frequent values to include in each column summary of the DataFrame.
```


Refer Example.ipynb for a full example