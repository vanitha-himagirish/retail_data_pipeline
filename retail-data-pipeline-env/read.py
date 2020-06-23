from util import get_connection
import pandas as pd
from pandas import DataFrame
import datetime

def read_table(db_details, table_name, limit=0):
    SOURCE_DB = db_details['SOURCE_DB']

    connection = get_connection(db_type=SOURCE_DB['DB_TYPE'],
                                db_host=SOURCE_DB['DB_HOST'],
                                db_name=SOURCE_DB['DB_NAME'],
                                db_user=SOURCE_DB['DB_USER'],
                                db_pass=SOURCE_DB['DB_PASS']
                                )
    cursor = connection.cursor()
    if limit == 0:
        query = f'SELECT * FROM {table_name}'
    else:
        query = f'SELECT * FROM {table_name} LIMIT {limit}'
    cursor.execute(query)
    data = cursor.fetchall()
    column_names = cursor.column_names
    df = pd.DataFrame(data=data,columns=column_names)
    return df
    connection.close()

#Get the product details
def getProducts(db_details):
    df_products = pd.DataFrame(read_table(db_details, 'products'),columns=['product_id','product_name','product_price','product_category_id'])
    df_categories = pd.DataFrame(read_table(db_details, 'categories'),columns=['category_id','category_name','category_department_id'])
    df_departments =pd.DataFrame(read_table(db_details, 'departments'),columns=['department_id','department_name'])
    batch_id = datetime.datetime.now().timestamp()
    batch_name="PRODUCT"
    df_join = pd.merge(df_products,pd.merge(df_departments,df_categories,how="inner",left_on="department_id",right_on='category_department_id'), how="inner",left_on="product_category_id",right_on="category_id")
    df_join['batch_id']=batch_id
    df_join['batch_name']=batch_name
    df_join=pd.DataFrame(df_join,columns=['product_id','product_name','product_price','category_id','category_name','department_id','department_name','batch_id','batch_name'])
    return df_join