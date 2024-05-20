import logging
from functools import wraps

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def logger(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)
            logging.info(f"Message: {func.__name__} executed successfully")
            return result
        except Exception as e:
            logging.error(f"An error occurred during {func.__name__}: {e}")
            raise e
    return wrapper
