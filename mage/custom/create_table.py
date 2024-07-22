import psycopg2
import psycopg2.extras


if 'custom' not in globals():
    from mage_ai.data_preparation.decorators import custom
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def setup_database():
    conn = psycopg2.connect(
        dbname='mage',
        user='postgres',
        password='postgres',
        host='postgres',
        port='5432'
    )
    create_table_if_not_exists(conn)
    return conn


@custom
def create_table_if_not_exists(data):
    conn = setup_database(
        
    )

    create_table_query = """
    CREATE TABLE IF NOT EXISTS predictions (
        id SERIAL PRIMARY KEY,
        distance_from_home FLOAT,
        distance_from_last_transaction FLOAT,
        ratio_to_median_purchase_price FLOAT,
        repeat_retailer BOOLEAN,
        used_chip BOOLEAN,
        used_pin_number BOOLEAN,
        online_order BOOLEAN,
        prediction FLOAT,
        ground_truth FLOAT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    with conn.cursor() as cursor:
        cursor.execute(create_table_query)
        conn.commit()


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
