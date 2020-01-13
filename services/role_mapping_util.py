import pandas as pd
import os
import os.path


def prepare_excel_dataframe(sheet_name: str, df: pd.DataFrame, master_df):
    """
    Args:
        sheet_name:
    """
    print(f"sheet {sheet_name} has {df.count()} entries")
    df['Role'] = sheet_name
    if not master_df:
        master_df = df
    else:
        master_df.append(df)


def process_data(sheet_name: str, df=pd.DataFrame):
    role_users = df['uNumber'].astype(str).tolist()
    json_object = {"role_name": sheet_name,
                   "uNumbers": role_users}
    return json_object


def process_excel(file_path: str):
    """Process a given excel file into a dataframe
    Args:
        file_path: string containing the full path of the excel file
    """
    if not os.path.exists(file_path):
        raise Exception(f"no file found at location {file_path}")
    excel_file = pd.ExcelFile(io=file_path)
    master_df = pd.DataFrame()
    json = []
    for sheet_name in excel_file.sheet_names:
        json.append(process_data(sheet_name=sheet_name, df=excel_file.parse(sheet_name)))
    return (json)

# process_excel("/Users/asharma/Downloads/test_book.xlsx")
