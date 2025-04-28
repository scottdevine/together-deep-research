from typing import Any, Optional
import json
import os

import tenacity
from together import Together


@tenacity.retry(stop=tenacity.stop_after_attempt(3), wait=tenacity.wait_exponential(multiplier=1, min=4, max=15))
async def asingle_shot_llm_call(
    model: str,
    system_prompt: str,
    message: str,
    response_format: Optional[dict[str, str | dict[str, Any]]] = None,
    max_completion_tokens: int | None = None,
) -> str:
    # Use the Together API directly instead of litellm
    # This avoids the provider format issues with litellm
    # Note: Together API doesn't support async operations, so we use the synchronous API
    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

    # Check if response_format is specified
    if response_format is not None and response_format.get("type") == "json_object" and "schema" in response_format:
        # For Together AI models, we need to handle JSON formatting differently
        # Add instructions to the system prompt instead
        schema_str = json.dumps(response_format["schema"], indent=2)
        enhanced_system_prompt = f"{system_prompt}\n\nYour response must be a valid JSON object that conforms to this schema:\n{schema_str}\n\nEnsure your response is properly formatted JSON with no additional text."

        # Call the Together API directly (synchronously)
        response = client.chat.completions.create(
            model=model,  # Use the model name directly
            messages=[
                {"role": "system", "content": enhanced_system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.0,
            max_tokens=max_completion_tokens if max_completion_tokens else 1024
        )
        return response.choices[0].message.content

    # For when no response_format is specified
    response = client.chat.completions.create(
        model=model,  # Use the model name directly
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.0,
        max_tokens=max_completion_tokens if max_completion_tokens else 1024
    )
    return response.choices[0].message.content


@tenacity.retry(stop=tenacity.stop_after_attempt(3), wait=tenacity.wait_exponential(multiplier=1, min=4, max=15))
def single_shot_llm_call(
    model: str,
    system_prompt: str,
    message: str,
    response_format: Optional[dict[str, str | dict[str, Any]]] = None,
    max_completion_tokens: int | None = None,
) -> str:
    # Use the Together API directly instead of litellm
    # This avoids the provider format issues with litellm
    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

    # Check if response_format is specified
    if response_format is not None and response_format.get("type") == "json_object" and "schema" in response_format:
        # For Together AI models, we need to handle JSON formatting differently
        # Add instructions to the system prompt instead
        schema_str = json.dumps(response_format["schema"], indent=2)
        enhanced_system_prompt = f"{system_prompt}\n\nYour response must be a valid JSON object that conforms to this schema:\n{schema_str}\n\nEnsure your response is properly formatted JSON with no additional text."

        # Call the Together API directly
        response = client.chat.completions.create(
            model=model,  # Use the model name directly
            messages=[
                {"role": "system", "content": enhanced_system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.0,
            max_tokens=max_completion_tokens if max_completion_tokens else 1024
        )
        return response.choices[0].message.content

    # For when no response_format is specified
    response = client.chat.completions.create(
        model=model,  # Use the model name directly
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        temperature=0.0,
        max_tokens=max_completion_tokens if max_completion_tokens else 1024
    )
    return response.choices[0].message.content



def generate_toc_image(prompt: str, planning_model: str, topic: str) -> str:
    """Generate a table of contents image"""

    image_generation_prompt = single_shot_llm_call(
        model=planning_model, system_prompt=prompt, message=f"Research Topic: {topic}")

    if image_generation_prompt is None:
        raise ValueError("Image generation prompt is None")

    # HERE WE CALL THE TOGETHER API SINCE IT'S AN IMAGE GENERATION REQUEST
    client = Together()
    imageCompletion = client.images.generate(
        model="black-forest-labs/FLUX.1-dev",
        width=1024,
        height=768,
        steps=28,
        prompt=image_generation_prompt,
    )

    return imageCompletion.data[0].url  # type: ignore


