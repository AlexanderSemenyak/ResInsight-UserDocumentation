# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NNCProperties.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Case_pb2 as Case__pb2
import Definitions_pb2 as Definitions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='NNCProperties.proto',
  package='rips',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13NNCProperties.proto\x12\x04rips\x1a\nCase.proto\x1a\x11\x44\x65\x66initions.proto\"R\n\x14\x41vailableNNCProperty\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\rproperty_type\x18\x02 \x01(\x0e\x32\x15.rips.NNCPropertyType\"H\n\x16\x41vailableNNCProperties\x12.\n\nproperties\x18\x01 \x03(\x0b\x32\x1a.rips.AvailableNNCProperty\"{\n\rNNCConnection\x12\x18\n\x10\x63\x65ll_grid_index1\x18\x01 \x01(\x05\x12\x18\n\x10\x63\x65ll_grid_index2\x18\x02 \x01(\x05\x12\x1a\n\x05\x63\x65ll1\x18\x03 \x01(\x0b\x32\x0b.rips.Vec3i\x12\x1a\n\x05\x63\x65ll2\x18\x04 \x01(\x0b\x32\x0b.rips.Vec3i\":\n\x0eNNCConnections\x12(\n\x0b\x63onnections\x18\x01 \x03(\x0b\x32\x13.rips.NNCConnection\"{\n\x10NNCValuesRequest\x12\x0f\n\x07\x63\x61se_id\x18\x01 \x01(\x05\x12\x15\n\rproperty_name\x18\x02 \x01(\t\x12,\n\rproperty_type\x18\x03 \x01(\x0e\x32\x15.rips.NNCPropertyType\x12\x11\n\ttime_step\x18\x04 \x01(\x05\"\x1b\n\tNNCValues\x12\x0e\n\x06values\x18\x01 \x03(\x01\"\x83\x01\n\x15NNCValuesInputRequest\x12\x0f\n\x07\x63\x61se_id\x18\x01 \x01(\x05\x12\x15\n\rproperty_name\x18\x02 \x01(\t\x12/\n\x0eporosity_model\x18\x03 \x01(\x0e\x32\x17.rips.PorosityModelType\x12\x11\n\ttime_step\x18\x04 \x01(\x05\"o\n\x0eNNCValuesChunk\x12-\n\x06params\x18\x01 \x01(\x0b\x32\x1b.rips.NNCValuesInputRequestH\x00\x12!\n\x06values\x18\x02 \x01(\x0b\x32\x0f.rips.NNCValuesH\x00\x42\x0b\n\tChunkType*E\n\x0fNNCPropertyType\x12\x0f\n\x0bNNC_DYNAMIC\x10\x00\x12\x0e\n\nNNC_STATIC\x10\x01\x12\x11\n\rNNC_GENERATED\x10\x02\x32\xa9\x02\n\rNNCProperties\x12N\n\x19GetAvailableNNCProperties\x12\x11.rips.CaseRequest\x1a\x1c.rips.AvailableNNCProperties\"\x00\x12@\n\x11GetNNCConnections\x12\x11.rips.CaseRequest\x1a\x14.rips.NNCConnections\"\x00\x30\x01\x12;\n\x0cGetNNCValues\x12\x16.rips.NNCValuesRequest\x1a\x0f.rips.NNCValues\"\x00\x30\x01\x12I\n\x0cSetNNCValues\x12\x14.rips.NNCValuesChunk\x1a\x1f.rips.ClientToServerStreamReply\"\x00(\x01\x62\x06proto3'
  ,
  dependencies=[Case__pb2.DESCRIPTOR,Definitions__pb2.DESCRIPTOR,])

_NNCPROPERTYTYPE = _descriptor.EnumDescriptor(
  name='NNCPropertyType',
  full_name='rips.NNCPropertyType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NNC_DYNAMIC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NNC_STATIC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NNC_GENERATED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=804,
  serialized_end=873,
)
_sym_db.RegisterEnumDescriptor(_NNCPROPERTYTYPE)

NNCPropertyType = enum_type_wrapper.EnumTypeWrapper(_NNCPROPERTYTYPE)
NNC_DYNAMIC = 0
NNC_STATIC = 1
NNC_GENERATED = 2



_AVAILABLENNCPROPERTY = _descriptor.Descriptor(
  name='AvailableNNCProperty',
  full_name='rips.AvailableNNCProperty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='rips.AvailableNNCProperty.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='property_type', full_name='rips.AvailableNNCProperty.property_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=142,
)


