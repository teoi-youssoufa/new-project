import logging

def main():
    # Set up logging configuration
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("app.log")
        ]
    )

    # Log some messages
    logging.info("Application started")
    logging.warning("This is a warning message")
    logging.error("An error occurred")

if __name__ == "__main__":
    main()
