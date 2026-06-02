# fábrica de clients boto3

"""Factory helpers for the read-only AWS clients the tools depend on.

Keeping client creation in one place makes the tools trivial to test: a test
just passes in a mock client instead of touching AWS at all.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import boto3

if TYPE_CHECKING:
    # Esses tipos vêm do boto3-stubs (dependência de dev) e só são usados na
    # checagem estática, então importar sob TYPE_CHECKING mantém o runtime leve.
    from mypy_boto3_ce import CostExplorerClient
    from mypy_boto3_resourcegroupstaggingapi import ResourceGroupsTaggingAPIClient


def cost_explorer_client(region: str) -> CostExplorerClient:
    """Return a Cost Explorer client.

    Note: Cost Explorer is a global service whose endpoint lives in us-east-1,
    but the client accepts a region for signing.
    """
    return boto3.client("ce", region_name=region)


def tagging_client(region: str) -> ResourceGroupsTaggingAPIClient:
    """Return a Resource Groups Tagging API client for the given region."""
    return boto3.client("resourcegroupstaggingapi", region_name=region)
