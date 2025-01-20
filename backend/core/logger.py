import logfire

def setup_logger():
    logfire.configure()
    logfire.install_auto_tracing(
        modules=["backend"], 
        min_duration=0.01, 
        check_imported_modules="warn"
    )
    return logfire

logger = setup_logger()
