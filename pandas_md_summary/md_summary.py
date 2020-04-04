from .templates import md_template, table_md_template, column_md_template
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os
from functools import reduce

def ser_to_markdown(ser,top=100):
    total_entries = ser.shape[0]
    num_missing = ser.isna().sum()
    ser_df = pd.DataFrame(ser.value_counts()).reset_index()
    ser_df.columns = ['value', 'count']
    ser_df = ser_df.set_index('value')
    table_md = ser_df.iloc[:top].to_markdown()
    md_out = md_template.format(ser.name, total_entries, num_missing, top, table_md, 
                                ((num_missing / total_entries) * 100))
    return md_out

def ser_to_markdown_file(ser, out_dir='.',top=100):
    md_str = ser_to_markdown(ser,top=top)
    out_dir = Path(out_dir)
    with open(out_dir / f'{ser.name.replace("/", ".")}.md', 'w') as f:
        f.write(md_str)
              
def proc_md_col(df, col, out_dir, top=100):
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    ser = df[col]
    ser_to_markdown_file(ser, out_dir=out_dir, top=top)
    md_for_col = column_md_template.format(col, f'{out_dir}/{col}.md')
    return md_for_col

        
def gen_markdown_for_df(df, table_name, out_dir='.', top=100):
    out_dir = Path(out_dir)
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    col_heading_md = reduce(lambda acc, col: acc + proc_md_col(df, col, out_dir/table_name,top=top) + '\n', 
                   df.columns, '')

    table_md_out = table_md_template.format(table_name, col_heading_md)
    with open(out_dir / f'{table_name}.md', 'w') as f:
        f.write(table_md_out)