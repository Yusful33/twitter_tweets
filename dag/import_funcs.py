from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
## Remember admin for airflow 

# Operators; we need this to operate!
from airflow.operators.python_operator import PythonOperator

from twitter_app import grab_tweets 
from twitter_app import get_top_replies 

with DAG(
    'import_funcs',
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        'depends_on_past': False,
        'email': ['ycattaneo33@gmail.com'],
        'email_on_failure': True,
        'email_on_retry': True,
        'retries': 1,
        'retry_delay': timedelta(minutes=1),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
        # 'on_retry_callback': another_function,
        # 'sla_miss_callback': yet_another_function,
        # 'trigger_rule': 'all_success'
    },
    description='Sourcing data from Twitter, Loading to MongoDB and then pushing to SMS via Twilio.',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2022, 8, 1),
    catchup=True,
    tags=['twitter'],
) as dag:

    t1 = PythonOperator(
        task_id='get_tweets',
        python_callable= grab_tweets.main(),
        dag=dag,
    )

    t2 = PythonOperator(
        task_id='top_replies',
        python_callable= get_top_replies.main(),
        dag=dag,
    )
# Ordering of tasks
    t1 >> t2