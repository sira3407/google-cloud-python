# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from .resources import Replication, Secret, SecretPayload, SecretVersion
from .service import (
    AccessSecretVersionRequest,
    AccessSecretVersionResponse,
    AddSecretVersionRequest,
    CreateSecretRequest,
    DeleteSecretRequest,
    DestroySecretVersionRequest,
    DisableSecretVersionRequest,
    EnableSecretVersionRequest,
    GetSecretRequest,
    GetSecretVersionRequest,
    ListSecretsRequest,
    ListSecretsResponse,
    ListSecretVersionsRequest,
    ListSecretVersionsResponse,
    UpdateSecretRequest,
)

__all__ = (
    "Replication",
    "Secret",
    "SecretPayload",
    "SecretVersion",
    "AccessSecretVersionRequest",
    "AccessSecretVersionResponse",
    "AddSecretVersionRequest",
    "CreateSecretRequest",
    "DeleteSecretRequest",
    "DestroySecretVersionRequest",
    "DisableSecretVersionRequest",
    "EnableSecretVersionRequest",
    "GetSecretRequest",
    "GetSecretVersionRequest",
    "ListSecretsRequest",
    "ListSecretsResponse",
    "ListSecretVersionsRequest",
    "ListSecretVersionsResponse",
    "UpdateSecretRequest",
)
