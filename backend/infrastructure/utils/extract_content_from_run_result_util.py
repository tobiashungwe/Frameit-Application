def extract_content_from_run_result(run_result):
    """Extracts the content from a RunResult object."""
    if hasattr(run_result, "_all_messages"):
        # Access the last ModelResponse in _all_messages
        for message in reversed(run_result._all_messages):
            if hasattr(message, "parts") and message.parts:
                # Extract the first part with content
                for part in message.parts:
                    if hasattr(part, "content"):
                        return part.content
    # Fallback: Try accessing the `data` attribute directly
    if hasattr(run_result, "data"):
        return run_result.data
    raise ValueError("Content not found in RunResult.")
