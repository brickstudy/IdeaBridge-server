import logging


LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


def setup_logger(name):
    """각 모듈에서 사용할 로거 세팅"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG) 
    
    # Create console handler and set level to info
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # 콘솔에는 INFO 이상만 출력
    console_formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(console_formatter)
    
    # TODO: 외부 logger 저장 필요
    
    logger.addHandler(console_handler)
    return logger