_AVAILABLENNCPROPERTIES = _descriptor.Descriptor(
  name='AvailableNNCProperties',
  full_name='rips.AvailableNNCProperties',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='properties', full_name='rips.AvailableNNCProperties.properties', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=216,
)


_NNCCONNECTION = _descriptor.Descriptor(
  name='NNCConnection',
  full_name='rips.NNCConnection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cell_grid_index1', full_name='rips.NNCConnection.cell_grid_index1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cell_grid_index2', full_name='rips.NNCConnection.cell_grid_index2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cell1', full_name='rips.NNCConnection.cell1', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cell2', full_name='rips.NNCConnection.cell2', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=218,
  serialized_end=341,
)


_NNCCONNECTIONS = _descriptor.Descriptor(
  name='NNCConnections',
  full_name='rips.NNCConnections',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='connections', full_name='rips.NNCConnections.connections', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=401,
)


_NNCVALUESREQUEST = _descriptor.Descriptor(
  name='NNCValuesRequest',
  full_name='rips.NNCValuesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='case_id', full_name='rips.NNCValuesRequest.case_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='property_name', full_name='rips.NNCValuesRequest.property_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='property_type', full_name='rips.NNCValuesRequest.property_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_step', full_name='rips.NNCValuesRequest.time_step', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=526,
)


_NNCVALUES = _descriptor.Descriptor(
  name='NNCValues',
  full_name='rips.NNCValues',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='rips.NNCValues.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=528,
  serialized_end=555,
)


_NNCVALUESINPUTREQUEST = _descriptor.Descriptor(
  name='NNCValuesInputRequest',
  full_name='rips.NNCValuesInputRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='case_id', full_name='rips.NNCValuesInputRequest.case_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='property_name', full_name='rips.NNCValuesInputRequest.property_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='porosity_model', full_name='rips.NNCValuesInputRequest.porosity_model', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time_step', full_name='rips.NNCValuesInputRequest.time_step', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=558,
  serialized_end=689,
)


_NNCVALUESCHUNK = _descriptor.Descriptor(
  name='NNCValuesChunk',
  full_name='rips.NNCValuesChunk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='rips.NNCValuesChunk.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='rips.NNCValuesChunk.values', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='ChunkType', full_name='rips.NNCValuesChunk.ChunkType',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=691,
  serialized_end=802,
)

_AVAILABLENNCPROPERTY.fields_by_name['property_type'].enum_type = _NNCPROPERTYTYPE
_AVAILABLENNCPROPERTIES.fields_by_name['properties'].message_type = _AVAILABLENNCPROPERTY
_NNCCONNECTION.fields_by_name['cell1'].message_type = Definitions__pb2._VEC3I
_NNCCONNECTION.fields_by_name['cell2'].message_type = Definitions__pb2._VEC3I
_NNCCONNECTIONS.fields_by_name['connections'].message_type = _NNCCONNECTION
_NNCVALUESREQUEST.fields_by_name['property_type'].enum_type = _NNCPROPERTYTYPE
_NNCVALUESINPUTREQUEST.fields_by_name['porosity_model'].enum_type = Case__pb2._POROSITYMODELTYPE
_NNCVALUESCHUNK.fields_by_name['params'].message_type = _NNCVALUESINPUTREQUEST
_NNCVALUESCHUNK.fields_by_name['values'].message_type = _NNCVALUES
_NNCVALUESCHUNK.oneofs_by_name['ChunkType'].fields.append(
  _NNCVALUESCHUNK.fields_by_name['params'])
_NNCVALUESCHUNK.fields_by_name['params'].containing_oneof = _NNCVALUESCHUNK.oneofs_by_name['ChunkType']
_NNCVALUESCHUNK.oneofs_by_name['ChunkType'].fields.append(
  _NNCVALUESCHUNK.fields_by_name['values'])
