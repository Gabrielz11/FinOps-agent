# configurações tipadas

"""Application configuration.

All settings are read from environment variables prefixed with ``FINOPS_``
(e.g. ``FINOPS_MODEL_ID``). Defaults are chosen so the agent is cheap to run
during development.
"""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime configuration for the FinOps agent."""

    model_config = SettingsConfigDict(env_prefix="FINOPS_", env_file=".env")

    # Modelo Bedrock usado para o raciocínio. Default num modelo pequeno/barato;
    # troque por um maior só no demo final. Confirme que esse id está habilitado
    # na sua conta/região em Bedrock > Model access.
    model_id: str = "us.anthropic.claude-3-5-haiku-20241022-v1:0"

    # Região AWS para o Bedrock e para as APIs de dados.
    region: str = "us-east-1"

    # Guardrail de custo: teto de passos de raciocínio (chamadas ao modelo) por
    # requisição. Impede um loop descontrolado de torrar o LLM e inflar a conta.
    max_iterations: int = 8

    # Teto de tokens de saída por chamada (segundo guardrail de custo).
    max_tokens: int = 2048

    # Tags que todo recurso deveria ter. Recursos sem alguma delas são sinalizados
    # pela ferramenta de auditoria.
    required_tags: list[str] = ["Environment", "Owner", "CostCenter"]


def get_settings() -> Settings:
    """Return a fresh ``Settings`` instance read from the environment."""
    return Settings()
