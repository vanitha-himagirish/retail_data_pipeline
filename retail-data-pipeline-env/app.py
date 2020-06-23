import sys

from util import get_tables, load_db_details
from read import *
from write import *

def main():

    #env = sys.argv[0] -- Need to check..Im getting error for system environment variables
    db_details = load_db_details('dev')

    #Loading dimension - Product table
    pd=getProducts(db_details)
    load_data(db_details,pd,'dim_products')
    print('Completed Product Dimension table load')

    #Loading dimension - Customer table


if __name__ == '__main__':
    main()