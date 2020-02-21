# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/phishingprotection_v1beta1/proto/phishingprotection.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.api import resource_pb2 as google_dot_api_dot_resource__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/phishingprotection_v1beta1/proto/phishingprotection.proto",
    package="google.cloud.phishingprotection.v1beta1",
    syntax="proto3",
    serialized_options=_b(
        "\n%com.google.phishingprotection.v1beta1B\027PhishingProtectionProtoP\001ZYgoogle.golang.org/genproto/googleapis/cloud/phishingprotection/v1beta1;phishingprotection\242\002\004GCPP\252\002'Google.Cloud.PhishingProtection.V1Beta1\312\002'Google\\Cloud\\PhishingProtection\\V1beta1"
    ),
    serialized_pb=_b(
        '\nFgoogle/cloud/phishingprotection_v1beta1/proto/phishingprotection.proto\x12\'google.cloud.phishingprotection.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"n\n\x15ReportPhishingRequest\x12\x43\n\x06parent\x18\x01 \x01(\tB3\xe0\x41\x02\xfa\x41-\n+cloudresourcemanager.googleapis.com/Project\x12\x10\n\x03uri\x18\x02 \x01(\tB\x03\xe0\x41\x02"\x18\n\x16ReportPhishingResponse2\xd3\x02\n PhishingProtectionServiceV1Beta1\x12\xd7\x01\n\x0eReportPhishing\x12>.google.cloud.phishingprotection.v1beta1.ReportPhishingRequest\x1a?.google.cloud.phishingprotection.v1beta1.ReportPhishingResponse"D\x82\xd3\xe4\x93\x02\x31",/v1beta1/{parent=projects/*}/phishing:report:\x01*\xda\x41\nparent,uri\x1aU\xca\x41!phishingprotection.googleapis.com\xd2\x41.https://www.googleapis.com/auth/cloud-platformB\xf8\x01\n%com.google.phishingprotection.v1beta1B\x17PhishingProtectionProtoP\x01ZYgoogle.golang.org/genproto/googleapis/cloud/phishingprotection/v1beta1;phishingprotection\xa2\x02\x04GCPP\xaa\x02\'Google.Cloud.PhishingProtection.V1Beta1\xca\x02\'Google\\Cloud\\PhishingProtection\\V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_api_dot_client__pb2.DESCRIPTOR,
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_api_dot_resource__pb2.DESCRIPTOR,
    ],
)


_REPORTPHISHINGREQUEST = _descriptor.Descriptor(
    name="ReportPhishingRequest",
    full_name="google.cloud.phishingprotection.v1beta1.ReportPhishingRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="parent",
            full_name="google.cloud.phishingprotection.v1beta1.ReportPhishingRequest.parent",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b(
                "\340A\002\372A-\n+cloudresourcemanager.googleapis.com/Project"
            ),
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="uri",
            full_name="google.cloud.phishingprotection.v1beta1.ReportPhishingRequest.uri",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=_b("").decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=_b("\340A\002"),
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=230,
    serialized_end=340,
)


_REPORTPHISHINGRESPONSE = _descriptor.Descriptor(
    name="ReportPhishingResponse",
    full_name="google.cloud.phishingprotection.v1beta1.ReportPhishingResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=342,
    serialized_end=366,
)

DESCRIPTOR.message_types_by_name["ReportPhishingRequest"] = _REPORTPHISHINGREQUEST
DESCRIPTOR.message_types_by_name["ReportPhishingResponse"] = _REPORTPHISHINGRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReportPhishingRequest = _reflection.GeneratedProtocolMessageType(
    "ReportPhishingRequest",
    (_message.Message,),
    dict(
        DESCRIPTOR=_REPORTPHISHINGREQUEST,
        __module__="google.cloud.phishingprotection_v1beta1.proto.phishingprotection_pb2",
        __doc__="""The ReportPhishing request message.
  
  
  Attributes:
      parent:
          Required. The name of the project for which the report will be
          created, in the format "projects/{project\_number}".
      uri:
          Required. The URI that is being reported for phishing content
          to be analyzed.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.phishingprotection.v1beta1.ReportPhishingRequest)
    ),
)
_sym_db.RegisterMessage(ReportPhishingRequest)

ReportPhishingResponse = _reflection.GeneratedProtocolMessageType(
    "ReportPhishingResponse",
    (_message.Message,),
    dict(
        DESCRIPTOR=_REPORTPHISHINGRESPONSE,
        __module__="google.cloud.phishingprotection_v1beta1.proto.phishingprotection_pb2",
        __doc__="""The ReportPhishing (empty) response message.
  
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.phishingprotection.v1beta1.ReportPhishingResponse)
    ),
)
_sym_db.RegisterMessage(ReportPhishingResponse)


DESCRIPTOR._options = None
_REPORTPHISHINGREQUEST.fields_by_name["parent"]._options = None
_REPORTPHISHINGREQUEST.fields_by_name["uri"]._options = None

_PHISHINGPROTECTIONSERVICEV1BETA1 = _descriptor.ServiceDescriptor(
    name="PhishingProtectionServiceV1Beta1",
    full_name="google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1",
    file=DESCRIPTOR,
    index=0,
    serialized_options=_b(
        "\312A!phishingprotection.googleapis.com\322A.https://www.googleapis.com/auth/cloud-platform"
    ),
    serialized_start=369,
    serialized_end=708,
    methods=[
        _descriptor.MethodDescriptor(
            name="ReportPhishing",
            full_name="google.cloud.phishingprotection.v1beta1.PhishingProtectionServiceV1Beta1.ReportPhishing",
            index=0,
            containing_service=None,
            input_type=_REPORTPHISHINGREQUEST,
            output_type=_REPORTPHISHINGRESPONSE,
            serialized_options=_b(
                '\202\323\344\223\0021",/v1beta1/{parent=projects/*}/phishing:report:\001*\332A\nparent,uri'
            ),
        )
    ],
)
_sym_db.RegisterServiceDescriptor(_PHISHINGPROTECTIONSERVICEV1BETA1)

DESCRIPTOR.services_by_name[
    "PhishingProtectionServiceV1Beta1"
] = _PHISHINGPROTECTIONSERVICEV1BETA1

# @@protoc_insertion_point(module_scope)
