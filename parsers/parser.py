from models.response import Response, Choice, Message

def parse_response(data: dict) -> Response:
    """
    Parse a response dictionary into a Response object
    """
    choices = [Choice(
        index=choice["index"],
        message=Message(
            role=choice["message"]["role"],
            content=choice["message"]["content"]
        ),
        logprobs=choice["logprobs"],
        finish_reason=choice["finish_reason"]
    ) for choice in data["choices"]]
    usage = Usage(
        prompt_tokens=data["usage"]["prompt_tokens"],
        prompt_time=data["usage"]["prompt_time"],
        completion_tokens=data["usage"]["completion_tokens"],
        completion_time=data["usage"]["completion_time"],
        total_tokens=data["usage"]["total_tokens"],
        total_time=data["usage"]["total_time"]
    )
    system_fingerprint = SystemFingerprint(id=data["system_fingerprint"])
    x_groq = XGroq(id=data["x_groq"]["id"])
    return Response(
        id=data["id"],
        object=data["object"],
        created=data["created"],
        model=data["model"],
        choices=choices,
        usage=usage,
        system_fingerprint=system_fingerprint,
        x_groq=x_groq
    )