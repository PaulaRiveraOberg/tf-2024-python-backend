from client import course_saga, saga_compensating_transaction

if __name__ == "__main__":
    print("Starting transaction orchestrator")
    saga_failed = course_saga()

    if saga_failed:
        print("Saga failed, starting compensating transaction")
        saga_compensating_transaction()
