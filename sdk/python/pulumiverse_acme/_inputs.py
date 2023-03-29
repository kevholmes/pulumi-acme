# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'CertificateDnsChallengeArgs',
    'CertificateHttpChallengeArgs',
    'CertificateHttpMemcachedChallengeArgs',
    'CertificateHttpWebrootChallengeArgs',
    'CertificateTlsChallengeArgs',
    'RegistrationExternalAccountBindingArgs',
]

@pulumi.input_type
class CertificateDnsChallengeArgs:
    def __init__(__self__, *,
                 provider: pulumi.Input[str],
                 config: Optional[pulumi.Input[Mapping[str, Any]]] = None):
        pulumi.set(__self__, "provider", provider)
        if config is not None:
            pulumi.set(__self__, "config", config)

    @property
    @pulumi.getter
    def provider(self) -> pulumi.Input[str]:
        return pulumi.get(self, "provider")

    @provider.setter
    def provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider", value)

    @property
    @pulumi.getter
    def config(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        return pulumi.get(self, "config")

    @config.setter
    def config(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "config", value)


@pulumi.input_type
class CertificateHttpChallengeArgs:
    def __init__(__self__, *,
                 port: Optional[pulumi.Input[int]] = None,
                 proxy_header: Optional[pulumi.Input[str]] = None):
        if port is not None:
            pulumi.set(__self__, "port", port)
        if proxy_header is not None:
            pulumi.set(__self__, "proxy_header", proxy_header)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="proxyHeader")
    def proxy_header(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "proxy_header")

    @proxy_header.setter
    def proxy_header(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proxy_header", value)


@pulumi.input_type
class CertificateHttpMemcachedChallengeArgs:
    def __init__(__self__, *,
                 hosts: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(__self__, "hosts", hosts)

    @property
    @pulumi.getter
    def hosts(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "hosts")

    @hosts.setter
    def hosts(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "hosts", value)


@pulumi.input_type
class CertificateHttpWebrootChallengeArgs:
    def __init__(__self__, *,
                 directory: pulumi.Input[str]):
        pulumi.set(__self__, "directory", directory)

    @property
    @pulumi.getter
    def directory(self) -> pulumi.Input[str]:
        return pulumi.get(self, "directory")

    @directory.setter
    def directory(self, value: pulumi.Input[str]):
        pulumi.set(self, "directory", value)


@pulumi.input_type
class CertificateTlsChallengeArgs:
    def __init__(__self__, *,
                 port: Optional[pulumi.Input[int]] = None):
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)


@pulumi.input_type
class RegistrationExternalAccountBindingArgs:
    def __init__(__self__, *,
                 hmac_base64: pulumi.Input[str],
                 key_id: pulumi.Input[str]):
        pulumi.set(__self__, "hmac_base64", hmac_base64)
        pulumi.set(__self__, "key_id", key_id)

    @property
    @pulumi.getter(name="hmacBase64")
    def hmac_base64(self) -> pulumi.Input[str]:
        return pulumi.get(self, "hmac_base64")

    @hmac_base64.setter
    def hmac_base64(self, value: pulumi.Input[str]):
        pulumi.set(self, "hmac_base64", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_id", value)


