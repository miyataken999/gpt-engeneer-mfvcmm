from dataclasses import dataclass

@dataclass
class Message:
    role: str
    content: str

@dataclass
class Choice:
    index: int
    message: Message
    logprobs: str
    finish_reason: str

@dataclass
class Usage:
    prompt_tokens: int
    prompt_time: float
    completion_tokens: int
    completion_time: float
    total_tokens: int
    total_time: float

@dataclass
class SystemFingerprint:
    id: str

@dataclass
class XGroq:
    id: str

@dataclass
class Response:
    id: str
    object: str
    created: int
    model: str
    choices: list[Choice]
    usage: Usage
    system_fingerprint: SystemFingerprint
    x_groq: XGroq