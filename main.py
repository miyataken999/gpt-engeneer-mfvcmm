from parsers.parser import parse_response

def extract_content(response: dict) -> str:
    """
    Extract the content from a response dictionary
    """
    response_obj = parse_response(response)
    return response_obj.choices[0].message.content

# Example usage
response_data = {
    "id": "chatcmpl-ef674b28-e0f2-4206-a984-210e4a87bf96",
    "object": "chat.completion",
    "created": 1718274887,
    "model": "llama3-8b-8192",
    "choices": [{
        "index": 0,
        "message": {
            "role": "assistant",
            "content": "It looks like you typed \"test\"! Is there something specific you'd like to talk about or ask? I'm here to help and happy to chat!"
        },
        "logprobs": None,
        "finish_reason": "stop"
    }],
    "usage": {
        "prompt_tokens": 11,
        "prompt_time": 0.003524046,
        "completion_tokens": 33,
        "completion_time": 0.025700521,
        "total_tokens": 44,
        "total_time": 0.029224567
    },
    "system_fingerprint": "fp_873a560973",
    "x_groq": {
        "id": "req_01j08jm3hteh5s46fpgsrswvrt"
    }
}

content = extract_content(response_data)
print(content)  # Output: It looks like you typed "test"! Is there something specific you'd like to talk about or ask? I'm here to help and happy to chat!