def chunk_text(text, chunk_size=2):

    # Split text into sentences
    sentences = text.split(".")

    chunks = []

    current_chunk = []

    for sentence in sentences:

        sentence = sentence.strip()

        if sentence:

            current_chunk.append(sentence)

        # Create chunk after enough sentences
        if len(current_chunk) >= chunk_size:

            chunk = ". ".join(current_chunk) + "."
            chunks.append(chunk)

            current_chunk = []

    # Add remaining sentences
    if current_chunk:

        chunk = ". ".join(current_chunk) + "."
        chunks.append(chunk)

    return chunks