def retry_llm_call(func, retries=2):
    for attempt in range(retries):
        try:
            result = func()

            if result and len(result.strip()) > 0:
                return result

        except Exception as e:
            print(f"⚠️ Retry {attempt + 1} failed:", e)

    return None