_NNCVALUESCHUNK.fields_by_name['values'].containing_oneof = _NNCVALUESCHUNK.oneofs_by_name['ChunkType']
DESCRIPTOR.message_types_by_name['AvailableNNCProperty'] = _AVAILABLENNCPROPERTY
DESCRIPTOR.message_types_by_name['AvailableNNCProperties'] = _AVAILABLENNCPROPERTIES
DESCRIPTOR.message_types_by_name['NNCConnection'] = _NNCCONNECTION
DESCRIPTOR.message_types_by_name['NNCConnections'] = _NNCCONNECTIONS
DESCRIPTOR.message_types_by_name['NNCValuesRequest'] = _NNCVALUESREQUEST
DESCRIPTOR.message_types_by_name['NNCValues'] = _NNCVALUES
DESCRIPTOR.message_types_by_name['NNCValuesInputRequest'] = _NNCVALUESINPUTREQUEST
DESCRIPTOR.message_types_by_name['NNCValuesChunk'] = _NNCVALUESCHUNK
DESCRIPTOR.enum_types_by_name['NNCPropertyType'] = _NNCPROPERTYTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvailableNNCProperty = _reflection.GeneratedProtocolMessageType('AvailableNNCProperty', (_message.Message,), {
  'DESCRIPTOR' : _AVAILABLENNCPROPERTY,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.AvailableNNCProperty)
  })
_sym_db.RegisterMessage(AvailableNNCProperty)

AvailableNNCProperties = _reflection.GeneratedProtocolMessageType('AvailableNNCProperties', (_message.Message,), {
  'DESCRIPTOR' : _AVAILABLENNCPROPERTIES,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.AvailableNNCProperties)
  })
_sym_db.RegisterMessage(AvailableNNCProperties)

NNCConnection = _reflection.GeneratedProtocolMessageType('NNCConnection', (_message.Message,), {
  'DESCRIPTOR' : _NNCCONNECTION,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.NNCConnection)
  })
_sym_db.RegisterMessage(NNCConnection)

NNCConnections = _reflection.GeneratedProtocolMessageType('NNCConnections', (_message.Message,), {
  'DESCRIPTOR' : _NNCCONNECTIONS,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.NNCConnections)
  })
_sym_db.RegisterMessage(NNCConnections)

NNCValuesRequest = _reflection.GeneratedProtocolMessageType('NNCValuesRequest', (_message.Message,), {
  'DESCRIPTOR' : _NNCVALUESREQUEST,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.NNCValuesRequest)
  })
_sym_db.RegisterMessage(NNCValuesRequest)

NNCValues = _reflection.GeneratedProtocolMessageType('NNCValues', (_message.Message,), {
  'DESCRIPTOR' : _NNCVALUES,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.NNCValues)
  })
_sym_db.RegisterMessage(NNCValues)

NNCValuesInputRequest = _reflection.GeneratedProtocolMessageType('NNCValuesInputRequest', (_message.Message,), {
  'DESCRIPTOR' : _NNCVALUESINPUTREQUEST,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.NNCValuesInputRequest)
  })
_sym_db.RegisterMessage(NNCValuesInputRequest)

NNCValuesChunk = _reflection.GeneratedProtocolMessageType('NNCValuesChunk', (_message.Message,), {
  'DESCRIPTOR' : _NNCVALUESCHUNK,
  '__module__' : 'NNCProperties_pb2'
  # @@protoc_insertion_point(class_scope:rips.NNCValuesChunk)
  })
_sym_db.RegisterMessage(NNCValuesChunk)



_NNCPROPERTIES = _descriptor.ServiceDescriptor(
  name='NNCProperties',
  full_name='rips.NNCProperties',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=876,
  serialized_end=1173,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAvailableNNCProperties',
    full_name='rips.NNCProperties.GetAvailableNNCProperties',
    index=0,
    containing_service=None,
    input_type=Case__pb2._CASEREQUEST,
    output_type=_AVAILABLENNCPROPERTIES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetNNCConnections',
    full_name='rips.NNCProperties.GetNNCConnections',
    index=1,
    containing_service=None,
    input_type=Case__pb2._CASEREQUEST,
    output_type=_NNCCONNECTIONS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetNNCValues',
    full_name='rips.NNCProperties.GetNNCValues',
    index=2,
    containing_service=None,
    input_type=_NNCVALUESREQUEST,
    output_type=_NNCVALUES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SetNNCValues',
    full_name='rips.NNCProperties.SetNNCValues',
    index=3,
    containing_service=None,
    input_type=_NNCVALUESCHUNK,
    output_type=Definitions__pb2._CLIENTTOSERVERSTREAMREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NNCPROPERTIES)

DESCRIPTOR.services_by_name['NNCProperties'] = _NNCPROPERTIES

# @@protoc_insertion_point(module_scope)
