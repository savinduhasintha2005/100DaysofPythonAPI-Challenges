from pydantic import BaseModel


class TextRequest(BaseModel):
    text: str


class CharacterResponse(BaseModel):
    text: str
    total_characters: int
    characters_without_spaces: int
    total_words: int
    total_sentences: int
    total_lines: int