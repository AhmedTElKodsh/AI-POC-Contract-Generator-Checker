"""
LLM API Fallback Handler

Provides resilient LLM API calling with automatic fallback between providers.
Supports OpenAI, Anthropic, and other configured providers.
"""

import os
import asyncio
from typing import List, Dict, Any, Optional
from enum import Enum


class LLMProvider(Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    GEMINI = "gemini"
    GROQ = "groq"
    MISTRAL = "mistral"
    COHERE = "cohere"
    OLLAMA = "ollama"
    HUGGINGFACE = "huggingface"


class LLMFallbackManager:
    """
    Manages LLM API calls with automatic fallback between providers.
    """

    def __init__(self, providers: List[LLMProvider] = None, max_retries: int = 3):
        if providers is None:
            providers = [
                LLMProvider.OPENAI,
                LLMProvider.ANTHROPIC,
                LLMProvider.GEMINI,
                LLMProvider.GROQ,
                LLMProvider.MISTRAL,
                LLMProvider.COHERE,
            ]

        self.providers = providers
        self.max_retries = max_retries

        # Initialize API keys from environment
        self.api_keys = {
            LLMProvider.OPENAI: os.getenv("OPENAI_API_KEY"),
            LLMProvider.ANTHROPIC: os.getenv("ANTHROPIC_API_KEY"),
            LLMProvider.GEMINI: os.getenv("GEMINI_API_KEY"),
            LLMProvider.GROQ: os.getenv("GROQ_API_KEY"),
            LLMProvider.MISTRAL: os.getenv("MISTRAL_API_KEY"),
            LLMProvider.COHERE: os.getenv("COHERE_API_KEY"),
            LLMProvider.OLLAMA: os.getenv("OLLAMA_API_KEY"),
            LLMProvider.HUGGINGFACE: os.getenv("HUGGING_API_KEY"),
        }

        # Validate providers have API keys
        for provider in self.providers:
            if not self.api_keys.get(provider):
                print(f"Warning: No API key found for {provider.value}")

    async def call_llm(
        self,
        prompt: str,
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Call LLM with automatic fallback between providers.

        Args:
            prompt: The input prompt
            model: Model name (provider-specific)
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            **kwargs: Additional provider-specific parameters

        Returns:
            Dict containing response, provider used, and metadata
        """

        last_error = None

        for provider in self.providers:
            try:
                # Check if provider has API key
                if not self.api_keys.get(provider):
                    continue

                print(f"Trying {provider.value}...")

                # Call the specific provider
                response = await self._call_provider(
                    provider=provider,
                    prompt=prompt,
                    model=model,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    **kwargs,
                )

                return {
                    "response": response,
                    "provider": provider.value,
                    "success": True,
                    "error": None,
                }

            except Exception as e:
                error_msg = f"{provider.value} failed: {str(e)}"
                print(f"Error: {error_msg}")
                last_error = error_msg

                # Continue to next provider
                continue

        # All providers failed
        return {
            "response": None,
            "provider": None,
            "success": False,
            "error": f"All providers failed. Last error: {last_error}",
        }

    async def _call_provider(
        self,
        provider: LLMProvider,
        prompt: str,
        model: str,
        temperature: float,
        max_tokens: int,
        **kwargs,
    ) -> str:
        """Call specific LLM provider"""

        if provider == LLMProvider.OPENAI:
            return await self._call_openai(prompt, model, temperature, max_tokens, **kwargs)

        elif provider == LLMProvider.ANTHROPIC:
            return await self._call_anthropic(prompt, model, temperature, max_tokens, **kwargs)

        elif provider == LLMProvider.GEMINI:
            return await self._call_gemini(prompt, model, temperature, max_tokens, **kwargs)

        elif provider == LLMProvider.GROQ:
            return await self._call_groq(prompt, model, temperature, max_tokens, **kwargs)

        elif provider == LLMProvider.MISTRAL:
            return await self._call_mistral(prompt, model, temperature, max_tokens, **kwargs)

        elif provider == LLMProvider.COHERE:
            return await self._call_cohere(prompt, model, temperature, max_tokens, **kwargs)

        elif provider == LLMProvider.OLLAMA:
            return await self._call_ollama(prompt, model, temperature, max_tokens, **kwargs)

        elif provider == LLMProvider.HUGGINGFACE:
            return await self._call_huggingface(prompt, model, temperature, max_tokens, **kwargs)

        else:
            raise ValueError(f"Unsupported provider: {provider}")

    async def _call_openai(
        self,
        prompt: str,
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call OpenAI API"""
        try:
            from openai import AsyncOpenAI

            client = AsyncOpenAI(api_key=self.api_keys[LLMProvider.OPENAI])

            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs,
            )

            return response.choices[0].message.content

        except ImportError:
            raise Exception("OpenAI package not installed")
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")

    async def _call_anthropic(
        self,
        prompt: str,
        model: str = "claude-3-sonnet-20240229",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call Anthropic API"""
        try:
            import anthropic

            client = anthropic.AsyncAnthropic(api_key=self.api_keys[LLMProvider.ANTHROPIC])

            response = await client.messages.create(
                model=model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                **kwargs,
            )

            return response.content[0].text

        except ImportError:
            raise Exception("Anthropic package not installed")
        except Exception as e:
            raise Exception(f"Anthropic API error: {str(e)}")

    async def _call_gemini(
        self,
        prompt: str,
        model: str = "gemini-pro",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call Google Gemini API"""
        try:
            import google.generativeai as genai

            genai.configure(api_key=self.api_keys[LLMProvider.GEMINI])

            generation_config = genai.types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )

            model_instance = genai.GenerativeModel(
                model_name=model, generation_config=generation_config
            )
            response = await model_instance.generate_content_async(prompt)

            return response.text

        except ImportError:
            raise Exception("google-generativeai package not installed")
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")

    async def _call_groq(
        self,
        prompt: str,
        model: str = "llama2-70b-4096",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call Groq API"""
        try:
            from groq import AsyncGroq

            client = AsyncGroq(api_key=self.api_keys[LLMProvider.GROQ])

            response = await client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs,
            )

            return response.choices[0].message.content

        except ImportError:
            raise Exception("groq package not installed")
        except Exception as e:
            raise Exception(f"Groq API error: {str(e)}")

    async def _call_mistral(
        self,
        prompt: str,
        model: str = "mistral-medium",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call Mistral API"""
        try:
            from mistralai import Mistral

            client = Mistral(api_key=self.api_keys[LLMProvider.MISTRAL])

            response = await client.chat.complete_async(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs,
            )

            return response.choices[0].message.content

        except ImportError:
            raise Exception("mistralai package not installed")
        except Exception as e:
            raise Exception(f"Mistral API error: {str(e)}")

    async def _call_cohere(
        self,
        prompt: str,
        model: str = "command",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call Cohere API"""
        try:
            import cohere

            client = cohere.Client(api_key=self.api_keys[LLMProvider.COHERE])

            response = client.generate(
                model=model,
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs,
            )

            return response.generations[0].text

        except ImportError:
            raise Exception("cohere package not installed")
        except Exception as e:
            raise Exception(f"Cohere API error: {str(e)}")

    async def _call_ollama(
        self,
        prompt: str,
        model: str = "llama2",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call Ollama API"""
        try:
            import httpx

            # Assuming Ollama runs locally on port 11434
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://localhost:11434/api/generate",
                    json={
                        "model": model,
                        "prompt": prompt,
                        "stream": False,
                        "options": {
                            "temperature": temperature,
                            "num_predict": max_tokens,
                        },
                    },
                )
                response.raise_for_status()
                data = response.json()
                return data.get("response", "")

        except ImportError:
            raise Exception("httpx package not installed")
        except Exception as e:
            raise Exception(f"Ollama API error: {str(e)}")

    async def _call_huggingface(
        self,
        prompt: str,
        model: str = "gpt2",
        temperature: float = 0.7,
        max_tokens: int = 1000,
        **kwargs,
    ) -> str:
        """Call HuggingFace Inference API"""
        try:
            import httpx

            headers = {"Authorization": f"Bearer {self.api_keys[LLMProvider.HUGGINGFACE]}"}

            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"https://api-inference.huggingface.co/models/{model}",
                    headers=headers,
                    json={
                        "inputs": prompt,
                        "parameters": {
                            "temperature": temperature,
                            "max_new_tokens": max_tokens,
                        },
                    },
                )
                response.raise_for_status()
                data = response.json()

                # Handle different response formats
                if isinstance(data, list) and data:
                    return data[0].get("generated_text", "").replace(prompt, "").strip()
                return str(data)

        except ImportError:
            raise Exception("httpx package not installed")
        except Exception as e:
            raise Exception(f"HuggingFace API error: {str(e)}")


# Global instance for easy use
llm_manager = LLMFallbackManager()


async def call_llm_with_fallback(
    prompt: str, model: str = "gpt-4", temperature: float = 0.7, max_tokens: int = 1000, **kwargs
) -> Dict[str, Any]:
    """
    Convenience function to call LLM with fallback.

    Use this function whenever you need to call an LLM API provider.
    It will automatically try providers in order until one succeeds.
    """
    return await llm_manager.call_llm(
        prompt=prompt, model=model, temperature=temperature, max_tokens=max_tokens, **kwargs
    )


# Synchronous wrapper for convenience
def call_llm_sync(
    prompt: str, model: str = "gpt-4", temperature: float = 0.7, max_tokens: int = 1000, **kwargs
) -> Dict[str, Any]:
    """Synchronous wrapper for call_llm_with_fallback"""
    try:
        # Try to get event loop
        loop = asyncio.get_event_loop()
        if loop.is_running():
            # If loop is running, use run_until_complete in a new thread
            import concurrent.futures

            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(
                    asyncio.run,
                    call_llm_with_fallback(prompt, model, temperature, max_tokens, **kwargs),
                )
                return future.result()
        else:
            return loop.run_until_complete(
                call_llm_with_fallback(prompt, model, temperature, max_tokens, **kwargs)
            )
    except RuntimeError:
        # No event loop, create new one
        return asyncio.run(call_llm_with_fallback(prompt, model, temperature, max_tokens, **kwargs))
